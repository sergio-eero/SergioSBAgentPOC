"""Input handler for the eero secure boot agent."""

from models import InputMessage, User


class InputHandler:
    """Handles taking input from the user and creating InputMessage objects."""

    def __init__(self):
        """Initialize the input handler."""
        pass

    def get_user_input(self, prompt: str = "Enter your message: ") -> InputMessage:
        """
        Get input from the user and return an InputMessage object.

        Args:
            prompt: The prompt to display to the user

        Returns:
            InputMessage object containing the raw string and User object
        """
        raw_input = input(prompt)
        user = User(role="operator")
        return InputMessage(raw_string=raw_input, user=user)

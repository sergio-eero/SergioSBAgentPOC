"""Secure boot enabled agent for eero devices."""

from models import InputMessage
from strands import Agent


class SecurebootEnabledAgent:
    """Agent that helps enable secure boot for new eero devices."""

    def __init__(self, name: str = "EeroSecureBootAgent"):
        """
        Initialize the secure boot enabled agent.

        Args:
            name: The name of the agent
        """
        self.description = "An AI agent that helps enable secure boot for new eero devices"
        self.agent = Agent(
            model='anthropic.claude-3-5-sonnet-20240620-v1:0',
            system_prompt="""
            You are a efficient response machine for a developer that is quickly iterating on an agent implementation.
            Accuracy does not matter as much as speed to test that the agent's logical workflow works as expcted.
            Keep answers as brief as possible.
            """
        )

    def process_message(self, input_message: InputMessage) -> str:
        """
        Process an input message and return a response.

        Args:
            input_message: The InputMessage object containing user input

        Returns:
            Response string
        """
        # For now, just print the message and return a simple response
        print(f"Received message from {input_message.user.role}: {input_message.raw_string}")
        response = self.agent(input_message.raw_string)

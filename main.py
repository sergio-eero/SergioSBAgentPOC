#!/usr/bin/env python3
"""
Eero Secure Boot Agent
A simple agent to help enable secure boot for new eero devices.
"""

import asyncio
import os
from input_handler import InputHandler
from secureboot_enabled_agent import SecurebootEnabledAgent

# Set AWS region environment variable
os.environ['AWS_REGION'] = 'us-west-2'
os.environ["BYPASS_TOOL_CONSENT"] = "true"

async def main():
    """Main entry point for the eero secure boot agent."""
    print("Starting Eero Secure Boot Agent...")
    print("Type 'quit' or 'exit' to stop the agent")
    print("-" * 50)

    # Initialize components
    input_handler = InputHandler()
    agent = SecurebootEnabledAgent()

    while True:
        try:
            # Get user input
            input_message = input_handler.get_user_input("\nYou: ")

            # Check for exit commands
            if input_message.raw_string.lower() in ['quit', 'exit', 'bye']:
                print("Agent: Goodbye! Have a great day!")
                break

            # Process message with agent
            agent.process_message(input_message)

        except KeyboardInterrupt:
            print("\nAgent: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())

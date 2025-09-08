#!/usr/bin/env python3
"""
Eero Secure Boot Agent - Main Module
A simple agent to help enable secure boot for new eero devices.
"""

import click


@click.command()
@click.version_option()
def main():
    """Main entry point for the eero secure boot agent."""
    click.echo("Hello World")


if __name__ == "__main__":
    main()

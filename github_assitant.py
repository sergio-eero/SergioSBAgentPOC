
from mcp.client.streamable_http import streamablehttp_client
from strands import Agent, tool
from strands.tools.mcp import MCPClient
from strands_tools import file_write
from os import environ

@tool
def query_github(query: str) -> str:
    """
    Gets information from github about the cloud and cloud-terraform repos.
    """
    formatted_query = f"{query}"
    response = str()
    try:
        github_token = environ.get("GITHUB_TOKEN", "")
        github_mcp_server = MCPClient(lambda: streamablehttp_client(
            "https://api.githubcopilot.com/mcp/",
            headers={
                "Authorization": f"Bearer {github_token}"
            },
          )
        )

        with github_mcp_server:
            tools = github_mcp_server.list_tools_sync()  + [file_write]

            # Create the research agent with specific capabilities
            research_agent: Agent = Agent(
                model='anthropic.claude-3-5-sonnet-20240620-v1:0',
                system_prompt="""
                You are a Github super agent that focuses on eero device secureboot enabling documentation and ticket tracking.
                Do not look at any other repo except the ones listed below:

                The main eero db is cloud which can be found in: https://github.com/eero-inc/cloud
                The cloud repo contains the HwModel enums in modules/data/src/main/scala/eero/data/node/HwModel.scala

                Terraform repo for cloud can be found in: https://github.com/eero-inc/cloud-terraform
                The terraform repo declares secureboot components under the secureboot module
                """,
                tools=tools,
            )


            response = str(research_agent(formatted_query))

        if len(response) > 0:
            return response

        return "I apologize, but I couldn't properly analyze your question. Could you please rephrase or provide more context?"

    # Return specific error message for English queries
    except Exception as e:
        return f"Error processing your query: {str(e)}"

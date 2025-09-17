
from mcp import StdioServerParameters, stdio_client
from strands import Agent, tool
from strands.tools.mcp import MCPClient
from strands_tools import file_write

@tool
def query_atlassian(query: str) -> str:
    """
    Gets information from atlassian and jira about secureboot. It can also create tickets for tracking steps as long as a parent jira ticket id is provided.

    Note that at eero, we call Eero wiki: "the wiki".
    """
    formatted_query = f"{query}"
    response = str()
    try:
        jira_mcp_server = MCPClient(
            lambda: stdio_client(
                StdioServerParameters(
                    command="npx",
                    args=["mcp-remote", "https://mcp.atlassian.com/v1/sse", "--transport", "sse-only"]
                )
            )
        )

        with jira_mcp_server:
            tools = jira_mcp_server.list_tools_sync()  + [file_write]

            # Create the research agent with specific capabilities
            research_agent: Agent = Agent(
                model='anthropic.claude-3-5-sonnet-20240620-v1:0',
                system_prompt="""
                You are a Atlassian super agent that focuses on eero device secureboot enabling documentation and ticket tracking.
                The core steps for enabling secureboot for an eero device can be found in https://eeroinc.atlassian.net/wiki/spaces/CLOUD/pages/2723709114

                While you focus on secureboot, you can still go and look at other jira tickets and wiki pages to get more information as needed.
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

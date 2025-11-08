from openmcp import Server
from tools import weather_tool_definition, handle_weather_tool

def create_server() -> Server:
    server_instance = Server(
        info={
            "name": "weather-mcp",
            "version": "0.2.0",
        },
        capabilities={
            "tools": {},
        }
    )

    # Handle initialized notification
    @server_instance.on_initialized
    async def on_initialized():
        print("Weather MCP client initialized")

    # Handle list tools request
    @server_instance.list_tools
    async def list_tools():
        return {"tools": [weather_tool_definition]}

    # Handle call tool request
    @server_instance.call_tool
    async def call_tool(name: str, arguments: dict):
        if name == "weather_hourly":
            return await handle_weather_tool(arguments)
        return {
            "content": [{"type": "text", "text": f"Unknown tool: {name}"}],
            "isError": True,
        }

    return server_instance
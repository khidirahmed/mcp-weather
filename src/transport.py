from openmcp import Server
from openmcp.server import StdioServerTransport, StreamableHTTPServerTransport
from uuid import uuid4
import json
import sys

def start_http_transport(server: Server, host: str = "localhost", port: int = 8080):
    """Start HTTP transport for production/cloud deployment."""
    sessions = {}

    async def handle_health_check():
        return {
            "status": "healthy",
            "timestamp": None,  # Will be set by the transport
            "service": "weather-mcp",
            "version": "0.2.0"
        }

    transport = StreamableHTTPServerTransport(
        session_id_generator=lambda: str(uuid4()),
        on_session_initialized=lambda session_id: sessions.update({session_id: server}),
        on_session_closed=lambda session_id: sessions.pop(session_id, None),
        health_check=handle_health_check
    )

    transport.start(host=host, port=port)
    print(f"Weather MCP Server listening on http://{host}:{port}")

    if host == "localhost":
        print("\nPut this in your client config:")
        print(json.dumps({
            "mcpServers": {
                "weather": {
                    "url": f"http://localhost:{port}/mcp"
                }
            }
        }, indent=2))

def run_stdio_transport(server: Server):
    """Run STDIO transport for development."""
    transport = StdioServerTransport()
    transport.start(server)
    print("Weather MCP Server running on stdio", file=sys.stderr)
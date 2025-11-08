#!/usr/bin/env python3

import os
import argparse
from dotenv import load_dotenv
from openmcp import Server
from transport import start_http_transport, run_stdio_transport
from server import create_server

def parse_args():
    parser = argparse.ArgumentParser(description="Weather MCP Server")
    parser.add_argument("--stdio", action="store_true", help="Use STDIO transport instead of HTTP")
    parser.add_argument("--port", type=int, default=8080, help="HTTP server port (default: 8080)")
    return parser.parse_args()

def main():
    try:
        # Load environment variables
        load_dotenv()
        
        # Parse command line arguments
        args = parse_args()
        
        # Create server instance
        server = create_server()
        
        if args.stdio:
            # STDIO transport for local development
            run_stdio_transport(server)
        else:
            # HTTP transport for production/cloud deployment
            port = int(os.getenv("PORT", args.port))
            is_production = os.getenv("ENV") == "production"
            host = "0.0.0.0" if is_production else "localhost"
            start_http_transport(server, host=host, port=port)
            
    except Exception as error:
        print(f"Fatal error running Weather MCP server: {error}")
        exit(1)

if __name__ == "__main__":
    main()
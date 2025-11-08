# Weather MCP Server

A Model Context Protocol (MCP) server that provides weather information using the AccuWeather API.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/khidirahmed/mcp-weather-1.git
cd mcp-weather-1
```

2. Install the package:
```bash
pip install -e .
```

## Configuration

1. Create a `.env` file in the project root with your AccuWeather API key:
```bash
ACCUWEATHER_API_KEY=your_api_key_here
```

You can get an API key by registering at [AccuWeather API](https://developer.accuweather.com/).

## Usage

### HTTP Transport (Default)

Run the server with HTTP transport (recommended for production):

```bash
weather-mcp
```

By default, the server runs on `http://localhost:8080`. You can specify a different port:

```bash
weather-mcp --port 3000
```

### STDIO Transport

For development and testing, you can use STDIO transport:

```bash
weather-mcp --stdio
```

## Client Configuration

Add this to your client's configuration:

```json
{
  "mcpServers": {
    "weather": {
      "url": "http://localhost:8080/mcp"
    }
  }
}
```

## Available Tools

### weather_hourly

Get hourly weather forecast for a location.

Parameters:
- `location` (string): The location to get weather for (city name)

Response:
```json
{
    "location": "Jakarta",
    "location_key": "208971",
    "country": "Indonesia",
    "current_conditions": {
        "temperature": {
            "value": 32.2,
            "unit": "C"
        },
        "weather_text": "Partly sunny",
        "relative_humidity": 75,
        "precipitation": false,
        "observation_time": "2024-01-01T12:00:00+07:00"
    },
    "hourly_forecast": [
        {
            "relative_time": "+1 hour",
            "temperature": {
                "value": 16,
                "unit": "C"
            },
            "weather_text": "Mostly sunny",
            "precipitation_probability": 10,
            "precipitation_type": null,
            "precipitation_intensity": null
        }
    ]
}
```

## Development

To install development dependencies:

```bash
pip install -e ".[dev]"
```

## License

MIT License
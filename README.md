# Agent Weather — Simple Weather Agent

A small Python project demonstrating a minimal weather agent. The agent can fetch current weather for a city (via wttr.in) and includes a simple command-line runner for experimentation.

## What this project does
- `agent_wheather.py`: main script that implements a lightweight weather agent and tools.
- The project uses a simple HTTP query to `wttr.in` to retrieve current weather data for a given city.

## Files
- [agent_wheather.py](agent_wheather.py)
- [requirements.txt](requirements.txt)
- [magics.txt](magics.txt)
- [t.txt](t.txt)

## Prerequisites
- Python 3.10 or newer
- Internet access (for querying wttr.in)

## Setup (Windows)
1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. (Optional) If the agent uses an external model API, add any required API keys to a `.env` file in the project root. Check `agent_wheather.py` for exact environment variable names.

## Run
Run the agent from the project root:

```powershell
python agent_wheather.py
```

Interact with the prompt or follow on-screen instructions.

## Test the weather tool directly (no model required)
To test the underlying weather fetcher in an interactive shell or short script:

```powershell
python -c "from agent_wheather import get_weather; print(get_weather('London'))"
```

This performs an HTTP query to `wttr.in` and prints a short summary like `7°C, Partly cloudy`.

## Troubleshooting
- If `wttr.in` requests fail, verify network connectivity and that `https://wttr.in/<city>?format=j1` is reachable.
- Use a virtual environment to avoid dependency conflicts.

## Contributing
Suggestions, fixes, and pull requests are welcome. Please open an issue if you find incorrect behavior or want to propose features.

## Fun image
Enjoy a tiny mascot to brighten the README:

![Fun mascot](assets/fun.svg)

---
Updated README to reflect the current project layout and quickstart instructions.


 
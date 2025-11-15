# NHL Player Comparison with LangChain & LangGraph

A CLI tool that uses LangGraph to compare NHL player career trajectories and advanced analytics, powered by Claude AI.

## Features

- Fetch historical NHL player statistics
- Compare player development trajectories
- Advanced analytics integration (Corsi, Fenwick, xG, etc.)
- AI-powered insights using Claude via LangChain
- Compare prospects to established players

## Project Structure

```
langchain-NHL-player-comp/
├── src/
│   ├── api/
│   │   └── nhl_client.py      # NHL API integration
│   ├── models/
│   │   └── player.py           # Data models for player stats
│   ├── graph/
│   │   ├── state.py            # LangGraph state definitions
│   │   └── workflow.py         # LangGraph workflow orchestration
│   ├── utils/
│   │   └── cache.py            # Caching utilities (optional)
│   └── main.py                 # CLI entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=your_actual_key_here
```

Get your API key from: https://console.anthropic.com/

### 3. Run the Application

```bash
python src/main.py compare "Connor McDavid" "Connor Bedard"
```

## Usage

### Compare Two Players

```bash
python src/main.py compare "Player 1 Name" "Player 2 Name"
```

Example:
```bash
python src/main.py compare "Connor McDavid" "Connor Bedard"
```

## Development

### NHL API Resources

- [NHL Stats API Documentation](https://gitlab.com/dword4/nhlapi)
- Example endpoints:
  - Player search: `https://api-web.nhle.com/v1/search/player?q={name}`
  - Player stats: `https://api-web.nhle.com/v1/player/{playerId}/landing`

### LangGraph Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph Tutorial](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- [State Management](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)

## How It Works

1. **Input**: User provides two player names via CLI
2. **Player Search**: LangGraph workflow validates and searches for players
3. **Data Fetching**: Retrieves historical stats and advanced analytics from NHL API
4. **AI Analysis**: Claude analyzes career trajectories and identifies patterns
5. **Comparison**: Generates intelligent comparison highlighting similarities/differences
6. **Output**: Displays formatted results in the terminal

## Next Steps

- [ ] Implement NHL API client ([src/api/nhl_client.py](src/api/nhl_client.py))
- [ ] Define player data models ([src/models/player.py](src/models/player.py))
- [ ] Create LangGraph state ([src/graph/state.py](src/graph/state.py))
- [ ] Build LangGraph workflow ([src/graph/workflow.py](src/graph/workflow.py))
- [ ] Implement CLI interface ([src/main.py](src/main.py))
- [ ] Add caching for API responses ([src/utils/cache.py](src/utils/cache.py))

## Contributing

This is a learning project. Feel free to experiment and extend it!

## License

MIT

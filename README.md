# News Agent

A conversational AI agent built using Google's Agent Development Kit (ADK) that provides news-related services through an interactive chat interface.

## Overview

This project implements a news agent that can engage in conversations with users, maintaining session state and interaction history. It's built using Python and leverages Google's ADK framework for agent management and conversation handling.

## Features

- Interactive chat interface
- Session management with state persistence
- Conversation history tracking
- Asynchronous processing of user queries
- Clean exit handling

## Prerequisites

- Python 3.x
- Google ADK
- dotenv package

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd news_agent_folder
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
Create a `.env` file in the project root and add any necessary configuration variables.

## Project Structure

```
news_agent_folder/
├── main.py              # Main application entry point
├── news_agent/
│   └── agent.py        # Root agent implementation
├── utils.py            # Utility functions
└── .env               # Environment variables
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Interact with the agent through the command-line interface:
   - Type your messages after the "You: " prompt
   - Type 'exit' or 'quit' to end the conversation

## Session Management

The application uses an in-memory session service to maintain conversation state. Each session includes:
- User identification
- Interaction history
- Session state

## Development

The main components of the application are:

1. **Session Service**: Handles session creation and state management
2. **Agent Runner**: Processes user queries through the root agent
3. **State Management**: Maintains user interaction history and session state
4. **Async Processing**: Handles asynchronous communication with the agent



## License

[MIT linsene provided ]

## Author

Author Tahasin 
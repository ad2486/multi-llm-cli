# Multi LLM CLI


███╗   ███╗██╗   ██╗██╗  ████████╗██╗      ██╗     ██╗     ███╗   ███╗       ██████╗██╗     ██╗
████╗ ████║██║   ██║██║  ╚══██╔══╝██║      ██║     ██║     ████╗ ████║      ██╔════╝██║     ██║
██╔████╔██║██║   ██║██║     ██║   ██║█████╗██║     ██║     ██╔████╔██║█████╗██║     ██║     ██║
██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════╝██║     ██║     ██║╚██╔╝██║╚════╝██║     ██║     ██║
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║      ███████╗███████╗██║ ╚═╝ ██║      ╚██████╗███████╗██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚══════╝╚══════╝╚═╝     ╚═╝       ╚═════╝╚══════╝╚═╝
                                                                                    by @ad2486  

A modular terminal-based LLM client with support for multiple AI providers.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## Features
- 🌐 Multiple providers support (OpenRouter, Groq, Google) with plans for expansion
- 💬 Multi-turn conversation with message history
- 🎨 Markdown rendering in the terminal
- ⚙️ Configurable system prompt
- 🔄 Switch models during the conversation
- 📥 Import files directly into the conversation context
- 💾 Persistent configuration between sessions
- 📚 Dynamic model listing and selection

## Requirements

- Python 3.10+
- An API key, at least one is needed, but check the supported providers

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ad2486/multi-llm-cli.git
cd multi-llm-cli
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Create your `.env` file based on the example:
```bash
cp .env.example .env
```

4. Add your API key to `.env`:
```
OPENROUTER_API_KEY=
GROQ_API_KEY=
GOOGLE_API_KEY=
(examples)
```

5. Run the CLI:
```bash
python main.py
```

## Usage

Just type your message and press Enter to chat. You can also use the following commands:

| Command | Description |
|---|---|
| `/model` | Lists models and lets you switch to another one |
| `/export <name>` | Exports a .md file of the last answer |
| `/import <file>` | Imports a file to give context to the model |
| `/system <prompt>` | Change the system prompt |
| `/provider <provider>` | Changes the provider |
| `/clear` | Clear the chat history |
| `/exit` | Exit the CLI |


## About

Hi! I'm **Arthur Duarte**, a Brazilian high school student passionate about programming.

I'm currently learning HTML/CSS/JS for fullstack freelance work, and I've already built backend projects with Python and Flask. My goal is to study Computer Science in college and work as a developer.

This CLI was one of my first real-world Python projects, built to learn about API integration, project structure, and terminal applications.

- 🐙 GitHub: [@ad2486](https://github.com/ad2486)
  


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

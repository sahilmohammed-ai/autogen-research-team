# AutoGen Research Team

A multi-agent research pipeline built with AutoGen. Give it a topic and it produces a structured report using a team of specialized agents.

## How It Works

Five agents collaborate to produce the final report:

- **Manager** — kicks off the task and coordinates the team
- **Researcher** — gathers information and presents findings
- **Fact Checker** — challenges claims and flags unsupported statements
- **Writer** — drafts a structured report from verified findings
- **Editor** — reviews and polishes the draft for clarity and completeness

The conversation ends automatically when the Manager outputs `REPORT COMPLETE`.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your-key-here
```

## Usage

Update the `message` at the bottom of `team.py` with your research topic, then run:

```bash
python team.py
```

## Requirements

- Python 3.10+
- Anthropic API key
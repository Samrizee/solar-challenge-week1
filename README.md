# Solar Challenge - Week 1

## Environment Setup

To reproduce this development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. Set up virtual environment:
   - For venv:
     ```bash
     python -m venv .venv
     source .venv/bin/activate  # On Windows: .venv\Scripts\activate
     ```
   - For conda:
     ```bash
     conda create -n solar-challenge python=3.9
     conda activate solar-challenge
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
```

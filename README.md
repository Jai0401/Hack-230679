# Automated resume screening and matching agent

This Flask application is a simple web server that predicts the completion percentage of a given resume text compared to a predefined job description using Natural Language Processing (NLP) techniques.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/) (version 3.x recommended)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

## Getting Started
Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/resume-completion-predictor.git
   cd [directory]
   python3 -m venv venv
   source venv/bin/activate
   ```
   Install all the required dependencies.
## Usage
Ensure you have a job description document in the project directory (e.g., sample_description.docx).
Run the Flask application:
```bash
python app.py
```
The server will be running at http://localhost:5000/.
## For running Agents
- Start a Virtual Environment.
- Then will run ai-agent using:
```bash
python ai-agent.py
```
- run user-agent(in another terminal):
```bash
python user_agent.py
```


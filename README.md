# Job Application AI Agent

This AI agent helps you process job descriptions and automatically generate tailored application materials. It can:
1. Read and analyze job descriptions
2. Extract key requirements
3. Generate customized cover letters
4. Create a one-minute video script for self-introduction

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
```

2. Install the required packages:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

3. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Create a `user_profile.yaml` file with your professional information:
```yaml
name: Your Name
title: Your Professional Title
experience:
  - company: Company Name
    role: Your Role
    duration: Duration
    highlights:
      - Key achievement 1
      - Key achievement 2
skills:
  - Skill 1
  - Skill 2
education:
  - degree: Your Degree
    institution: Institution Name
    year: Graduation Year
```

## Usage

1. Save the job description in a text file (e.g., `job_description.txt`)

2. Run the agent:
```bash
python main.py
```

3. When prompted, enter the path to your job description file.

4. The agent will:
   - Extract key requirements from the job description
   - Generate a tailored cover letter
   - Create a one-minute video script
   - Save all outputs to the `outputs` directory

## Output Files

The agent creates the following files in the `outputs` directory:
- `application_package.yaml`: All generated content in YAML format
- `job_description.txt`: The original job description
- `requirements.txt`: Extracted requirements
- `cover_letter.txt`: Generated cover letter
- `video_script.txt`: One-minute video script

## Customization

You can modify the prompt templates in `src/agent.py` to adjust the style and tone of the generated content.
# AI-JD-agent-

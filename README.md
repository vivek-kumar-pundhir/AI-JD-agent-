# Job Application AI Agent

This AI agent helps you process job descriptions and automatically generate tailored application materials. It can:
1. Read and analyze job descriptions
2. Extract key requirements
3. Generate customized cover letters
4. Create a one-minute video script for self-introduction

## How to Run (Google Colab or Local)

### **Recommended: Run in Google Colab (No API Key Needed)**

1. **Open [Google Colab](https://colab.research.google.com/)**
2. **Upload these files:**
   - `main.py`
   - `user_profile.yaml`
   - `JD.txt` (your job description)
   - `src.zip` (your `src` folder zipped)
3. **Unzip your code:**
   ```python
   !unzip -o src.zip
   ```
4. **Install required packages:**
   ```python
   !pip install transformers accelerate spacy pyyaml
   !python -m spacy download en_core_web_sm
   ```
5. **Run the agent:**
   ```python
   !python main.py
   ```

### **If Running Locally**

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate    # On Windows
   ```
2. Install the required packages:
   ```bash
   pip install transformers accelerate spacy pyyaml
   python -m spacy download en_core_web_sm
   ```
3. Make sure your files are organized as:
   - `main.py`
   - `user_profile.yaml`
   - `JD.txt`
   - `src/agent.py` (and other code files)
4. Run the agent:
   ```bash
   python main.py
   ```

## Input Files
- `JD.txt`: The job description (plain text)
- `user_profile.yaml`: Your professional profile (YAML format)

## Output Files
The agent creates the following files in the `outputs` directory:
- `application_package.yaml`: All generated content in YAML format
- `job_description.txt`: The original job description
- `requirements.txt`: Extracted requirements
- `cover_letter.txt`: Generated cover letter
- `video_script.txt`: One-minute video script

## Customization
You can modify the prompt templates in `src/agent.py` to adjust the style and tone of the generated content.

---

**No API key is needed if you use the local model (default: distilgpt2).**
If you want to use a cloud LLM, see the code comments for how to adapt.

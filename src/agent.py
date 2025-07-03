import os
from dotenv import load_dotenv
import spacy
import yaml
from transformers import pipeline

class JobApplicationAgent:
    def __init__(self):
        load_dotenv()
        self.generator = pipeline("text-generation", model="distilgpt2")
        self.nlp = spacy.load('en_core_web_sm')

    def read_job_description(self, file_path):
        """Read and process the job description from a text file."""
        with open(file_path, 'r') as file:
            return file.read()

    def extract_requirements(self, job_description):
        """Extract key requirements from the job description using SpaCy."""
        doc = self.nlp(job_description)
        requirements = []
        for sent in doc.sents:
            if any(keyword in sent.text.lower() for keyword in 
                ['required', 'requirements', 'qualifications', 'must have', 'skills']):
                requirements.append(sent.text.strip())
        return requirements

    def generate_cover_letter(self, job_description, requirements, user_profile):
        """Generate a tailored cover letter based on the JD and user profile."""
        prompt = (
            "Dear Hiring Manager,\n\nBased on the following job requirements and my profile, "
            "write a professional and engaging cover letter:\n\n"
            f"Job Description: {job_description}\n"
            f"Key Requirements: {'; '.join(requirements)}\n"
            f"My Profile: {user_profile}\n"
            "The cover letter should highlight relevant experience and skills while maintaining a professional tone.\n"
        )
        result = self.generator(prompt, max_length=300, do_sample=True, temperature=0.7)
        return result[0]['generated_text']

    def generate_video_script(self, cover_letter, user_profile):
        """Generate a one-minute video script introduction."""
        prompt = (
            "Create an engaging one-minute video script where I introduce myself based on:\n"
            f"Cover Letter Highlights: {cover_letter}\n"
            f"My Profile: {user_profile}\n"
            "The script should be natural, professional, and highlight key strengths while being time-conscious (one minute).\n"
        )
        result = self.generator(prompt, max_length=300, do_sample=True, temperature=0.7)
        return result[0]['generated_text']

    def save_outputs(self, outputs, output_dir='outputs'):
        """Save all generated content to files."""
        os.makedirs(output_dir, exist_ok=True)
        with open(f'{output_dir}/application_package.yaml', 'w') as f:
            yaml.dump(outputs, f)
        for key, content in outputs.items():
            with open(f'{output_dir}/{key}.txt', 'w') as f:
                if isinstance(content, list):
                    f.write('\n'.join(str(item) for item in content))
                else:
                    f.write(str(content))

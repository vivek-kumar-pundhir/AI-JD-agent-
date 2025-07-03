import os
import spacy
import openai
from dotenv import load_dotenv
from moviepy.editor import *

class JobAgent:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.nlp = spacy.load("en_core_web_sm")

    def read_job_description(self, file_path):
        """Read and return the contents of a job description file"""
        with open(file_path, 'r') as file:
            return file.read()

    def extract_requirements(self, job_description):
        """Extract key requirements from job description using spaCy"""
        doc = self.nlp(job_description)
        requirements = []
        
        # Look for requirement patterns
        for sent in doc.sents:
            if any(keyword in sent.text.lower() for keyword in ["required", "requirements", "qualifications", "must have", "skills"]):
                requirements.append(sent.text.strip())

        return requirements

    def generate_cover_letter(self, job_description, requirements):
        """Generate a tailored cover letter using OpenAI GPT"""
        prompt = f"""
        Job Description: {job_description}
        Key Requirements: {', '.join(requirements)}
        
        Write a professional and engaging cover letter that addresses these requirements 
        and positions me as an ideal candidate. Make it personal and specific to the role.
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional career advisor helping to write a compelling cover letter."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message['content']

    def create_video_script(self, requirements, cover_letter):
        """Generate a one-minute video script introduction"""
        prompt = f"""
        Based on these job requirements: {', '.join(requirements)}
        And this cover letter: {cover_letter}
        
        Create a natural, engaging one-minute video script for a self-introduction that:
        1. Highlights my most relevant qualifications
        2. Shows enthusiasm for the role
        3. Demonstrates personality and cultural fit
        Keep it conversational and around 150 words.
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a video script writer specializing in professional introductions."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message['content']

def main():
    agent = JobAgent()
    
    # Get the job description file path from user
    job_desc_path = input("Please enter the path to your job description text file: ")
    
    # Process the job description
    job_description = agent.read_job_description(job_desc_path)
    requirements = agent.extract_requirements(job_description)
    
    print("\nExtracted Requirements:")
    for req in requirements:
        print(f"• {req}")
    
    # Generate cover letter
    cover_letter = agent.generate_cover_letter(job_description, requirements)
    print("\nGenerated Cover Letter:")
    print(cover_letter)
    
    # Generate video script
    video_script = agent.create_video_script(requirements, cover_letter)
    print("\nVideo Script:")
    print(video_script)

if __name__ == "__main__":
    main()

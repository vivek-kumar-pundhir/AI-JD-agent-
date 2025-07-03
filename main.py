from dotenv import load_dotenv
load_dotenv('.env')
from src.agent import JobApplicationAgent
import yaml

def main():
    # Initialize the agent
    agent = JobApplicationAgent()
    
    # Load user profile
    with open('user_profile.yaml', 'r') as f:
        user_profile = yaml.safe_load(f)
    
    # Process job description
    jd_path = input("Please enter the path to the job description text file: ")
    job_description = agent.read_job_description(jd_path)
    
    # Extract requirements
    requirements = agent.extract_requirements(job_description)
    print("\nExtracted Requirements:")
    for req in requirements:
        print(f"- {req}")
    
    # Generate cover letter
    cover_letter = agent.generate_cover_letter(
        job_description,
        requirements,
        yaml.dump(user_profile)
    )
    print("\nGenerated Cover Letter:")
    print(cover_letter)
    
    # Generate video script
    video_script = agent.generate_video_script(cover_letter, yaml.dump(user_profile))
    print("\nGenerated Video Script:")
    print(video_script)
    
    # Save all outputs
    outputs = {
        'job_description': job_description,
        'requirements': requirements,
        'cover_letter': cover_letter,
        'video_script': video_script
    }
    
    agent.save_outputs(outputs)
    print("\nAll outputs have been saved to the 'outputs' directory.")

if __name__ == "__main__":
    main()

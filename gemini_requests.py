from google import genai
import os
import importlib
import gemini_requests
importlib.reload(gemini_requests)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def resume_grader_response(resume_text):
    prompt = f"""
        You are an expert resume reviewer.

        Grade the following resume using this rubric and return results in JSON format:
        {{
        "Grammar_Spelling_and_Formatting": <score out of 20>,
        "Name_Contact_Information": <score out of 10>,
        "Experience": <score out of 30>,
        "Education": <score out of 15>,
        "Skills": <score out of 15>,
        "Additional_Information": <score out of 10>,
        "Total": <total out of 100>
        }}
        Then, briefly explain any major deductions after the JSON.
        There will be some spacing issues but they are not important since it is most likey do to the PDF to text conversion.
        Here is the resume:
        \"\"\"{resume_text}\"\"\"
    """
    response = client.models.generate_content(
        model = "gemini-2.0-flash", contents = prompt
    )
    return response
    
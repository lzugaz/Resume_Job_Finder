from resume_reader import pdf_to_text
from gemini_requests import resume_grader_response
import re
import json

resume_text = pdf_to_text("resume.pdf")
gemini_response = resume_grader_response(resume_text) #This calls the gemini api
resume_grading = gemini_response.text


match = re.search(r"```json\s*(\{.*?\})\s*```", resume_grading, re.DOTALL) #This regex pattern matches the JSON object inside the triple backticks
if match:
    json_data = json.loads(match.group(1))
    print(json_data)


Grammar_Spelling_and_Formatting = json_data["Grammar_Spelling_and_Formatting"]
Name_Contact_Information = json_data["Name_Contact_Information"]
Experience = json_data["Experience"]
Education = json_data["Education"]
Skills = json_data["Skills"]
Additional_Information = json_data["Additional_Information"]
Total = json_data["Total"]

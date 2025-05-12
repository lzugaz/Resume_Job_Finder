from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import json
import re
from resume_reader import pdf_to_text

model_id = "deepseek-ai/deepseek-llm-7b-chat"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
resume = pdf_to_text("resume.pdf")

def build_resume_grading_prompt(resume_text):
    return f"""
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

Here is the resume:
\"\"\"{resume_text}\"\"\"
"""

def extract_json_from_output(output):
    match = re.search(r"\{.*?\}", output, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return None
    return None


def grade_resume():
    resume_text = pdf_to_text("resume.pdf")
    prompt = build_resume_grading_prompt(resume_text)
    response = pipe(prompt, max_new_tokens=1024)[0]['generated_text']
    
    grading_json = extract_json_from_output(response)
    
    if grading_json:
        print("✅ Grading Results (JSON):")
        print(json.dumps(grading_json, indent=2))
    else:
        print("❌ Failed to extract JSON from model output.")
        print("Raw response:")
        print(response)

grade_resume()
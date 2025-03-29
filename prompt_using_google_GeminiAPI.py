import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # List available models
# for m in genai.list_models():
#     print(m.name, " - ", m.supported_generation_methods)


model = genai.GenerativeModel("gemini-2.0-flash")

text = f""" python, java, c, c++, sql, java microservices, springboot, kafka, machine learning, AI, 
prompt engineering, html, css, bootstrap, communication, team-worker """

prompt = f""" Act like a Skill Recommender system and recommend what next skills a user should learn based on job 
market, successful people, relevant to their skills, growth and potential interest based on a user's existing skills. 
The user's existing skills are delimited by triple backticks : ```{text}``` 
"""

response = model.generate_content(prompt)

print(response.text)

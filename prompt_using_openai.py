import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_completion(user_prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": user_prompt}]
    response_from_chat = client.chat.completions.create(model=model,
                                                        messages=messages,
                                                        temperature=0)
    return response_from_chat.choices[0].message.content


text = f""" Lorde talks the way she dances, with the full and free use of all limbs. Sitting outside a hotel in 
California – where the New Zealand-born musician, real name Ella Yelich-O’Connor, has come to perform at the 
Coachella festival – she flails, fidgets, and flings out her fingertips for emphasis. She runs her hands into her 
great mane of hair (Pixar-springy and the colour of burnt toast) and talks with her palms pressed into her head. 
Discussing her imminent second album, Melodrama, Lorde waggles her legs excitedly. And to help illustrate what it 
felt like, five or six years ago, to be an ambitious kid in far-flung Auckland, making music that she hoped would one 
day be heard by a wider world, she stretches out her arms. There was an element of reaching out. Do you see me? Do 
you hear me? I’m over here. """
prompt = f"""
Summarize the text delimited by triple backticks into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)

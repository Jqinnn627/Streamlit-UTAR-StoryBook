import os
import streamlit as st  #important
from openai import OpenAI
#from google.colab import userdata
#from IPython.display import Image

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY']) #change

#Story
def story_gen(prompt):
  System_prompt = """ 
  You are a world author for young adults fiction short stories. 
  Given a concept, generate a short story relevent to the themes of      the concept with a twist ending.
  The total length of the story should be within 100 words
  """

  response = client.chat.completions.create(model="gpt-4o-mini",
                                            messages=[{
                                                "role": "system",
                                                "content": System_prompt
                                            }, {
                                                "role": "user",
                                                "content": prompt
                                            }],
                                            temperature=1.3,
                                            max_tokens=2000)

  return response.choices[0].message.content

#Cover
def design_gen(prompt):
  system_prompt = """
  You will be given a short story. Generate a prompt for a cover art     that is suitable for the story. The prompt is for dall-e-2
  """
  response = client.chat.completions.create(model="gpt-4o-mini",
                                            messages=[{
                                                "role": "system",
                                                "content": system_prompt
                                            }, {
                                                "role": "user",
                                                "content": prompt
                                            }],
                                            temperature=1.3,
                                            max_tokens=1000)

  return response.choices[0].message.content

#Cover art
def art_gen(prompt):
  response = client.images.generate(model="dall-e-2",
                                    prompt=prompt,
                                    size="1024x1024",
                                    n=1)

  return response.data[0].url

prompt = st.text_input("Enter a prompt")
if st.button("Generate"):
  story = story_gen(prompt)
  design = design_gen(story)
  art = art_gen(design)
  st.caption(design)
  st.divider()
  st.write(story)
  st.divider()
  st.image(art)

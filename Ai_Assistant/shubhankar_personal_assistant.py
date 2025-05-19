
# !pip install -q -U google-generativeai
# !pip install gtts

from google.colab import userdata # type: ignore
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
model = genai.GenerativeModel('gemini-2.0-flash')

import pathlib
import textwrap
from gtts import gTTS

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from IPython.display import Audio, display


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Corrected: Use the defined GOOGLE_API_KEY instead of GOOGLE_API_KEY_1
genai.configure(api_key=GOOGLE_API_KEY)

def ask_question(name):
    ques='Hey '+ name + ' what do you want ?'
    ques=input(ques)
    return ques

def classify_question(ques):
    goahead_with_web_search=False
    device_lst=['alarm','reminder','message','call']
    personal_lst=['who are you','who created you']

    device=False
    for i in device_lst:
        if i in ques:
            device=True

    if device:
        print("This question is related to device things which is not supported in our Jarvis assistant!")

    personal_question=False
    for i in personal_lst:
        if i in ques.lower():
            personal_question=True

    if personal_question:
        print("Hey am a personal assistant created by Shubhankar Tiwary")

    if device:
        goahead_with_web_search=False
    elif personal_question:
        goahead_with_web_search=False
    else:
        goahead_with_web_search=True

    return goahead_with_web_search

classify_question("who are you?")

#Searching with Google Gemini

def ask_gemini(ques):
  modified_prompt='Hey Gemini, give me answer to this question '+ques+' in maximum 500 words'
  response = model.generate_content(modified_prompt)
  to_markdown(response.text)
  return response.text
  return response.text

def speak(answer):
  tts=gTTS(answer)
  tts.save('audio.mp3')
  display(Audio('audio.mp3', autoplay=True))

# # Add this block to list available models
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)


have_any_other_ques='y'
name=''

while have_any_other_ques=='y':

  if name=='':
    name=input("What is your name? - ")

  q=ask_question(name)

  go_ahead=classify_question(q)
  answer=''

  if go_ahead==True:
    answer=ask_gemini(q)
    speak(answer)
    print(answer)

  have_any_other_ques=input("Do you have any other questions ?")




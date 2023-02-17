import pandas as pd
import openai
import datetime
import os
import colorama
from colorama import Fore, Back, Style

openai.api_key = ('OPEN_API_KEY')

# define the dataframe
df = pd.DataFrame(columns=['Question', 'Answer'])

# function to add question and answer to dataframe
def add_qa(question, answer):
    df.loc[len(df)] = [prompt, response]
    
def generate_response(prompt):
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()


while True:
#    print("-------------------------------------")
    now = datetime.datetime.now()
    now1 = str(now)
    current_year = datetime.datetime.now().year
    c = str(current_year)
    p = now.strftime("%A, %B %d, " + c + " at %I:%M %p")
    length = len(p)
    print('-' * length)
    print(p)
    print('-' * length)
#    print(now.strftime("%A, %B %d, " + c + " at %I:%M %p"))
#    print(now1)
#    print("-------------------------------------")
    print("")
    # get user input
    prompt = input(Fore.RED + "Enter your message or question: \n" + Style.RESET_ALL)
        # check if user input is 'quit'
    prompt2 = prompt.lower()
    if prompt2 == 'quit':
         print("Program Ended!")
         quit()
    if prompt2 == 'quit.':
         print("Program Ended!")
         quit()

    response = generate_response(prompt)
    print()
    # provide response
    print(Fore.RED + 'ChatGPT replied: \n' + Style.RESET_ALL)
    print(Fore.GREEN + response + Style.RESET_ALL)
    print()
    # add question and answer to dataframe
    add_qa(prompt, response)
    # save dataframe to csv file
#    df.to_csv('ChatGPT.csv', index=False)
    df.to_csv('ChatGPT.csv', mode='a', index=False, header=False)
    now = datetime.datetime.now()
    now1 = str(now)

    with open('chatlog.txt', 'a') as f:
      f.write('###XXX###' + p +'#####'+ prompt + '-------\n#####' +response + '#####\n')
    with open('ChatBrain.txt', 'a') as f:
      f.write(p + '#####' + prompt + "#####"  +response + "###########\n")
    with open('response.txt', 'w') as f:
        f.write(response)
    with open('prompt.txt', 'w') as f:
        f.write(prompt)

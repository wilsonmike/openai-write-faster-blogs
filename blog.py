import os
import openai
import config 

openai.api_key = config.OPENAI_API_KEY

def generateBlogTopics(prompt1):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate blog topic ideas on: {}. \n \n 1. ".format(prompt1),
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']

def generateBlogSections(prompt1):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Expand the blog title into high level blog sections: {} \n\n- Introduction: ".format(prompt1),
        temperature=0.65,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']

def blogSectionExpander(prompt1):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Expand the blog section into a detailed professional, witty and clever explanation. \n\n {}".format(prompt1),
        temperature=0.65,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']

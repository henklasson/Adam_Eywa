import openai 

openai.api_key_path = '/home/henrikvklasson/Adam_n_Eve/API_KEY.txt'

#If your API key is stored in a file, you can point the openai module at it 
# with 'openai.api_key_path = <PATH>'.

#openai.api_key = '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'

model = 'text-davinci-003'

# completion = openai.Completion.create(model="ada", prompt="Hi THere")
# print(completion.choices[0].text)

prompt= "What is the capital of Norway?"

response = openai.Completion.create(
    model=model,
    prompt = prompt,
    temperature = 0.5,
    max_tokens = 10,
    top_p = 1.0,
    frequency_penalty=0.0,
    presence_penalty = 0.0
)

answere = response['choices'][0]['text']

answere = answere.lstrip()
print(answere)

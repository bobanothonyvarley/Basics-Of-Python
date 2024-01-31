#easy access to chatgpt 3.5 api
from openai import OpenAI


#if frontend wants to use chatgpt API, use this text_presentation = 0, with 
# text_presentation = 0   meaning that you will get a human-readable response from chatgpt
# text_presentation = 1   meaning that you will get the data in the form of a python dictionary

def message_chatGPT(message, text_presentation=0, existing_messages=[]): 

    structure = ''

    # if == 0, no need to change anything
    if (text_presentation==1): 
    # in the form of d3, so we don't have to format ourselves.
    # all in one line because dealing with indents in python is awkward, but makes no difference to data stored, so it removes \t, \n, etc
    # ' dont add any notes ' means dont add a concluding statement, as AI usually do.
        structure = "For each node, give a brief description in a 'description' key. Give the answer in the form of a json d3 tree, all in one line. Do not add any extra notes"
    

    
    #store the response
    existing_messages.append( {"role" : 'user', 'content' : message + structure})

    #gain access with api key
    # IMPORTANT: do not store API key on Github in plain text, i've heard a few horror stories about AWS users leaving their API key in a public repo, then some web scraper finds it and uses 5000 dollars worth of API calls.
    api_key = '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'
    client = OpenAI( api_key=api_key)

    #get reponses, this is just how using the api works
    response = client.chat.completions.create( model='gpt-3.5-turbo', messages=existing_messages )

    #strip away padding we dont need
    content = response.choices[0].message.content.strip()
    return content
# message_chatGPT() end

#this will return a dictionary with attributes. the frontend should not be calling this
def store_as_d3_tree(content):
    #store data into d3 tree node, ie, nested dicts
    #initialise node
    node = ''

    #get code as string
    code = 'node = ' + content

    # node = '...' == the chatgpt d3 formatted dict. run the string as actual code
    exec( code)

    return node
# store_as_d3_tree() end


'''
message = 'give 3 benefits of jogging'#input('Enter your query: \n')
content = message_chatGPT(message)
node = store_as_d3_tree(content)
'''

# copy and pasted from cgpt response, if you are having trouble with the format, this is how the data is formatted and stored
'''
node = {"name": "Jogging", "children": [{"name": "Physical Fitness", "description": "Jogging helps improve cardiovascular fitness, increases lung capacity, and strengthens muscles and bones."}, {"name": "Weight Management", "description": "Regular jogging can aid in burning calories, resulting in weight loss or maintenance."}, {"name": "Mental Well-being", "description": "Jogging releases endorphins, which can enhance mood, reduce stress, and improve mental health."}]}

'''

'''
#for displaying results
print( "\nname of parent node: ", node['name'], '\n')

print('\nNode content: ******************************************************\n')
for child in node['children']:
    print(child['name'])
    print(child['description'])
print('\n********************************************************************\n')

'''



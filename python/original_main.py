# Imports
import requests
import json
# from decouple import config
import jsonpickle
# import pprint


# Variables
# apiurl = config('URL') # Go in .env to set the URL.
# key = config('KEY') # Go in .env to set the key.

apiurl = 'https://api.cloud.ox.security/api/apollo-gateway'
key = 'ox_Z-PNHfMtX~ruy-oUMhLQodINoWpXBOXowL6R'

# class Thing(object):
#    def __init__(self, id):
#        self.id = id


# Deserialize Function
def deserialize (response):
    #frozen = jsonpickle.encode(response)
    thawed = jsonpickle.decode(response)
    for check in thawed['data']['getIssues']['issues']:
        id = check['id']
        desc = check['mainTitle']
        owners = check['owners']
        print("Issue ID:", id)
        print("Issue Description:", desc)
        print("Issue Owners:", owners)
        print("")
    ### Custom Deserialization Method ----
    #data = json.loads(response) # Formats the JSON response into raw format.
    #for check in data['data']['getIssues']['issues']: # FOR loop to get each ID and Description.
        #id = check['id'] # Sets the ID as checking for the ID in the Issues category
        #desc = check['mainTitle'] # Sets the Description as checking for the Description in the Issues category
        #print("Issue ID:", id) # Prints the ID
        #print("Issue Description:", desc) # Prints the Desc
        #print("") # Newline
    ### ----

# Reading Files

with open('./request/getIssues.query.json', 'r') as query_file: 
    query = query_file.read()

with open('./request/getIssues.variables.json', 'r') as variables_file:
    variables = json.load(variables_file)

# Setting Post Params

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'{key}',
}

body = {
    'query': query,
    'variables': variables,
}

# Post Request

try:
    response = requests.post(apiurl, headers=headers, json=body)
    if response.status_code == 200:
        result = response.json()
        passresult = json.dumps(result, indent=2)
        deserialize(passresult)
    else:
        print(f'GraphQL request failed with status code: {response.status_code}')

except requests.exceptions.RequestException as error:
    print(f'Error: {error}')
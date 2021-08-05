import json

def set_environment_variables():
    json_file = open("..\\vault.json")
    variables = json.load(json_file)
    json_file.close()
    print(variables)
    return(variables)
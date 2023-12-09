import json


def write_json(new_data, filename='training_data.jsonl'):
    with open(filename, 'a') as file:
        file.write(json.dumps(new_data, ensure_ascii=False) + '\n')


add_data = True
while add_data:
    question = input("Question: ")
    
    if question.lower() == "exit":
        add_data = False
        break
    
    answere = input("Answere: ")
    
    ny_data = {"prompt": f"{question}", "completion": f"{answere}"}
    write_json(ny_data)
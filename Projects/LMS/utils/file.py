import json

def read_data(data_path):
    with open(data_path) as f:
        data = json.load(f)
    return data

def write_data(LMS,data_path):
    with open(data_path,'w') as f:
        json.dump(LMS,f)
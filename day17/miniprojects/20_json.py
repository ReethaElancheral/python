# 20. JSON Stream Processor 
# Objective: Lazily load and process a large JSON file. 
# Requirements: 
#  Read file line-by-line. 
#  Yield parsed objects. 
#  Stop at a certain key match or file end.

import json

def json_stream_processor(file_path, stop_key=None, stop_value=None):
    with open(file_path, 'r') as f:
        for line in f:
            try:
                obj = json.loads(line.strip())
                yield obj
                if stop_key and obj.get(stop_key) == stop_value:
                    break
            except json.JSONDecodeError:
                continue

# Example usage:
# Assuming `data.json` is a file with one JSON object per line
for record in json_stream_processor('data.json', stop_key='status', stop_value='done'):
    print(record)

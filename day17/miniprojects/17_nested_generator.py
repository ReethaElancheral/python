# 17. Nested Generator Chain (Pipeline) 
# Objective: Build a data-processing pipeline using chained generators. 
# Requirements: 
#  Generator 1: yields raw data 
#  Generator 2: filters data 
#  Generator 3: transforms data 
#  Combine all three into one loop.

def raw_data():
    for i in range(20):
        yield i

def filter_data(source):
    for val in source:
        if val % 2 == 0:
            yield val

def transform_data(source):
    for val in source:
        yield val * val

# Pipeline chaining
pipeline = transform_data(filter_data(raw_data()))
for result in pipeline:
    print(result)

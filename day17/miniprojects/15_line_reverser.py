# 15. Line Reverser from File 
# Objective: Read lines from a file and yield each reversed line. 
# Requirements: 
#  Strip newline and reverse content. 
#  Use generator to yield reversed strings. 
#  Stop gracefully at EOF. 

def reversed_lines(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()[::-1]

# Example usage:
# Assuming 'sample.txt' has some lines
for reversed_line in reversed_lines('sample.txt'):
    print(reversed_line)

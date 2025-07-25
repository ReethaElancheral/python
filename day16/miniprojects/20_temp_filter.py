# 20. Weather Log Reader 
# Goal: Read temperature logs from a file and yield temperature only if above 30°C. 
# Requirements: 
#  File contains one temperature per line 
#  Use iterator to read & filter 
#  End reading at EOF 

class TemperatureFilter:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.file.readline()
            if not line:
                self.file.close()
                raise StopIteration
            temp = int(line.strip())
            if temp > 30:
                return temp

# Usage & Output
print("Temperatures above 30°C:")
for temp in TemperatureFilter('weather_log.txt'):
    print(f"{temp}°C")

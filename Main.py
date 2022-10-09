from typing import List

def merge_sort(data) -> None:
  # Write code here
  if len(data) > 1:
    mid = len(data)//2
    left= data[:mid]
    right= data[mid:]
   

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)

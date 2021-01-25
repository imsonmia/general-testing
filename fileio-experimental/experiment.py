# In Git VCS
# Lasted Edited: 2021-01-26 01:04:28
file = open(file="test_data.txt", mode="r+", buffering=1)
print(f"Filename: {file.name}")
print(f"Encoding: {file.encoding}")
print(f"Content: '{file.read()}'")

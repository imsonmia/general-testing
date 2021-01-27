# In Git VCS
# Lasted Edited: 2021-01-26 01:04:28
file = open(file="usr.txt", mode="r+", buffering=1)
print(f"Filename: {file.name}")
print(f"Encoding: {file.encoding}")
usr = str(file.read())

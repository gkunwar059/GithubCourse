# converting string to raw string 
# to remove the escape squence the python use raw string 
loc="Home\\Interntask"

with open(loc,'r') as file:
    text=file.read()
    print(text)
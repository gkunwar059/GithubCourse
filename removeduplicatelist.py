# remove duplicate
name=['ganesh','harish','ramesh','abishek','henri']

name=list(dict.fromkeys(name,1))
print(name)
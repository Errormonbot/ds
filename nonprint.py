import string
#removing non-printable characters
printable = set(string.printable)
baddata = "Data\x00Science with \x02 funny characters is \x10bad!!!"
cleandata =''.join(filter(lambda x: x in string.printable,baddata))
print(cleandata)
#removing unwanted spaces
baddata = "      Data Science with too many spaces is bad!!!           "
print('>',baddata,'<')
cleandata=baddata.strip()
print('>',cleandata,'<')

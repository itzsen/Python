import re, pyperclip


#Create Regex for Phone
# 317-460-6373, 460-6373, (317) 460-6373, 460-6373 ext 12345, ext.12345, x12345

PhoneRegex=re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?  #area code (optional)
(\s|-)                    #seperator
\d\d\d                    #first 3 digits
-                         #seperator
\d\d\d\d                  #last 4 digits
(((ext(\.)?\s)|x)         #extension word part(optional)
 (\d{2,5}))?               #extension number part (optional)
)
''',re.VERBOSE)


#Create Regex for email
# some.+_thing@some.+_.com

emailRegex=re.compile(r'''
[a-zA-Z0-9_.+]+ #name part
@               #@ symbol
[a-zA-Z0-9_.+]+ #domain part
''',re.VERBOSE)

# Get the text off the clipboard
text=pyperclip.paste()

#get the text off the clipboard

extractedphone = PhoneRegex.findall(text)
extractedemail = emailRegex.findall(text)

print(extractedphone[0])
print(extractedemail)

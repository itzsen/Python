import pprint

message = 'my name is senthil'

count={}

for character in message.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1

#print(count)

#pprint.pprint(count)

rjtext=pprint.pformat(count)
print(rjtext)

#print welcome message
message1="'hello\"s world'"
print(message1)
message2="""Hello
World

"""
print(message2)
print(len(message1))
print(message1[-1])
print(message1[:6])
print(message1[9:])
#using methods

print(message1.upper())
print(message1.count('o'))
print(message1.find('o'))
print(message1.replace('"','is'))

msg1='hello'
msg2='dev'
print(msg1+' '+msg2)
print('{} {}'.format(msg1,msg2))

print(dir(str))
print(help(str.strip))
msg3= '...hello dev...'
print(msg3.strip('.' )) #only from beginning and end
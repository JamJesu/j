#*************************************************************
# Name:Jeswin Antony M                         Class:S3 IT
#  Roll No:20                                   Date:
#
#		 NO OF VOWELS,CONSONANTS,WORD,'?'
#**************************************************************
v=0
c=0
w=1
q=0
s=input("enter the string:(min 1 word)")
for i in s:
	if(i=='a' or i=='e' or i=='i' or i=='o'or i=='u'or i=='A'
           or i=='E' or i=='I' or i=='O'or i=='U'):
		v=v+1
	elif(i==' '):
		w=w+1
	elif(i=='?'):
                q=q+1
for i in s:
	if(i>='a' and i<='z'):
		c=c+1
	elif(i>='A' and i<='Z'):
		c=c+1
print("vowels:",v," word:",w," question mark:",q,"consonants: ",c-v)
#        SAMPLE OUTPUT
#enter the string:(min 1 word)hi hi? Go Go happy
#vowels: 5  word: 5  question mark: 1 consonants:  8

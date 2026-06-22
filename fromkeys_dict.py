a='mehar'
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))#it will raise error bcz we dont have values for keys that's why
#we use fromkeys method to overcome this error
b=dict.fromkeys(a)
print(b)
c=dict.fromkeys(a,'begum')
print(c)
c['a']='anas'
print(c)

#To print fibonacci series
a=int(input("Input no. upto which fibonacci series to be print "))
b=0
c=1
d=0
print(b)
print(c)
while d<=a:
	d=b+c
	print(d)
	b=c
	c=d

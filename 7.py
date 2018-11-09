def string_reverse(str):

 	reverse=''
 	i=len(str)
 	while i>0:
 		reverse=reverse+str[i-1]
 		i=i-1
 	return reverse;
str=input("enter the string\n")
print("reverse of string is ",string_reverse(str)) 
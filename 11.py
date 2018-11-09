def area_circle(r):
	return(3.175*r*r);

def area_triangle(b,h):
	return(0.5*b*h);

def area_square(a):
	return(a*a);


r=int(input("enter radius of circle"))
b=int(input("enter base of triangle"))
h=int(input("enter height of traingle"))
a=int(input("enter side of square"))

print("area of circle",area_circle(r))

print("area of triangle",area_triangle(b,h))

print("area of square",area_square(a))
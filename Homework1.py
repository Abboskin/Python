'''23/10/2024
We studied:
1) How to use GitHub
2) Data types - int(1,2), float(3.14), complex(4 + 5j), str("Hello world"), bool(True(1), False(0))
3) Functions - print, type, id, input + float(input(...))
'''

#simple_calc
length = float(input("What is the length of rectangle?: "))
width = float(input("What is the width of rectangle?: "))

area = length*width
perimeter = 2*(length + width)

print("The area is ", area)
print("The perimeter is ", perimeter)

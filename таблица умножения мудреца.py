def simple_multiplication(x, y):
    s=(100-((100-x)+(100-y)))*100+(100-x)*(100-y)
    if s==x*y:
        return "True"
    else:
        return "False"
x,y=int(input()),int(input())
print(simple_multiplication(x, y))
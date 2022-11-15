x = 5  #  isort error
y = 10  #  pylint space error 
temp = x
x = y
y = temp
print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))


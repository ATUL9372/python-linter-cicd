 import os     # flake8 error in this code not use import os 
  
  x = 5  # black linter (formatter) error this line 
        # black linter extra spaces line add
x = 5 # isort error
y=10  # pylint space error  
temp = x




x = y
y = temp
x = y       # isort error multiple time same line use in code 
# print('The value of x after swapping: {}'.format(x))
# print('The value of y after swapping: {}'.format(y))
print('The value of x after swapping: {}'.format(x))
print("The value of Y after swapping: {}".format(y)) ## pylint error i'm using Y 




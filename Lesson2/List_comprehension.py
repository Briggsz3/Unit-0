evens_list1= []
for i in range(1,11):
    evens_list1.append(i**2)
print(evens_list1)

# list comprehension way
evens_list2 = [i**2 for i in range(1,11)]
print(evens_list2)

# List comprehension with conditionals

# Curly braces rather than brackets
alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
# prints out green

alien_0['x-position']=0
alien_0['y-position']= 25
print(alien_0)
# adds x position and y position to it
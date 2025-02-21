# start with empty dictionary
print()
print("Modify List".center(20, "-"))
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
print(f"The aliens color is {alien_0['color']}")

alien_0['x-pos'] = 0
alien_0['y-pos'] = 25
alien_0['speed'] = 'medium'

####
# If the speed is slow, increment x_pos by 1. If medium, by 2
# If fast, by 3. Print the initial position and the new position
####


if alien_0['speed'] == 'medium':
    print(f"The initial position is {alien_0['x-pos']}, {alien_0['y-pos']}")
    alien_0['x-pos'] +=2
    print(f"The new position is {alien_0['x-pos']}, {alien_0['y-pos']}")
elif alien_0['speed'] == 'slow':
    print(f"The initial position is {alien_0['x-pos']}, {alien_0['y-pos']}")
    alien_0['x-pos'] +=1
    print(f"The new position is {alien_0['x-pos']}, {alien_0['y-pos']}")
elif alien_0['speed'] == 'fast':
    print(f"The initial position is {alien_0['x-pos']}, {alien_0['y-pos']}")
    alien_0['x-pos'] +=3
    print(f"The new position is {alien_0['x-pos']}, {alien_0['y-pos']}")
else:
    print("Invalid")

# removing key-value pairs
alien_0['home planet'] = 'Neptune'
print(alien_0)
del alien_0['home planet'] # permenatly deletes it. It deletes home planet all together
print(alien_0)

## Formatting dictionaries - one key value pair per line

alien_1{
    'color': 'blue',
    'points': 10,
    'x-pos': 50
    'y-pos': 30,
    'speed': 'fast'
}
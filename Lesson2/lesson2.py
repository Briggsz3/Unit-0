def find_average_price(price1,price2):
    return (price1+price2)/2

# exception for not printing inside functions

def min():
    price1 = float(input("What is the price? "))
    price2 = float(input("What is the next price? "))
    avg_price = find_average_price(price1,price2)
    print(avg_price)
    print(f"The average price of {price1} and {price2} is {avg_price:.2f}")

min()

def main(): 
    price = float(input("What is the price? "))
    print(round(price,2)) # if it was return it wouldn't show rounded price

main()

if __name__ == '__main__':
    main()
##########################################################

def cube_volume (length):
    return length**3

def sides():
    length = float(input("What is the length of all sides? "))
    vol = cube_volume(length)
    print(f"The volume of the cube is {vol}")

sides()

##########################################################
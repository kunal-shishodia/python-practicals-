# Program to create and print a list of cubes of even numbers up to n

def cubes_of_even_numbers(n):
    
    if n >= 2:
        
        return [x**3 for x in range(2, n+1, 2)]  
    else: 
        return("enter no greater than two")

def main():
    try:
        
        n = int(input("Enter a positive integer n: "))
        
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
            return
        
        
        result = cubes_of_even_numbers(n)
        
        
        print(f"Cubes of even numbers up to {n}: {result}")
    
    except ValueError:
        print("Invalid input! Please enter an integer.")

main()

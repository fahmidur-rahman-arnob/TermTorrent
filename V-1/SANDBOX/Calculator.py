import sys
operation = sys.argv[1]
num1 = float(sys.argv[2]) # data will come as a string ffrom cmdd.. that's why convertion to float is necessary
num2 = float(sys.argv[3])

result = 0

if operation == "add" : 
    result = num1 + num2 
elif operation == "multiply" : 
    result = num1 * num2 
else : 
    result = "Unknown Operation!"

# now printing the output

if isinstance(result, (int, float)) : 
    #if the result is whole number not float that's why for more readability I am using int
    if result.is_integer(): 
        print(f"Result is: {int(result)}")

    else : 
        print(f"Result is: {result}")

else : 
    print(result)
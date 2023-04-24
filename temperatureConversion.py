#This program converts given temperatures either to Fahrenheit to Celsius


#function for getting the temperature
def getTemp(tempType):
    
    if tempType == "f":
        temp = float(input("\nPlease enter the degrees fahrenheit to convert: "))

    elif tempType == "c":
        temp = float(input("\nPlease enter the degrees celsius to convert: "))

    return temp

#function for converting fahrenheit to Celsius
def fahr2Celsius(fahrenheit):
    result = (fahrenheit - 32) * 5/9
    return result

#function for converting  Celsius to fahrenheit
def cel2Fahrenheit(celsius):
    result2 = (9/5)* celsius + 32
    return result2

#Main function
def main():
    
    print("Temperature Conversion Calculator\n")
    print("1. Fahrenheit to Celsius ")
    print("2. Celsius to Fahrenheit ")
    print("3. Exit\n ")

    #Prompts the user to mak a choice
    choice = int(input("Enter your choice: "))

    #Loop
    while choice != 3:

        if choice == 1:
            org = getTemp("f")
            convert = fahr2Celsius(org)
            
            print(f"\n{org: .2f} degrees fahrenheit converts to approximately {convert:.2f} degrees celsius. ")

            print("\nTemperature Conversion Calculator\n")
            print("1. Fahrenheit to Celsius ")
            print("2. Celsius to Fahrenheit ")
            print("3. Exit\n ")
            
            choice = int(input("\nEnter your choice: "))
            
        if choice == 2:
            org1 = getTemp("c")
            convert1 = cel2Fahrenheit(org1)

            print(f"\n{org1:.2f} degrees celsius converts to approximately {convert1:.2f} degrees fahrenheit. ")
            
            
            print("\nTemperature Conversion Calculator\n")
            print("1. Fahrenheit to Celsius ")
            print("2. Celsius to Fahrenheit ")
            print("3. Exit\n ")
            
            choice = int(input("\nEnter your choice: "))
            
        if choice == 3:
            print("Exiting program")
            
    
#calling the main function
main()

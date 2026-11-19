def unit_converter():
    print("\n---(Unit Converter) ---")
    print("1.(Kilometers to Miles)")
    print("2.(Celsius to Fahrenheit)")
    
    choice = input("select your option (1 or 2): ")
    
    if choice == '1':
        km = float(input("kilometre entered: "))
        miles = km * 0.621371
        print(f"{km} kilometres = {miles:.2f} miles")
        
    elif choice == '2':
        celsius = float(input("temprature (Celsius) enter now: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
        
    else:
        print("wrong option selected!")

if __name__ == "__main__":
    unit_converter()

try:
    x = int(input("Enter a four digit number : "))
    y = str(x)
    if len(y)!=4:
        raise ValueError ("Wrong number of digits entered.")
    else: 
        print("Number of digit are good")
except ValueError:
     print("The length is too short/long.")
finally:
    print("End of script")

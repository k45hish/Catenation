try:
    x = int(input("Enter four digits number :"))
    y = str(x)
    if len(y)!=4:
        raise ValueError ("Worng Number of Digit")
except ValueError:
     print("The length is too short/long !!! Please provide only four digits.")
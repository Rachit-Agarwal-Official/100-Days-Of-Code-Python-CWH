# Match Case statements

x = int(input("Enter the number <= 10: "))

match x:
    case 2:
        print("This is a even and smallest prime number")
    case 3:
        print("This is a odd and the smallest odd prime number")
    case 5:
        print("This is another odd prime")
    case 7:
        print("This number is again an odd prime")
    case _ if x > 10:
        print("Your number is greater than 10")
    case _:
        print("Your number is not a prime")
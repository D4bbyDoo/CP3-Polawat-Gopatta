usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput  == "Dabby"  and passwordInput == "front":
        print("Done !")
        print("----- iShop -----")
        print("1. Vat Calculator")
        print("2. Price Calculator")
        userSelected = int(input(">>"))
        if userSelected == 1:
            price = int(input("Price (THB): "))
            vat = 7/100
            result = price + (price *vat)
            print(result)
        elif userSelected == 2 :
            price1 = int(input("First Product Price : "))
            price2 = int(input("Second Product Price : "))
            print("Total :",price1+price2)
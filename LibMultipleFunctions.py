class MultipleFunctions:
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    def OddEven():
        Num=int(input("Enter a number:"))
        if(Num%2==0):
            print("Given number is Even")
            Output="Given number is Even"
        else:
            print("Given number is Odd")
            Output="Given number is Odd"
            return Output

    def Elegible():
        Gender=input("Your Gender:")
        Age=int(input("Your age:"))
        if Gender=='Male' and Age>=21:
            print("You are eligible to get married")
        elif Gender=='Female' and Age>=18:
            print("You are eligible to get married")
        else:
            print("You are not eligible to get married")

    def percentage():
        Subject1=int(input("Subject1="))
        Subject2=int(input("Subject2="))
        Subject3=int(input("Subject3="))
        Subject4=int(input("Subject4="))
        Subject5=int(input("Subject5="))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        Percentage=(Total/5)
        print("Total: ",Total)
        print("Percentage: ",Percentage,"%")    

    def triangle():
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        Perimeter=Height1+Height2+Breadth
        print("Perimeter Formula:Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Perimeter)

        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        AreaFormula=(Height*Breadth)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",AreaFormula)
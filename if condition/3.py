UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
X=input("Enter the first city: ")
Y=input("Entet the second city: ")
if X in UAE and Y in UAE:
    print("Both cities are in UAE")
elif X in India and Y in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")
# celsius = float(input("enter your celcius number : "))
# farheneit =(celsius * 1.8)+ 32
# print(F"{celsius} Celcius is equal to {farheneit} Farheneit ")

print ("converter :")

while True:
    user_answer = input("Choose your option by typing A or B : Option A : conervert Celsius to Fahrenheit.|  " \
    "Option B : Convert Fahrenheit to Celsius : ").strip().upper()

    if user_answer not in  ("A", "B"):
        print("Enter A or B")
    else :
        break

    # fahrenheit_input= float(input("Enter your Fahrenheit value : "))


if user_answer =="A" :
    celsius_input= float(input(" Enter your celcius value : "))
    celsius_to_fahrenheit= (celsius_input * 1.8 ) + 32
    print(f"{celsius_input} ℃ Celsius is equal to {celsius_to_fahrenheit} ℉ Farhrenheit")

if user_answer=="B":
    farhrenheit_input= float(input("Enter your Farhrenheit value : "))
    farhrenheit_to_celsius= (farhrenheit_input-32)/ 1.8
    print(f"{farhrenheit_input} ℉ is equal to {farhrenheit_to_celsius} ℃ Celsius ")







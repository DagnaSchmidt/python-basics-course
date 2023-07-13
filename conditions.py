temperature = 55
forecast = "rain"

if temperature > 90:
    print("It's too hot outside")
elif temperature < 60:
    print("It's too cold outside")
else:
    print("Enjoy the weather!")

if temperature > 90 or temperature < 60:
    print("Stay inside")

if temperature < 90 and temperature > 60 and forecast != "rain":
    print("You can go out!")

raining = True
if raining:
    print("It's raining")
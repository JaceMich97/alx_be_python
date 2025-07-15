# weather_advice.py
# This program provides clothing recommendations based on weather conditions.

# prompt user for weather input
weather = input("What's the weather like today? (Sunny/rainy/cold): ").lower()

#provide clothing recommendations using if-elif-else

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("sorry, I don't have a recommendation for this weather")

# Mad libs generator with Conditionl statements
# prompt the user for inputs
adjective1 = input("Enter an adjective")
adjective2 = input("Enter another adjective")
adjective3 = input("Enter a third adjective")
adjective4 = input("Enter a final adjective")
noun = input("Enter a noun")
verb = input("Enter a verb")
place = input("Enter a place")

# Conditional touch: adjust the opening opening based on adjective1
if adjective1.lower() == "rainy":
    opening = "on a gloomy day"
else:
    opening = "on a beautiful day"

# Build the story
story = f"""
{opening} {adjective1} day, I went to the {place}. I saw a funny {adjective2} monkey
swinging from the trees. Then I spotted a majestic {adjective3} {noun} lounging in the sun.
 What a wild and {adjective4} experience.
 """
# Conditional touch: add extra lines based on the noun and the verb
if noun.lower() == "dragon":
    story += "\nsuddenly, it roared loudly and scared me !"
if verb.lower() == "run":
    story += "\nI had to run too"

# Display the final story
print("\nHere is your Mad libs story:")
print(story)    

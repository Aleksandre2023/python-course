# list of adjectives
list1 = ["Geeky", "Nerdy", "Tech-savvy", "Cyber", "Innovative", "Digital", "Caffeinated", 
         "Screaming", "Techoholic", "Gigabit", "Futuristic",
"Cloudy", "Wireless", "Pixelated", "Robotronic", "Artificial", "Viral", "Quantum", "Epic", "Databionic"]
# list of nouns
list2 = ["Banana", "Penguin", "Noodle", "Cupcake", "Bumblebee", "Pickle", "Flamingo", "Pancake", 
         "Snickerdoodle", "Cucumber",
"Wombat", "Marshmallow", "Llama", "Gummy Bear", "Muffin", "Koala",
"Panda", "Popcorn", "Jigsaw", "Raindrop"]
# additions and titles
list3 = ["Master of Memes", "Pixel Picasso", "Code Wizard", "Digital Dynamo",
"Tech Ninja", "Byte Buccaneer", "Debugging Diva", "Chief Emoji Officer", "Virtual Virtuoso", 
"Data Jedi", "Wi-Fi Whisperer", "Chief Troubleshooting Titan", "Byte-sized Comedian", 
"Pixel Puncher", "Algorithm Alchemist", "Digital Doodle Dandy", "Error Eradicator", "Byte Blaster", 
"Techie Tinkerer", "Chief of Laughter Loops"]

import random

def generate_random_nickname():
    adjective = random.choice(list1)
    noun = random.choice(list2)
    title = random.choice(list3)
    
    nickname = f"{adjective} {noun} {title}"
    return nickname

# Example usage
random_nickname = generate_random_nickname()
print("Random Nickname:", random_nickname)

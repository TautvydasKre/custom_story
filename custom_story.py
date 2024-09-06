with open("story.txt", 'r') as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

instructions = {
    "<adjective>": "Describe something using qualities like brave, funny, or gigantic.",
    "<adjective2>": "Choose a different adjective like mysterious, magical, or powerful.",
    "<adjective3>": "Choose a different adjective like mysterious, magical, or powerful.",
    "<adjective4>": "Choose a different adjective like mysterious, magical, or powerful.",
    "<verb>": "Pick an action word like run, jump, or sing.",
    "<place>": "Name a location such as a forest, castle, or desert.",
    "<animal>": "Choose an animal, for example, bear, fox, or dragon.",
    "<name>": "Think of a name, like Tom, Lily, or Max.",
    "<object>": "Select an item like a sword, book, or key.",
    "<creature>": "Pick a mythical or fictional creature like unicorn, goblin, or troll.",
    "<liquid>": "Name a liquid like water, lava, or honey.",
    "<profession>": "Choose a job or role like knight, scientist, or explorer.",
    "<magical object>": "Think of a magical item like a wand, crystal, or potion.",
    "<emotion>": "Describe a feeling like joy, sadness, or fear."
}

answers = {}

for word in words:
    instruction = instructions.get(word, f"Enter a word for {word}:")
    answer = input(f"{instruction}\nEnter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print("\nHere's your story:")
print(story)

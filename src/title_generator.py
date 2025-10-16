import random

def generate_title(moods):
    templates = [
        "Whispers of {mood}",
        "Echoes in {mood}",
        "{mood.capitalize()} Symphony",
        "Dreams of {mood}",
        "The Art of {mood}"
    ]
    mood = random.choice(moods)
    return random.choice(templates).format(mood=mood)

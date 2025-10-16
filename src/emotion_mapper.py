def color_to_mood(colors):
    # Simple mapping of color hue ranges to mood words
    moods = []
    for (r, g, b) in colors:
        if r > 180 and g < 100:
            moods.append("passion")
        elif b > 150:
            moods.append("serenity")
        elif g > 150:
            moods.append("growth")
        else:
            moods.append("mystery")
    return moods

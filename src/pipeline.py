import argparse
from color_extractor import extract_dominant_colors
from emotion_mapper import color_to_mood
from title_generator import generate_title

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Path to image file")
    args = parser.parse_args()

    colors = extract_dominant_colors(args.image)
    moods = color_to_mood(colors)
    title = generate_title(moods)

    print(f"🎨 Generated title: '{title}'")

    with open("outputs/generated_titles.txt", "a") as f:
        f.write(title + "\n")

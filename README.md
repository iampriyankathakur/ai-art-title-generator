# 🖼️ AI Art Title Generator

Upload an image and this tool generates **poetic, stylistic titles** inspired by its colors and emotional tone.


## 🚀 Features
- Extract dominant colors
- Map color palette to emotional context
- Generate poetic art titles
- Optional: integrate with AI language models for more creative outputs


## ⚙️ Installation
```bash
git clone https://github.com/yourusername/ai-art-title-generator.git
cd ai-art-title-generator
pip install -r requirements.txt
```

## ▶️ Usage
```
python src/pipeline.py --image data/sample_art.jpg
```

## Output example:
```
🎨 Generated title: “Whispers of Dusk”
```

## 📊 Tech Stack

```
Python

Image Processing: OpenCV, scikit-learn

AI Language Generation: rule-based + optional LLM (Hugging Face)

Visualization: matplotlib (for color palette)
```


---

## Requirements

```txt
opencv-python
numpy
scikit-learn
matplotlib
pytest
```

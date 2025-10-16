from src.title_generator import generate_title

def test_generate_title():
    title = generate_title(["mystery", "passion"])
    assert isinstance(title, str)
    assert len(title) > 0

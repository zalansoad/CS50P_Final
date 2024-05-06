from project import extract_word, wiki

def test_wiki():
    assert wiki("gfdsvcsrgvsdfg2435vrewf456") == "I could not find anything about it"

def test_extract_word():
    assert extract_word("hey Bob, what is a car", "Bob") == "car"

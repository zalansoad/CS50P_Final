from project import extract_word, wiki
import asyncio
import python_weather

def test_wiki():
    assert wiki("gfdsvcsrgvsdfg2435vrewf456") == "I could not find anything about it"

def test_extract_word():
    assert extract_word("hey Bob, what is a car", "Bob") == "car"


def test_getweather():
    assert int(asyncio.run(getweather("London"))) > 0 
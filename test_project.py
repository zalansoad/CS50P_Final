from project import extract_word, wiki, getweather, flip_coin
import asyncio
import python_weather

def test_wiki():
    assert wiki("gfdsvcsrgvsdfg2435vrewf456") == "I could not find anything about it"

def test_extract_word():
    assert extract_word("hey Bob, what is a car", "Bob") == "car"


def test_getweather():
    assert int(asyncio.run(getweather("London"))) > -50 

def test_flip_coin():
    assert flip_coin() == "tail" or "head"
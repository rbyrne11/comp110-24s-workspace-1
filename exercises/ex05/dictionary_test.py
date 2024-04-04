"""Unit test for dictionary function."""


__author__ = "730410363"


# invert test.

from exercises.ex05.dictionary import invert

import pytest

from exercises.ex05.dictionary import count

from exercises.ex05.dictionary import favorite_color

from exercises.ex05.dictionary import alphabetizer

from exercises.ex05.dictionary import update_attendance


def test_invert() -> None:
    """Testing invert tests' functionality."""
    test: dict[str, int] = {"r": 1, "b": 3}
    assert invert(test) == {1: "r", 3: "b"}


def test_blank_invert() -> None:
    """Empty dictionary test."""
    test: dict[str, int] = {}
    assert invert(test) == {}


def test_multiples_of_invert() -> None: 
    """Multiples should return a key error."""
    with pytest.raises(KeyError):
        test: dict[str, int] = {"r": 3, "b": 3}
        invert(test)

# invert counts.

  
def test_counts() -> None: 
    """Each dictionary item should be present no  more than once."""
    test: list[str] = ["Ryan", "Emma", "Bea"]
    assert count(test) == {"Ryan": 1, "Emma": 1, "Bea": 1}


def test_many_count() -> None:
    """Used to assess names present multiple times."""
    test: list[str] = ["Emma", "Emma", "Bea"]
    assert count(test) == {"Emma": 2, "Bea": 1}


def test_empty_count() -> None:
    """If there is an empty list, an empty dictioanry will be present."""
    test: list[str] = []
    assert count(test) == {}


# Favorite color test.
    

def test_favorite_color() -> None:
    """Assesses a list of favorite colors."""
    test: dict[str, str] = {"Ryan": "green", "Emma": "pink", "Bea": "yellow"}
    assert favorite_color(test) == "green"


def test_favorite_color_singles() -> None:
    """No duplicates in the reading, will only return the first."""
    test: dict[str, str] = {"Ryan": "green", "Emma": "pink", "Bea": "yellow"}
    assert favorite_color(test) == "green"


def test_blank_favorite_color() -> None:
    """If there is an empty list, and empty dictionary should be returned."""
    test: dict[str, str] = {}
    assert favorite_color(test) == ""

# alphabet sorting.


def test_alphabetizer() -> None:
    """Organizes lsit properly into dictionary."""
    test: list[str] = ["banana", "apple", "carrot", "grape"]
    assert alphabetizer(test) == {'a': ["apple"], 'b': ["banana"], 'c': ["carrot"], 'g': ["grape"]}
                                

def test_lowercase_alphabetizer() -> None:
    """Assesses lowercase from the alphabetizer."""
    test: list[str] = ["banana", "Apple", "carrot", "Grape"]
    assert alphabetizer(test) == {'a': ["Apple"], 'b': ["banana"], 'c': ["carrot"], 'g': ["Grape"]}


def test_alphabetizer_solo() -> None: 
    """Alphabetizer can assess a singular entry and produce proper output."""
    test: list[str] = ["banana"]
    assert alphabetizer(test) == {'b': ["banana"]}


# Assess attendance.
    
def test_adding_update_attendance() -> None:
    """Assesses updated attendance by adding a new day's information."""
    test: dict[str, list[str]] = {"Tuesday": ["Ryan", "Bea"], "Thursday": ["Ryan"]}
    update_attendance(test, "Saturday", "Ella")
    assert test == {"Tuesday": ["Ryan", "Bea"], "Thursday": ["Ryan"], "Saturday": ["Ella"]}


def test_update_attendance_by_adding_members() -> None: 
    """Adds a participant to the daily attendance as needed."""
    test: dict[str, list[str]] = {"Tuesday": ["Ryan", "Bea"], "Thursday": ["Ryan"]}
    update_attendance(test, "Tuesday", "Carly")
    assert test == {"Tuesday": ["Ryan", "Bea", "Carly"], "Thursday": ["Ryan"]}


def test_blank_update_attendance() -> None:
    """Assess the test functionality with a blank list."""
    test: dict[str, list[str]] = {}
    update_attendance(test, "Tuesday", "Ryan")
    assert test == {"Tuesday": ["Ryan"]}                                         
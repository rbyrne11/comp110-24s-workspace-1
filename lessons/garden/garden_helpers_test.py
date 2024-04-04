"""Test my garden functions."""

__author__ = "730410363"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_to_empty_kind() -> None:
    """Testing a plant being placed into an empty kind."""
    by_kind = {}
    add_by_kind(by_kind, "fruit", "plum")
    assert by_kind == {"fruit": ["plum"]}


def test_add_plant_to_kind() -> None:
    """Test for plant to be placed in exisiting kind."""
    by_kind = {"vegetable": ["carrot", "corn"], "flower": ["sunflower"]}
    add_by_kind(by_kind, "vegetable", "broccoli")
    assert by_kind == {"vegetable": ["carrot", "corn", "broccoli"], "flower": ["sunflower"]}


def test_add_to_existing_month() -> None:
    """Test for a plant to placed with an existing month."""
    by_date = {"January": ["hydrangea"], "October": ["tomato"]}
    add_by_date(by_date, "March", "tulip")
    assert by_date == {"January": ["hydrangea", "tulip"], "October": ["tomato"]}


def test_add_new_month() -> None:
    """Test for adding a plant to a new month."""
    by_date = {"January": ["hydrangea"], "October": ["tomato"]}
    add_by_date(by_date, "April", "sage")
    assert by_date == {"January": ["hydrangea"], "October": ["tomato"], "April": ["sage"]} 


def test_by_kind_and_date_when_found() -> None:
    """Test for finding plants by date when found and kind."""
    # Modified data: No flowers are planted in July
    plants_by_kind = {"vegetable": ["carrot", "corn"], "flower": ["sunflower", "hydrangea"]}
    plants_by_date = {"May": ["sunflower", "tomato"], "July": ["carrot"]}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "July")
    assert result == "No flowers will be planted in July."


def test_lookup_by_kind_and_date() -> None:
    """Test looking up plants by kind and date when plants are found."""
    plants_by_kind = {"vegetable": ["carrot", "corn"], "flower": ["sunflower", "hydrangea"]}
    plants_by_date = {"April": ["sunflower", "carrot"], "July": ["carrot"]}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "April")
    assert result == "flowers to plant in : April['sunflower']"
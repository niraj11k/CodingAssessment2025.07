import pytest
from datetime import datetime, timedelta
from codeToRefactor import PersonFactory, Person, DAYS_IN_YEAR 

def test_create_and_add_people():
    pf = PersonFactory(seed=35)
    new_people = pf.create_and_add_people(5)
    assert len(new_people) == 5
    assert all(isinstance(p, Person) for p in new_people)

def test_get_bobs_older_than_30():
    pf = PersonFactory(seed=35)
    pf.create_and_add_people(10)
    bobs_over_30 = pf._get_bobs_older_than(older_than_30=True)
    for bob in bobs_over_30:
        assert bob.name == "Bob"
        assert bob.date_of_birth <= datetime.now() - timedelta(days=30 * DAYS_IN_YEAR)

def test_get_married_name():
    p = Person(name="Bettie", date_of_birth=datetime.now())
    pf = PersonFactory()
    married_name = pf.get_married_name(p, "Parker")
    assert married_name == "Bettie Parker"


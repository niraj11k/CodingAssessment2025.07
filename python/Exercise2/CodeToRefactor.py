from datetime import datetime, timedelta
from typing import List
import random


class People:
    Under16 = datetime.now() - timedelta(days=15 * 365)
    
    def __init__(self, name: str, dob: datetime = None):
        self.name = name
        self.dob = dob or self.Under16
    
    def get_name(self) -> str:
        return self.name
    
    def get_dob(self) -> datetime:
        return self.dob


class BirthingUnit:
    def __init__(self):
        # MaxItemsToRetrieve
        self._people = []

    def get_people(self, i: int) -> List[People]:
        """
        GetPeoples
        :param j:
        :return: List[object]
        """
        for j in range(i):
            try:
                # Creates a dandon Name
                name = ""
                if random.randint(0, 1) == 0:
                    name = "Bob"
                else:
                    name = "Betty"
                # Adds new people to the list
                age_days = random.randint(18, 85) * 356
                birth_date = datetime.now() - timedelta(days=age_days)
                self._people.append(People(name, birth_date))
            except Exception as e:
                # Dont think this should ever happen
                raise Exception("Something failed in user creation")
        return self._people

    def _get_bobs(self, older_than_30: bool) -> List[People]:
        thirty_years_ago = datetime.now() - timedelta(days=30 * 356)
        if older_than_30:
            return [x for x in self._people if x.name == "Bob" and x.dob >= thirty_years_ago]
        else:
            return [x for x in self._people if x.name == "Bob"]

    def get_married(self, p: People, last_name: str) -> str:
        if "test" in last_name:
            return p.name
        if len(p.name + last_name) > 255:
            return (p.name + " " + last_name)[:255]

        return p.name + " " + last_name

import logging
from datetime import datetime, timedelta
from typing import List, Optional, Sequence
import random

from pydantic import BaseModel, Field, field_validator

# configure module-level Logger
logger =  logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(handler)

# ---- Constants ---
# [REFACTORED]Instead using numbers and name in code, defining them as a constants here
DAYS_IN_YEAR = 365
DEFAULT_AGE_YEARS = 16
MIN_AGE_YEARS = 18
MAX_AGE_YEARS = 85
MAX_FULL_NAME_LENGTH = 255
DEFAULT_NAMES = ["Bob", "Bettie"]

# [REFACTORED]: Updating People class to singular person class so that List[person] can be people and less confusing
class Person(BaseModel):
    """
    Pydantic model for a person for better validations and strict data model
    [REFACTORED] Updated class name to Person for more clarity
    """

    #Under16 = datetime.now() - timedelta(days=15 * 365)[REACFOTRED]: No need of this class attribute
    name: str = Field(..., min_length=1, description="The Person's name")
    date_of_birth: datetime = Field(default_factory=lambda: datetime.now() - timedelta(days=DEFAULT_AGE_YEARS * DAYS_IN_YEAR),
                                    description="Date of Birth; Defaults tp 16 years ago")
    def get_name(self) -> str:
        return self.name
    
    def get_dob(self) -> datetime:
        return self.dob
    
    @field_validator('name')
    def name_must_not_be_whitespace(cls, validName) -> str: #type: ignore[override]
        """Validate the name is just not a whitespace"""
        if not validName.strip():
            raise ValueError("Name cannot be empty or just whitespace")
        return validName
    
# [REFACTORED]: Updating class name from BirthingUnit to Person Factory to make it appropirate 
class PersonFactory:
    """
    Manages a collection of Person instances.
    - get_people(i) updated to create_and_add_people(i), will create a new people and return only the newly created list(non-cumulative)
    - _get_bobs(older_than_30) updated to get_bobs_older_than(older_than_30) returns Person named "Bob" optionally filtered by age > 30 years
    - get_married_name(p, lastname) returns a concatenated full name, with 'test' special-case preserved
      for backward comptablity with original logic    
    """
    def __init__(self, seed: Optional[int] = None, allowed_first_names: Optional[Sequence[str]] = None):
        """
        :param seed: Optional random seed to make generation deterministic during tests.
        :param allowed_first_name: Optional list of first names to choose from defaults to ['Bob', 'Bettie,]
        """

        self._people: List[Person] = []
        self._seed = seed
        if seed is not None:
            random.seed(seed)
            logger.debug("Random seed set to %s", seed)
        self.allowed_first_names = list(allowed_first_names) if allowed_first_names else DEFAULT_NAMES

    def create_and_add_people(self, i: int) -> List[Person]:
        """
        Generate `i` new Person objects, append them to the internal collection, and return
        the newly created list
        """
        if i < 0:
            raise ValueError("i must be non negative")
        new_people: List[Person] = []

        for _ in range(i):
            try:
                # Creates a random Name
                name = random.choice(self.allowed_first_names)
                age_years = random.randint(MIN_AGE_YEARS,MAX_AGE_YEARS)
                age_days = age_years * DAYS_IN_YEAR
                birth_date = datetime.now() - timedelta(DAYS_IN_YEAR)
                person = Person(name=name, date_of_birth=birth_date)
                self._people.append(person)
                new_people.append(person)
                logger.debug("Created person %s, dob=%s", person.name, person.date_of_birth.isoformat())
            except Exception as e:
                logger.exception("Failed to create a person: %s", {e})
                raise RuntimeError("Failed to create a person") from e
        logger.info("Created %d person (total stores: %d)", len(new_people), len(self._people) )
        return new_people
    
    #[Refactored] Updated method with more clear name
    def _get_bobs_older_than(self, older_than_30: bool) -> List[Person]:
        """
        Returns Person whose name is 'Bob'. If older_than_30 is true, return only those older than 30 years.
        """
        thirty_years_ago = datetime.now() - timedelta(days=30 * DAYS_IN_YEAR)# [Refactored] use constant for days in year
        if older_than_30:
            result = [x for x in self._people if x.name == "Bob" and x.date_of_birth <= thirty_years_ago] # [Refactored] fixed the older_than_30 logic
        else:
            result = [x for x in self._people if x.name == "Bob"]
        logger.debug("_get_bobs_older_than(older_than_30=%s) returned %d entries", older_than_30, len(result))
        return result
    
    #[Refactored] Updated the method name here to make to more clear for developers
    def get_married_name(self, p: Person, last_name: str) -> str:
        """
        Return a married name string combining p.name and last_name. Preserve the original 'test'
        """
        if "test" in last_name:
            logger.debug("get_married_name: 'test' in last_name, returning original name for %s", p.name)
            return p.name
        first = p.name.strip()
        last = last_name.strip()

        full_name = f"{first} {last}"
        if len(full_name) > 255:
            logger.debug("get_married: full name longer than 255 chars; truncating")
            return full_name[:255]
        return full_name

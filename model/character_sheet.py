from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    CheckConstraint,
    SmallInteger,
)
from sqlalchemy.orm import relationship

from database.base import Base
from model.character_sheet_skill import character_skill_association


class CharacterSheet(Base):
    __tablename__ = "character_sheets"

    id_character_sheet = Column(Integer, primary_key=True)
    # id_user = Column(Integer, ForeignKey("users.id"))  # Assuming a Users table exists
    name = Column(Text(), nullable=False)
    # clan = Column(Integer, ForeignKey("clans.id"))  # Assuming a Clans table exists
    # predator = Column(
    #     Integer, ForeignKey("predators.id")
    # )  # Assuming a Predators table exists
    strength = Column(SmallInteger, CheckConstraint("strength BETWEEN 0 AND 5"))
    dexterity = Column(SmallInteger, CheckConstraint("dexterity BETWEEN 0 AND 5"))
    stamina = Column(SmallInteger, CheckConstraint("stamina BETWEEN 0 AND 5"))
    charisma = Column(SmallInteger, CheckConstraint("charisma BETWEEN 0 AND 5"))
    manipulation = Column(SmallInteger, CheckConstraint("manipulation BETWEEN 0 AND 5"))
    composure = Column(SmallInteger, CheckConstraint("composure BETWEEN 0 AND 5"))
    intelligence = Column(SmallInteger, CheckConstraint("intelligence BETWEEN 0 AND 5"))
    wits = Column(SmallInteger, CheckConstraint("wits BETWEEN 0 AND 5"))
    resolve = Column(SmallInteger, CheckConstraint("resolve BETWEEN 0 AND 5"))
    health = Column(SmallInteger)
    health_current = Column(SmallInteger)
    willpower = Column(SmallInteger)
    willpower_current = Column(SmallInteger)
    hunger = Column(SmallInteger)
    hunger_current = Column(SmallInteger)
    humanity = Column(SmallInteger)
    humanity_current = Column(SmallInteger)
    skills = relationship(
        "Skill", secondary=character_skill_association, back_populates="characters"
    )

    def __init__(
        self,
        name,
        strength,
        dexterity,
        stamina,
        charisma,
        manipulation,
        composure,
        intelligence,
        wits,
        resolve,
        health,
        willpower,
        hunger,
        humanity,
    ):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.stamina = stamina
        self.charisma = charisma
        self.manipulation = manipulation
        self.composure = composure
        self.intelligence = intelligence
        self.wits = wits
        self.resolve = resolve
        self.health = health
        self.health_current = health
        self.willpower = willpower
        self.willpower_current = willpower
        self.hunger = hunger
        self.hunger_current = hunger
        self.humanity = humanity
        self.humanity_current = humanity

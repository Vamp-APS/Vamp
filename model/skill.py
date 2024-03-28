from database.base import Base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from model.character_sheet_skill import character_skill_association


class Skill(Base):
    __tablename__ = "skills"

    id_skill = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    category = Column(
        Enum("Physical", "Social", "Mental", name="skill_categories"), nullable=False
    )
    characters = relationship(
        "CharacterSheet", secondary=character_skill_association, back_populates="skills"
    )

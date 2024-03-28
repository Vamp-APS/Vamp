from sqlalchemy import Table, Column, Integer, ForeignKey
from database.base import Base

# Association table for a many-to-many relationship between CharacterSheet and Skill
character_skill_association = Table(
    "character_skill",
    Base.metadata,
    Column("character_id", Integer, ForeignKey("character_sheets.id_character_sheet")),
    Column("skill_id", Integer, ForeignKey("skills.id_skill")),
)

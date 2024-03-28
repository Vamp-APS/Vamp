# app.py

from flask import Flask

from database.database import Database
from model.character_sheet import CharacterSheet
from model.skill import Skill

# Create a Flask application
app = Flask(__name__)


# Define a route and view function
@app.route("/")
def index():
    return "Hello, World!"


# Run the Flask application
if __name__ == "__main__":
    db = Database("mysql://root:password@localhost:3306/vamp")

    session = db.get_session()

    if session.query(Skill).count() == 0:
        skills_data = [
            {"name": "Athletics", "category": "Physical"},
            {"name": "Brawl", "category": "Physical"},
            {"name": "Craft", "category": "Physical"},
            {"name": "Drive", "category": "Physical"},
            {"name": "Firearms", "category": "Physical"},
            {"name": "Larceny", "category": "Physical"},
            {"name": "Melee", "category": "Physical"},
            {"name": "Stealth", "category": "Physical"},
            {"name": "Survival", "category": "Physical"},
            {"name": "Animal Ken", "category": "Social"},
            {"name": "Etiquette", "category": "Social"},
            {"name": "Insight", "category": "Social"},
            {"name": "Intimidation", "category": "Social"},
            {"name": "Leadership", "category": "Social"},
            {"name": "Performance", "category": "Social"},
            {"name": "Persuasion", "category": "Social"},
            {"name": "Streetwise", "category": "Social"},
            {"name": "Subterfuge", "category": "Social"},
            {"name": "Academics", "category": "Mental"},
            {"name": "Awareness", "category": "Mental"},
            {"name": "Finance", "category": "Mental"},
            {"name": "Investigation", "category": "Mental"},
            {"name": "Medicine", "category": "Mental"},
            {"name": "Occult", "category": "Mental"},
            {"name": "Politics", "category": "Mental"},
            {"name": "Science", "category": "Mental"},
            {"name": "Technology", "category": "Mental"},
        ]
        for skill_data in skills_data:
            skill = Skill(**skill_data)
            session.add(skill)

    # Step 1: Query for a skill (assuming you want to add a skill named 'Stealth')
    skill_to_add = session.query(Skill).filter_by(name="Stealth").first()

    # Step 2: Create a new CharacterSheet instance
    if session.query(CharacterSheet).count() == 0:
        new_character_sheet = CharacterSheet(
            name="Your Character Name",
            strength=3,
            dexterity=4,
            stamina=2,
            charisma=3,
            manipulation=3,
            composure=2,
            intelligence=4,
            wits=3,
            resolve=2,
            health=7,
            willpower=5,
            hunger=1,
            humanity=7,
        )

        # Step 3: Add the queried skill to the character's skills relationship
        # This step assumes a many-to-many relationship is properly set up
        if skill_to_add:
            new_character_sheet.skills.append(skill_to_add)
        else:
            print("Skill not found.")

        # Step 4: Commit the session to save the character sheet and its relationship to the database
        session.add(new_character_sheet)
        session.commit()

    sheets = session.query(CharacterSheet).all()
    for sheet in sheets:
        print(sheet.name)
        for skill in sheet.skills:
            print(f"- {skill.name} ({skill.category})")

    session.close()

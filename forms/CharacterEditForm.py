from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from src.models.Origin import origin_list


class CharacterEditForm(FlaskForm):

    name = StringField(
        'Name',
        validators=[DataRequired()],
        )

    lvl = SelectField(
        'Level',
        validators=[DataRequired()],
        choices=list(range(1, 21))
    )

    origin = SelectField(
        'Origin',
        validators=[DataRequired()],
        choices=[origin.name for origin in origin_list]
    )

    str = SelectField(
        'Strength',
        validators=[DataRequired()],
        choices=list(range(4, 11)),
    )

    per = SelectField(
        'Perception',
        validators=[DataRequired()],
        choices=list(range(4, 11)),
    )

    end = SelectField(
        'Endurance',
        validators=[DataRequired()],
        choices=list(range(4, 11)),
    )

    cha = SelectField(
        'Charisma',
        validators=[DataRequired()],
        choices=list(range(4, 11)),
    )

    int = SelectField(
        'Intelligence',
        validators=[DataRequired()],
        choices=list(range(4, 11)),
    )

    agi = SelectField(
        'Agility',
        validators=[DataRequired()],
        choices=list(range(4, 11)),
    )

    lck = SelectField(
        'Luck',
        validators=[DataRequired()],
        choices=list(range(4, 11)),
    )

    athletics = SelectField(
        'Athletics',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_athletics = BooleanField(
        'Tagged?',
    )

    barter = SelectField(
        'Barter',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_barter = BooleanField(
        'Tagged?'
    )

    big_guns = SelectField(
        'Big Guns',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_big_guns = BooleanField(
        'Tagged?'
    )

    energy_weapons = SelectField(
        'Energy Weapons',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_energy_weapons = BooleanField(
        'Tagged?'
    )

    explosives = SelectField(
        'Explosives',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_explosives = BooleanField(
        'Tagged?'
    )

    lockpick = SelectField(
        'Lockpick',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_lockpick = BooleanField(
        'Tagged?'
    )

    medicine = SelectField(
        'Medicine',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_medicine = BooleanField(
        'Tagged?'
    )

    melee_weapons = SelectField(
        'Melee Weapons',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_melee_weapons = BooleanField(
        'Tagged?'
    )

    pilot = SelectField(
        'Pilot',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_pilot = BooleanField(
        'Tagged?'
    )

    repair = SelectField(
        'Repair',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_repair = BooleanField(
        'Tagged?'
    )

    science = SelectField(
        'Science',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_science = BooleanField(
        'Tagged?'
    )

    small_guns = SelectField(
        'Small Guns',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_small_guns = BooleanField(
        'Tagged?'
    )

    sneak = SelectField(
        'Sneak',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_sneak = BooleanField(
        'Tagged?'
    )

    speech = SelectField(
        'Speech',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_speech = BooleanField(
        'Tagged?'
    )

    survival = SelectField(
        'Survival',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_survival = BooleanField(
        'Tagged?'
    )

    throwing = SelectField(
        'Throwing',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_throwing = BooleanField(
        'Tagged?'
    )

    unarmed = SelectField(
        'Unarmed',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    tagged_unarmed = BooleanField(
        'Tagged?'
    )

    submit = SubmitField('Apply Changes')

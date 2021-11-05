from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
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

    barter = SelectField(
        'Barter',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    big_guns = SelectField(
        'Big Guns',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    energy_weapons = SelectField(
        'Energy Weapons',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    explosives = SelectField(
        'Explosives',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    lockpick = SelectField(
        'Lockpick',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    medicine = SelectField(
        'Medicine',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    melee_weapons = SelectField(
        'Melee Weapons',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    pilot = SelectField(
        'Pilot',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    repair = SelectField(
        'Repair',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    science = SelectField(
        'Science',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    small_guns = SelectField(
        'Small Guns',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    sneak = SelectField(
        'Sneak',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    speech = SelectField(
        'Speech',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    survival = SelectField(
        'Survival',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    throwing = SelectField(
        'Throwing',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    unarmed = SelectField(
        'Unarmed',
        validators=[DataRequired()],
        choices=list(range(0, 7))
    )

    submit = SubmitField('Apply Changes')

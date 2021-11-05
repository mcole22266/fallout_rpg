import os

from flask import render_template, request, redirect
from forms.CharacterEditForm import CharacterEditForm
from forms.SessionCreateForm import SessionCreateForm
from src.models.Character import Character
from src.models.Session import Session


class Routes:

    def __init__(self, app):
        self.app = app

        @app.route('/')
        def index():
            return render_template(
                'index.html',
                title='Fallout RPG Tool'
            )

        @app.route('/session/create', methods=['GET', 'POST'])
        def createSession():

            form = SessionCreateForm()

            if form.validate_on_submit():
                sessionName = request.form['sessionName']
                session = Session()
                session.sessionName = sessionName
                session.saveSession(sessionName)
                return redirect(f'/session/sheet/{session.savedID}')

            return render_template(
                'sessioncreateform.html',
                title='Create Session',
                form=form
            )

        @app.route('/session/create/<sessionName>')
        def createSessionAction(sessionName):

            session = Session()
            session.saveSession(sessionName)

            return render_template(
                'sessionsheet.html',
                title='Create Session',
                session=session
            )

        @app.route('/session/load')
        def loadSession():

            sessions = []

            for f in os.listdir('./src/data/saved_data/sessions'):
                if os.path.isfile(
                    os.path.join('./src/data/saved_data/sessions',
                                 f)):
                    sessionID = f.split('.')[0]
                    session = Session()
                    session.loadSession(sessionID)
                    sessions.append(session)

            return render_template(
                'loadsession.html',
                title='Load Session',
                sessions=sessions
            )

        @app.route('/session/delete')
        def deleteSession():

            sessions = []

            for f in os.listdir('./src/data/saved_data/sessions'):
                if os.path.isfile(
                    os.path.join('./src/data/saved_data/sessions',
                                 f)):
                    sessionID = f.split('.')[0]
                    session = Session()
                    session.loadSession(sessionID)
                    sessions.append(session)

            return render_template(
                'deletesession.html',
                title='Delete Session',
                sessions=sessions
            )

        @app.route('/session/delete/<sessionID>')
        def deleteSessionAction(sessionID):

            os.remove(f'./src/data/saved_data/sessions/{sessionID}.pkl')

            sessions = []

            for f in os.listdir('./src/data/saved_data/sessions'):
                if os.path.isfile(
                    os.path.join('./src/data/saved_data/sessions',
                                 f)):
                    sessions.append(f.split('.')[0])

            sessions.sort()

            return render_template(
                'deletesession.html',
                title='Delete Session',
                sessions=sessions
            )

        @app.route('/session/sheet/<sessionID>')
        def sessionsheet(sessionID):
            session = Session()
            session.loadSession(sessionID)

            return render_template(
                'sessionsheet.html',
                title='Session Sheet',
                session=session
            )

        @app.route('/character/create')
        def createCharacter():

            character = Character('Default Character')
            character.saveCharacter()

            sessionID = request.args.get('sessionID')
            session = Session()
            session.loadSession(sessionID)
            session.characters.append(character)
            session.saveSession(session.sessionName)

            return render_template(
                'charactersheet.html',
                title='Character Sheet',
                character=character
                )

        @app.route('/character/sheet/<characterID>')
        def charactersheet(characterID):

            character = Character(None)

            character.loadCharacter(characterID)

            return render_template(
                'charactersheet.html',
                title='Character Sheet',
                character=character
                )

        @app.route('/character/save/<characterID>')
        def charactersave(characterID):

            character = Character()

            character.loadCharacter(characterID)
            character.saveCharacter()

            return render_template(
                'charactersheet.html',
                title='Character Sheet',
                character=character
                )

        @app.route('/character/edit/<characterID>', methods=['GET', 'POST'])
        def characteredit(characterID):

            character = Character()
            character.loadCharacter(characterID)

            form = CharacterEditForm()
            if form.validate_on_submit():
                character.name = request.form['name']
                character.lvl = int(request.form['lvl'])
                character.origin = request.form['origin']
                character.strength = int(request.form['str'])
                character.perception = int(request.form['per'])
                character.endurance = int(request.form['end'])
                character.charisma = int(request.form['cha'])
                character.intelligence = int(request.form['int'])
                character.agility = int(request.form['agi'])
                character.luck = int(request.form['lck'])
                character.athletics = int(request.form['athletics'])
                character.barter = int(request.form['barter'])
                character.big_guns = int(request.form['big_guns'])
                character.energy_weapons = int(request.form['energy_weapons'])
                character.explosives = int(request.form['explosives'])
                character.lockpick = int(request.form['lockpick'])
                character.medicine = int(request.form['medicine'])
                character.melee_weapons = int(request.form['melee_weapons'])
                character.pilot = int(request.form['pilot'])
                character.repair = int(request.form['repair'])
                character.science = int(request.form['science'])
                character.small_guns = int(request.form['small_guns'])
                character.sneak = int(request.form['sneak'])
                character.speech = int(request.form['speech'])
                character.survival = int(request.form['survival'])
                character.throwing = int(request.form['throwing'])
                character.unarmed = int(request.form['unarmed'])

                character.evaluate_tagged(request.form.keys())

                character.saveCharacter()

                return redirect(f'/character/sheet/{characterID}')

            form.lvl.default = character.lvl
            form.origin.default = character.origin
            form.str.default = character.strength
            form.per.default = character.perception
            form.end.default = character.endurance
            form.cha.default = character.charisma
            form.int.default = character.intelligence
            form.agi.default = character.agility
            form.lck.default = character.luck
            form.athletics.default = character.athletics
            form.barter.default = character.barter
            form.big_guns.default = character.big_guns
            form.energy_weapons.default = character.energy_weapons
            form.explosives.default = character.explosives
            form.lockpick.default = character.lockpick
            form.medicine.default = character.medicine
            form.melee_weapons.default = character.melee_weapons
            form.pilot.default = character.pilot
            form.repair.default = character.repair
            form.science.default = character.science
            form.small_guns.default = character.small_guns
            form.sneak.default = character.sneak
            form.speech.default = character.speech
            form.survival.default = character.survival
            form.throwing.default = character.throwing
            form.unarmed.default = character.unarmed

            form.tagged_athletics.default = 'athletics' in character.tagged_skills
            form.tagged_barter.default = 'barter' in character.tagged_skills
            form.tagged_big_guns.default = 'big_guns' in character.tagged_skills
            form.tagged_energy_weapons.default = 'energy_weapons' in character.tagged_skills
            form.tagged_explosives.default = 'explosives' in character.tagged_skills
            form.tagged_lockpick.default = 'lockpick' in character.tagged_skills
            form.tagged_medicine.default = 'medicine' in character.tagged_skills
            form.tagged_melee_weapons.default = 'melee_weapons' in character.tagged_skills
            form.tagged_pilot.default = 'pilot  ' in character.tagged_skills
            form.tagged_repair.default = 'repair' in character.tagged_skills
            form.tagged_science.default = 'science' in character.tagged_skills
            form.tagged_small_guns.default = 'small_guns' in character.tagged_skills
            form.tagged_sneak.default = 'sneak  ' in character.tagged_skills
            form.tagged_speech.default = 'speech' in character.tagged_skills
            form.tagged_survival.default = 'survival' in character.tagged_skills
            form.tagged_throwing.default = 'throwing' in character.tagged_skills
            form.tagged_unarmed.default = 'unarmed' in character.tagged_skills
                                                
            form.process()

            return render_template(
                'characteredit.html',
                title=f'Character Edit - {character.name}',
                character=character,
                form=form
                )

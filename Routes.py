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
                session.saveSession(sessionName)
                return redirect(f'/session/sheet/{sessionName}')

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
                    sessions.append(f.split('.')[0])

            sessions.sort()

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
                    sessions.append(f.split('.')[0])

            sessions.sort()

            return render_template(
                'deletesession.html',
                title='Delete Session',
                sessions=sessions
            )

        @app.route('/session/delete/<sessionName>')
        def deleteSessionAction(sessionName):

            os.remove(f'./src/data/saved_data/sessions/{sessionName}.pkl')

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

        @app.route('/session/sheet/<sessionName>')
        def sessionsheet(sessionName):
            session = Session()
            session.loadSession(sessionName=sessionName)

            return render_template(
                'sessionsheet.html',
                title='Session Sheet',
                session=session
            )

        @app.route('/character/create')
        def createCharacter():

            character = Character('Test Character')
            character.saveCharacter()

            sessionName = request.args.get('sessionName')
            session = Session()
            session.loadSession(sessionName)
            session.characters.append(character)
            session.saveSession(session.sessionName)

            return render_template(
                'charactersheet.html',
                title='Character Sheet',
                character=character
                )

        @app.route('/character/sheet/<characterName>')
        def charactersheet(characterName):

            character = Character(None)

            character.loadCharacter(characterName)

            return render_template(
                'charactersheet.html',
                title='Character Sheet',
                character=character
                )

        @app.route('/character/save/<characterName>')
        def charactersave(characterName):

            character = Character()

            character.loadCharacter(characterName)
            character.saveCharacter()

            return render_template(
                'charactersheet.html',
                title='Character Sheet',
                character=character
                )

        @app.route('/character/edit/<characterName>')
        def characteredit(characterName):

            character = Character()
            character.loadCharacter(characterName)

            form = CharacterEditForm()
            if form.validate_on_submit():
                character.name = request.form['name']

                return redirect(f'/character/sheet/{characterName}')

            return render_template(
                'characteredit.html',
                title=f'Character Edit - {character.name}',
                character=character,
                form=form
                )

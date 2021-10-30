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

        @app.route('/character/edit/<characterID>')
        def characteredit(characterID):

            character = Character()
            character.loadCharacter(characterID)

            form = CharacterEditForm()
            if form.validate_on_submit():
                character.name = request.form['name']

                return redirect(f'/character/sheet/{characterID}')

            return render_template(
                'characteredit.html',
                title=f'Character Edit - {character.name}',
                character=character,
                form=form
                )

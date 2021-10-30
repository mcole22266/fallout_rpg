# Session.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# Session Model
# -----------------------------------------------

from datetime import datetime

from src.helpers.persistance import save_object, load_object
from src.models.Character import Character


class Session:

    def __init__(self):
        self.session_start = datetime.now()
        self.characters = []
        self.ap_pool = 6
        self.sessionName = None

    def loadSession(self, sessionName=None):
        if not sessionName:
            # Get name of session to load from user
            sessionName = input('Provide the Session Name to load\n> ')

        object = load_object(f'./src/data/saved_data/sessions/{sessionName}.pkl')

        # Assign current sessions attributes to match the loaded session
        self.session_start = object.session_start
        self.characters = object.characters
        self.ap_pool = object.ap_pool
        self.sessionName = sessionName

        print(f'Session {sessionName} loaded successfully')

    def saveSession(self, sessionName=None):
        if not sessionName:
            # Get name this session should be saved as
            sessionName = input('Provide the name of the Session to save\n> ')
            sessionName = f'{sessionName}'

        self.sessionName = sessionName
        save_object(self, f'./src/data/saved_data/sessions/{sessionName}.pkl')
        print(f'Session {sessionName} saved successfully')

    def createCharacter(self):
        character = Character('Test Character')
        self.characters.append(character)

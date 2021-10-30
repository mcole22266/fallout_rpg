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
        self.generateSavedSessionFilename()

    def generateSavedSessionFilename(self):
        self.saveLocation = f'./src/data/saved_data/sessions/{self.sessionName}.pkl'

    def loadSession(self, sessionName=None):
        if not sessionName:
            # Get name of session to load from user
            sessionName = input('Provide the Session Name to load\n> ')

        self.sessionName = sessionName
        self.generateSavedSessionFilename()
        object = load_object(self.saveLocation)

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
        print(self.saveLocation)
        self.generateSavedSessionFilename()
        print(self.saveLocation)
        save_object(self, self.saveLocation)
        print(f'Session {sessionName} saved successfully')

    def createCharacter(self):
        character = Character('Test Character')
        self.characters.append(character)

# Session.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# Session Model
# -----------------------------------------------

from datetime import datetime

from helpers.persistance import save_object, load_object
from models.Character import Character


class Session:

    def __init__(self):
        self.session_start = datetime.now()
        self.characters = []
        self.ap_pool = 6

    def loadSession(self):
        # Get name of session to load from user
        sessionName = input('Provide the Session Name to load\n> ')
        object = load_object(f'./data/saved_data/{sessionName}.pkl')

        # Assign current sessions attributes to match the loaded session
        self.session_start = object.session_start
        self.characters = object.characters
        self.ap_pool = object.ap_pool

        print(f'Session {sessionName} loaded successfully')

    def saveSession(self):
        # Get name this session should be saved as
        sessionName = input('Provide the name of the Session to save\n> ')
        save_object(self, f'./data/saved_data/{sessionName}.pkl')

        print(f'Session {sessionName} saved successfully')

    def createCharacter(self):
        character = Character('Test Character')
        self.characters.append(character)

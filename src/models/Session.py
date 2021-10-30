# Session.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# Session Model
# -----------------------------------------------

from datetime import datetime
from random import randint

from src.helpers.persistance import save_object, load_object
from src.models.Character import Character


class Session:

    def __init__(self):
        self.savedID = ''.join([str(randint(0, 9)) for _ in range(15)])
        self.session_start = datetime.now()
        self.characters = []
        self.ap_pool = 6
        self.sessionName = None
        self.generateSavedSessionFilename()

    def generateSavedSessionFilename(self):
        self.saveLocation = f'./src/data/saved_data/sessions/{self.savedID}.pkl'

    def loadSession(self, savedID=None):

        self.savedID = savedID
        self.generateSavedSessionFilename()
        object = load_object(self.saveLocation)

        # Assign current sessions attributes to match the loaded session
        self.session_start = object.session_start
        self.characters = object.characters
        self.ap_pool = object.ap_pool
        self.sessionName = object.sessionName

        print(f'Session {self.sessionName} loaded successfully')

    def saveSession(self, sessionName):

        self.sessionName = sessionName
        print(self.saveLocation)
        self.generateSavedSessionFilename()
        print(self.saveLocation)
        save_object(self, self.saveLocation)
        print(f'Session {self.sessionName} saved successfully')

    def createCharacter(self):
        character = Character('Test Character')
        self.characters.append(character)

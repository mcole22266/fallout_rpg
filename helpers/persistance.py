# persistance.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# Helper functions related to saving/loading data
# -----------------------------------------------

import pickle


def save_object(object, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(object, outp, pickle.HIGHEST_PROTOCOL)


def load_object(filename):
    with open(filename, 'rb') as inp:
        object = pickle.load(inp)

    return object

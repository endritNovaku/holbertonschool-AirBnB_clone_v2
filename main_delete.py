#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()
# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# Delete the new State
fs.delete(new_state)

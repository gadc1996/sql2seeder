import os

class DirectoryReader:
    def __init__(self, directory):
        self.files = os.listdir(directory)
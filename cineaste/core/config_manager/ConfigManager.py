import json
import tempfile
import errno

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.decoded = json.loads(self.config_file)

    def folder_access(self, path):
        try:
            testfile = tempfile.TemporaryFile(dir = path)
            testfile.close()
        except OSError as e:
            if e.errno == errno.EACCES:  # 13
                return False
            e.filename = path
            raise
        return True
    def Renamer(self):
        
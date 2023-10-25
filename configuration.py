from matrix import Matrix
from cryptography import Enigma


class FilesConfig(Enigma):
    pass


class SystemConfig(FilesConfig):
    pass


class WidgetsConfig(SystemConfig, Matrix):
    pass


class CommandsConfig(WidgetsConfig):
    pass

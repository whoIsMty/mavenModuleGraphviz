from abc import ABC, abstractmethod


class MavenModule(ABC):
    moduleName = ""
    moduleGroup = ""
    moduleVersion = ""

    def __init__(self, moduleName, moduleGroup, moduleVersion):
        self.moduleVersion = moduleVersion
        self.moduleName = moduleName
        self.moduleGroup = moduleGroup

    @abstractmethod
    def analyzeDepencyTree(self):
        pass

    def __str__(self):
        return f"{self.moduleGroup},{self.moduleName},{self.moduleVersion}"

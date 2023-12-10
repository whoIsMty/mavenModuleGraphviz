from abc import ABC, abstractmethod


class MavenModule(ABC):
    moduleName = ""
    moduleGroup = ""
    moduleVersion = ""

    def __init__(self, moduleName, moduleVersion=None, moduleGroup=None):
        if not moduleName:
            raise Exception(f"要初始化一个MavenModule一定要有moduleName，初始化时检查出为空。moduleName:{moduleName}")
        if moduleVersion:
            self.moduleVersion = moduleVersion
        if not moduleGroup:
            self.moduleGroup = moduleGroup
        self.moduleName = moduleName

    @abstractmethod
    def analyzeDepencyTree(self):
        pass

    def __str__(self):
        return f"{self.moduleGroup},{self.moduleName},{self.moduleVersion}"

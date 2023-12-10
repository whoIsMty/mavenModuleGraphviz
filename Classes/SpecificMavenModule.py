from Classes.MavenModule import MavenModule


class SpecificMavenModule(MavenModule):

    def analyzeDepencyTree(self):
        pass


    def __init__(self, moduleName, moduleVersion=None, moduleGroup=None):
        super().__init__(moduleName,moduleGroup=moduleGroup,moduleVersion=moduleVersion)

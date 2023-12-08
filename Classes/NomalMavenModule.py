from Classes.MavenModule import MavenModule


class NormalMavenModule(MavenModule):
    parentModule: MavenModule = None

    dependenciesModule = []

    def __init__(self, moduleName, moduleGroup, moduleVersion):
        super().__init__(moduleName, moduleGroup, moduleVersion)

    def setParentModule(self, parent: MavenModule):
        if parent:
            if self.parentModule is not None:
                raise Exception("parent已经指定。" + str(parent))
            self.parentModule = parent

    def setDependencies(self, dependency: list):
        if dependency:
            self.dependenciesModule = dependency

    def analyzeDepencyTree(self):
        pass

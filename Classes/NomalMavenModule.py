from Classes.MavenModule import MavenModule


class NormalMavenModule(MavenModule):
    parentModule = []

    dependenciesModule = []

    def __init__(self, moduleName, moduleGroup, moduleVersion):
        super().__init__(moduleName, moduleGroup, moduleVersion)

    def addParentModule(self, parent: MavenModule):
        if len(self.parentModule) == 1:
            raise Exception("parent已经指定。" + str(parent))
        self.parentModule.append(parent)

    def addDependenciesMode(self, dependency):
        self.dependenciesModule.append(dependency)

    def analyzeDepencyTree(self):
        pass

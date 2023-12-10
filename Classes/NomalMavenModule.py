from Classes.MavenModule import MavenModule


class NormalMavenModule(MavenModule):
    parentModule: MavenModule = None

    dependencies = []

    def __init__(self, moduleName, moduleGroup, moduleVersion):
        super().__init__(moduleName, moduleGroup, moduleVersion)

    def setParentModule(self, parent: MavenModule):
        if parent and self.parentModule is not None:
            raise Exception("parent已经指定。" + str(parent))
        self.parentModule = parent

    def setDependencies(self, dependencies: list):
        if dependencies:
            self.dependencies = dependencies

    def analyzeDepencyTree(self):
        pass

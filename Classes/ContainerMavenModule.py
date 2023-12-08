from abc import ABC

from MavenModule import MavenModule


class ContainerMavenModule(MavenModule, ABC):
    parentModule = None
    dependencies = []
    childModules = []

    def __init__(self, moduleName, moduleGroup, moduleVersion):
        super().__init__(moduleName, moduleGroup, moduleVersion)

    def setParentModule(self, parent: MavenModule):
        if self.parentModule is not None:
            raise Exception("parent已经指定。")
        self.parentModule = parent

    def setDependencies(self, dependencies: list):
        self.dependencies = dependencies

    def setChildModules(self, childModules: list):
        self.childModules = childModules

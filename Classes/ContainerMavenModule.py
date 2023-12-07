from abc import ABC

from MavenModule import MavenModule


class ContainerMavenModule(MavenModule, ABC):
    parentModule = []

    dependenciesModule = []

    modules = []

    def __init__(self, moduleName, moduleGroup, moduleVersion):
        super().__init__(moduleName, moduleGroup, moduleVersion)

    def addParentModule(self, parent: MavenModule):
        if len(self.parentModule) == 1:
            raise Exception("parent已经指定。")
        self.parentModule.append(parent)

    def addDependenciesMode(self, dependency):
        self.dependenciesModule.append(dependency)

    def addModuleToModules(self, module: MavenModule):
        self.modules.append(module)

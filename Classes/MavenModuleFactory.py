from Enum.ModuleTypeEnum import ModuleTypeEnum
from Classes.NomalMavenModule import NormalMavenModule
from Classes.ContainerMavenModule import ContainerMavenModule
from Utils.PomNodeParser import PomNodeParser as p


class MavenModuleFactory:

    @staticmethod
    def getModule(pomPath):
        (pomType, moduleName, moduleGroup, moduleVersion, moduleDependencies, childModules,
         parentModule) = p.analyzePomFileBaseInfoMain(
            pomPath)
        moduleType = p.getPomType(p.readPomXml(pomPath))
        if moduleType == ModuleTypeEnum.NORMAL:
            n = NormalMavenModule(moduleName, moduleGroup, moduleVersion)
            n.setDependencies(moduleDependencies)
            n.setParentModule(parentModule)
            return n
        elif moduleType == ModuleTypeEnum.CONTAINER:
            c = ContainerMavenModule(moduleName, moduleGroup, moduleVersion)
            c.setDependencies(moduleDependencies)
            c.setParentModule(parentModule)
            c.setChildModules(childModules)
            return c
        else:
            raise ValueError("Unknown type")

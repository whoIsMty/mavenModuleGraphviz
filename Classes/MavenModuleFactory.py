from Enum.ModuleTypeEnum import ModuleTypeEnum
from Classes.NomalMavenModule import NormalMavenModule
from Classes.ContainerMavenModule import ContainerMavenModule
from Utils.PomNodeParser import PomNodeParser as p


class MavenModuleFactory:

    @staticmethod
    def getModule(pomPath):
        pomType, moduleName, moduleGroup, moduleVersion, pomStr = p.analyzePomFileBaseInfoMain(pomPath)
        moduleType = p.getPomType(p.readPomXml(pomPath))
        if moduleType == ModuleTypeEnum.NORMAL:
            n = NormalMavenModule(moduleName, moduleGroup, moduleVersion)
            # 补充解析逻辑
            return n
        elif moduleType == ModuleTypeEnum.CONTAINER:
            # 补充解析逻辑
            c = ContainerMavenModule(moduleName, moduleGroup, moduleVersion)
            return c
        else:
            raise ValueError("Unknown type")

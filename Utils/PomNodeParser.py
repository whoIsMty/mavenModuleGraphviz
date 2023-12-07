from Classes.MavenModule import MavenModule
import os
from Enum.ModuleTypeEnum import ModuleTypeEnum
from Classes.MavenModuleFactory import MavenModuleFactory


class PomNodeParser:

    def __init__(self, project_path):
        self.ProjectPath = project_path

    @staticmethod
    def readPomXml(filePath):
        return open(filePath, "r", encoding="utf-8").read()

    @staticmethod
    def getPomType(pomStr):
        return ModuleTypeEnum.NORMAL

    @staticmethod
    def addDependencyOfModule(dependencyNode, module: MavenModule):
        pass

    @staticmethod
    def yieldAllPom(path):
        """
          遍历给定路径，查找所有pom.xml文件。
          """
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == 'pom.xml':
                    yield os.path.join(root, file)

    @staticmethod
    def getModuleArtifact(pomStr: str):
        return ""

    @staticmethod
    def getModuleName(pomStr: str):
        return ""

    @staticmethod
    def getModuleGroup(pomStr: str):
        return ""

    @staticmethod
    def analyzePomFileBaseInfoMain(pomPath: str):
        pomStr = PomNodeParser.readPomXml(pomPath)
        pomType = PomNodeParser.getPomType(pomStr)
        moduleName = PomNodeParser.getModuleName(pomStr)
        moduleGroup = PomNodeParser.getModuleGroup(pomStr)
        moduleVersion = PomNodeParser.getModuleArtifact(pomStr)
        return pomType, moduleName, moduleGroup, moduleVersion, pomStr

from bs4.element import PageElement, Tag

from Classes.MavenModule import MavenModule
import os
from Enum.ModuleTypeEnum import ModuleTypeEnum
from bs4 import BeautifulSoup, Comment


def transNodeToMavenModule(func, t: ModuleTypeEnum):
    def wrapper(pom):
        result = func(pom)
        new_result = []
        if type(result) == list:
            for el in result:
                if issubclass(el, Tag):
                    new_result.append(el.text)
            return new_result
        elif issubclass(pom, Tag):
            return pom.text

    return wrapper


class PomNodeParser:

    def __init__(self, project_path):
        self.ProjectPath = project_path

    @staticmethod
    def readPomXml(filePath):
        content = open(filePath, "r", encoding="utf-8").read()
        soup = BeautifulSoup(content, 'lxml-xml')  # 或者 'xml'
        # 移除所有注释
        comments = soup.find_all(text=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()
        return soup

    @staticmethod
    def getPomType(pom: BeautifulSoup):
        pomPackagingType = pom.find("packaging")
        if pomPackagingType:
            if pomPackaingType.text == "pom":
                return ModuleTypeEnum.CONTAINER
            elif pomPackaingType.text in ["jar", "war"]:
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
    def getModuleVersion(pom: BeautifulSoup):
        project = pom.find("project")
        moduleVersion = project.find_all("version", recursive=False)
        return moduleVersion if len(moduleVersion) > 0 else ''

    @staticmethod
    def getModuleName(pom: BeautifulSoup):
        project = pom.find("project")
        moduleName = project.find_all("artifactId", recursive=False)
        return moduleName if len(moduleName) > 0 else ''

    @staticmethod
    def getModuleGroup(pom: BeautifulSoup):
        project = pom.find("project")
        moduleGroup = project.find_all("groupId", recursive=False)
        return moduleGroup if len(moduleGroup) > 0 else ''

    @staticmethod
    @transNodeToMavenModule
    def getModuleDependencies(pom: BeautifulSoup):
        project = pom.find("project")
        dependencies = project.find_all("dependencies", recursive=False)
        if len(dependencies) > 0:
            ds = dependencies[0].find_all("dependency", recursive=False)
            return ds if len(ds) > 0 else None

        return []

    @staticmethod
    @transNodeToMavenModule
    def getChildModules(pom: BeautifulSoup):
        project = pom.find("project")
        modules = project.find_all("modules", recursive=False)
        if (len(modules) > 0):
            modules = modules[0].find_all("module", recursive=False)
            return modules;
        return []

    @staticmethod
    @transNodeToMavenModule
    def getParentModule(pom: BeautifulSoup):
        project = pom.find("project")
        parent = project.find("parent")
        if parent is not None:
            return parent

    @staticmethod
    def analyzePomFileBaseInfoMain(pomPath: str):
        pom = PomNodeParser.readPomXml(pomPath)
        # 模块类型
        pomType = PomNodeParser.getPomType(pom)
        # 模块信息
        moduleName = PomNodeParser.getModuleName(pom)
        moduleGroup = PomNodeParser.getModuleGroup(pom)
        moduleVersion = PomNodeParser.getModuleVersion(pom)
        # 依赖
        moduleDependencies = PomNodeParser.getModuleDependencies(pom)
        # 子模块
        childModules = PomNodeParser.getChildModules(pom)

        # 父模块
        parentModule = PomNodeParser.getParentModule(pom)
        return pomType, moduleName, moduleGroup, moduleVersion, moduleDependencies, childModules, parentModule

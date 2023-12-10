from Enum.ModuleTypeEnum import ModuleTypeEnum
from Classes.NomalMavenModule import NormalMavenModule
from Classes.ContainerMavenModule import ContainerMavenModule
from Utils.PomNodeParser import PomNodeParser as p
from Classes.MavenModule import MavenModule


class MavenModuleFactory:
    # 这个方法用来对文件pom文件进行解析。实现一个pom_file_path ->MavenModule对象的转换过程。
    @staticmethod
    def getModule(pomPath: str) -> MavenModule:
        (pomType, moduleName, moduleGroup, moduleVersion, moduleDependencies, childModules,
         parentModule) = p.analyzePomFileBaseInfoMain(
            pomPath)
        print(pomType, moduleName, moduleGroup, moduleVersion, moduleDependencies, childModules,
         parentModule)
        if pomType == ModuleTypeEnum.NORMAL:
            n = NormalMavenModule(moduleName, moduleGroup, moduleVersion)
            n.setDependencies(moduleDependencies)
            n.setParentModule(parentModule)
            return n
        elif pomType == ModuleTypeEnum.CONTAINER:
            c = ContainerMavenModule(moduleName, moduleGroup, moduleVersion)
            c.setDependencies(moduleDependencies)
            c.setParentModule(parentModule)
            c.setChildModules(childModules)
            return c
        else:
            print(pomType)
            raise ValueError("Unknown type")

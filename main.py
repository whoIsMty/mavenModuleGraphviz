from Utils.PomNodeParser import PomNodeParser
from Classes.MavenModuleFactory import MavenModuleFactory
import traceback

if __name__ == "__main__":
    ProjectPath = r"D:\Project\newdouban\back"
    maven_modules = []
    for e in PomNodeParser.yieldAllPom(ProjectPath):
        try:
            print(e)
            maven_modules.append(MavenModuleFactory.getModule(e))
        except Exception as ex:
            print(e)
            traceback.print_exc()

    print(len(maven_modules))

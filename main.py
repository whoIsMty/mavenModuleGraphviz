from Utils.PomNodeParser import PomNodeParser as p



if __name__ == "__main__":
    ProjectPath = r"E:\myproject\newdouban\back"
    for e in p.yieldAllPom(ProjectPath):
        pomType = p.getPomType(p.readPomXml(e))

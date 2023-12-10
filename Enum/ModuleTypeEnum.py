from enum import Enum


class ModuleTypeEnum(Enum):
    NORMAL = (1, "normal", "")
    CONTAINER = (2, "container", "")

    def __init__(self, index, code, remark):
        self.index = index
        self.code = code
        self.remark = remark

    def getIndex(self):
        return self.index

    def getCode(self):
        return self.code

    def getRemark(self):
        return self.remark

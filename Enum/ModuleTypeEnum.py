from enum import Enum


class ModuleTypeEnum(Enum):
    remark = None
    index = None
    code = None

    NORMAL = (1, "normal", "")
    CONTAINER = (2, "container", "")

    def __init__(self, index, code, remark):
        self.index = index
        self.code = code
        self.remark = remark

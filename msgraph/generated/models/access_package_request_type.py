from enum import Enum

class AccessPackageRequestType(str, Enum):
    NotSpecified = "notSpecified",
    UserAdd = "userAdd",
    UserExtend = "UserExtend",
    UserUpdate = "userUpdate",
    UserRemove = "userRemove",
    AdminAdd = "adminAdd",
    AdminUpdate = "adminUpdate",
    AdminRemove = "adminRemove",
    SystemAdd = "systemAdd",
    SystemUpdate = "systemUpdate",
    SystemRemove = "systemRemove",
    OnBehalfAdd = "onBehalfAdd",
    UnknownFutureValue = "unknownFutureValue",


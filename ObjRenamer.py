import maya.cmds

def check_obj_type(obj):
    if maya.cmds.objExists(obj):
        objChildren = maya.cmds.listRelatives(obj, children = True, fullPath = True) or []
        objType = ""
        if len(objChildren) == 2:
            objType = maya.cmds.objectType(objChildren[0])
        else:
            objType = maya.cmds.objectType(obj)
        return objType

def get_suffix(objType, obj, meshSuffix, jointSuffix):
    suffix = ""
    if objType == "mesh":
        suffix = meshSuffix
    elif objType == "joint":
        suffix = jointSuffix
    if len(suffix) > 0: suffix = "_" + suffix
    return suffix

def get_prefix(obj, leftPrefix, rightPrefix, centerPrefix):
    prefix = ""
    if maya.cmds.objExists(obj):
        translateX = maya.cmds.getAttr(obj + '.translateX')
        if translateX > 1:
            prefix = leftPrefix
        elif translateX < -1:
            prefix = rightPrefix
        else:
            prefix = centerPrefix
        if len(prefix) > 0: prefix = prefix + "_"
        return prefix   
  
def get_new_name(prefix, suffix, obj):
    if maya.cmds.objExists(obj):
        newName = prefix + obj + suffix
        maya.cmds.rename(obj, newName)

       
def run_renamer(meshSuffix, jointSuffix, leftPrefix, rightPrefix, centerPrefix):
    selected = maya.cmds.ls(selection = True)
    if len(selected) > 0:
        selected.reverse()
        for obj in selected:
            objType = check_obj_type(obj)
            suffix = get_suffix(objType, obj, meshSuffix, jointSuffix)
            prefix = get_prefix(obj, leftPrefix, rightPrefix, centerPrefix)  
            get_new_name(prefix, suffix, obj)
   

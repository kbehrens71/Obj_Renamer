# Obj_Renamer
This is a tool used to rename objects in a Maya scene in order to create a specific, consistent naming convention.
It adds a suffix and/or prefix based on user input that gives more specificity to what the object is.

When the UI is run, a dialogue box appears, asking the user to select the objects they would like to rename,
and to type in the labels they would like to use for different categories.

The current categories that can be labeled are:
* object type (meshes and joints)
* location on a character (left, center, and right)

The renamer will then rename all selected objects according to what the user wants labeled.
(ex: if the user chooses to label joints as "jnt", then all joints will receive a suffix of "jnt")

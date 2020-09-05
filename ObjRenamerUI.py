from PySide2 import QtWidgets, QtCore, QtGui
from shiboken2 import wrapInstance
import maya.OpenMayaUI
import ObjRenamer


def get_maya_window():
    maya_window_ptr = maya.OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(maya_window_ptr), QtWidgets.QWidget)
    
class ObjRenameDialog(QtWidgets.QDialog):
    
    def __init__(self):
        maya_main = get_maya_window()
        super(ObjRenameDialog, self).__init__(maya_main)
        
        self.setWindowTitle("Rename Objects")
        
        self.setMinimumWidth(200)
        self.setMinimumHeight(100)
        
        self.create_widgets()
        self.create_layouts()
        self.create_connections()

        
    def create_widgets(self):
        self.instructions_text = QtWidgets.QLabel()
        self.instructions_text.setAlignment(QtCore.Qt.AlignHCenter)
        self.instructions_text.setText("Select items in outliner that you want to rename")
        
        self.mesh_text = QtWidgets.QLabel()
        self.mesh_text.setText("mesh label:")
        self.mesh_input = QtWidgets.QLineEdit()
        
        self.joint_text = QtWidgets.QLabel()
        self.joint_text.setText("joint label:")
        self.joint_input = QtWidgets.QLineEdit()
        
        self.left_text = QtWidgets.QLabel()
        self.left_text.setText("left label:")
        self.left_input = QtWidgets.QLineEdit()
        
        self.center_text = QtWidgets.QLabel()
        self.center_text.setText("center label:")
        self.center_input = QtWidgets.QLineEdit()

        self.right_text = QtWidgets.QLabel()
        self.right_text.setText("right label:")
        self.right_input = QtWidgets.QLineEdit()
        
        self.run_btn = QtWidgets.QPushButton("Run")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        
        
    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        mesh_layout = QtWidgets.QHBoxLayout(self) 
        joint_layout = QtWidgets.QHBoxLayout(self) 
        left_layout = QtWidgets.QHBoxLayout(self) 
        center_layout = QtWidgets.QHBoxLayout(self)
        right_layout = QtWidgets.QHBoxLayout(self)
        btn_layout = QtWidgets.QHBoxLayout(self)
        
        mesh_layout.addWidget(self.mesh_text)
        mesh_layout.addWidget(self.mesh_input)
        joint_layout.addWidget(self.joint_text)
        joint_layout.addWidget(self.joint_input)

        left_layout.addWidget(self.left_text)
        left_layout.addWidget(self.left_input)
        center_layout.addWidget(self.center_text)
        center_layout.addWidget(self.center_input)
        right_layout.addWidget(self.right_text)
        right_layout.addWidget(self.right_input)
        
        btn_layout.addWidget(self.run_btn)
        btn_layout.addWidget(self.cancel_btn)
        
        main_layout.addSpacing(10)
        main_layout.addWidget(self.instructions_text)
        main_layout.addSpacing(10)
        main_layout.addLayout(mesh_layout)
        main_layout.addLayout(joint_layout)
        main_layout.addLayout(left_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(btn_layout)
        
    
    def create_connections(self):
        self.run_btn.clicked.connect(self.run_batch_function)
        self.cancel_btn.clicked.connect(self.close)


    def run_batch_function(self):
        print "running object renamer"
        ObjRenamer.run_renamer(self.mesh_input.text(), self.joint_input.text(), self.left_input.text(), self.right_input.text(), self.center_input.text())

try:
    ui_obj.close()
    ui_obj.deleteLater()
    
except:
    pass
    
ui_obj = ObjRenameDialog()
ui_obj.show()


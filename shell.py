import os
os.system("pyside6-designer UI/_00login.ui UI/_01test.ui UI/_02upgrade.ui UI/_03write.ui")
os.system("pyside6-uic UI/_00login.ui   -o UI/ui_00login.py")
os.system("pyside6-uic UI/_01test.ui    -o UI/ui_01test.py")
os.system("pyside6-uic UI/_02upgrade.ui -o UI/ui_02upgrade.py")
os.system("pyside6-uic UI/_03write.ui   -o UI/ui_03write.py")
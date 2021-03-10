class PyCharm:
    def execute(self):
        print("In pycharm")
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("in my editor")
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")


class Laptop():

    def code(self, ide):
        ide.execute()


ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)

ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)

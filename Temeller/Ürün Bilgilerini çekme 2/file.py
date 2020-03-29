class FileFunctions:
    def __init__(self, text):
        self.text = text
        FileFunctions.printToFile(self)

    def printToFile(self):
        file = open("amazonProduct.txt", "a")
        file.write(self.text + "\n")
        file.close()

class FileFunctions:

    def __init__(self, text):
        self.text = text
        FileFunctions.writeToFile(self)

    def writeToFile(self):
        file = open("AmazonList.txt", "a")
        file.write(self.text)
        file.close()

class Confinement:
    def __init__(self,filename:str="",chunks:int=0) -> None:
        self.fileToConfine = filename
        self.chunksToRead = chunks

    def confine(self):
        pass


    def convertTob64Chunks(self):
        with open(self.fileToConfine,"rb") as file:
            while chunk := file.read(self.chunksToRead):
                self.confine(chunk)
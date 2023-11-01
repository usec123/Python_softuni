class Song:
    def __init__(self,name:str,length:float,single:bool) -> None:
        self.name = name
        self.lenght = length
        self.single = single
    
    def get_info(self):
        return f"{self.name} - {self.lenght}"
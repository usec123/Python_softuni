class Smartphone:
    def __init__(self, memory) -> None:
        self.memory = memory
        self.apps = []
        self.is_on = False
    
    def power(self):
        self.is_on = not self.is_on
    
    def install(self,app,app_memory):
        if self.memory - app_memory >= 0:
            if self.is_on:
                self.apps.append(app)
                self.memory -= app_memory
                return f'Installing {app}'
            return f'Turn on your phone to install {app}'
        return f'Not enough memory to install {app}'
    
    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'
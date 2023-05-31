class Car:
    def __init__(self,model,make,year):
        self.model=model
        self.make=make
        self.year=year
        self.is_running=False

    def start(self):
        if not self.is_running:
            print(f"{self.model} {self.make}is starting ")
            self.is_running = True
        else:
            print(f"{self.model} {self.make}is already started")


    def stop(self):
        if self.is_running:
            print(f"{self.model}{self.make}is stoping")
            self.is_running=False
        else:
            print(f"{self.model} {self.make}is already stoped")


car1=Car("BMW", "S300 ", 2020)
car1.start()
car1.start()










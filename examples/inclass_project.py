class Bicycle:
    def exclaim(self):
        print("I'm a bicycle!! 🚲")



class Specialized(Bicycle):
    def exclaim(self):
        print("i'm a specialized bike y'all.")

    def jump(self):
        print("I'm jumping")


a_bicycle = Bicycle()

a_specialized = Specialized()
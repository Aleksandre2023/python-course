class character():
    name: None
    health_points: None

    def __init__(self, p_name):
        self.name = p_name
        self.health_points = 100


#Display
    def display():
        if self.health_points >= 50:
            print("0_0")
        elif self.health_points > 0:
            print("0_o")
        else:
            print("x_x")
        
        def damage(self, points):
            self.health_points -= points

            if self.health_points < 0:
                self.health_points = 0 
    

Geralt = character("Geralt")
# Geralt.name = "Geralt"
# Geralt.health_points = 100

Geralt.Display()
Geralt.damage(80)


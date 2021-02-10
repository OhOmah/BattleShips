

"""Short Rules 
1 Arrange your ships on Grid according to FLEET table
2 Take turns firsing a salvo at your enemy, calling out squares
    as "A3,B3", etc
Salvo = number of your ships you have left (use count)/1 shot(easy)
3 Mark salvos fired on "Enemy Ships" grid 
    "/" marks water, 
    "X" marks hit
4 Sink 'em all! (Victory Condition)
"""
class EgohBattleShipGame:

    

    def __init__(self):
        
        self.ship = {"Type" : "AircraftCarrier",
                     "MaxHits": 5,
                     "CurrentDamage": 0}

    
    def createACCarrier(self):

        return self.ship

    # a ship is a dict
    # type:
    # maxHits: 
    # currentHealth: 





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


import arcade


# SCREEN_WIDTH = 640
# SCREEN_HEIGHT = 480

class EgohBattleShipGame:

    def __init__(self):
        
        self.ship = {"Type" : "AircraftCarrier",
                     "MaxHits": 5,
                     "CurrentDamage": 0}
        self.players = []

    def addPlayer(self, name: str):

        if len(self.players) < 2:
            self.players.append(name)
        

    def createACCarrier(self):

        return self.ship

    def placeGameTile(self, gametile):

        newTileList = self.tileList.copy()
        self.tileList.append(gametile)


class GameTile:
    
    def __init__(self, column: chr, row: int): 
        self.column = column
        self.row = row






# Screen title and size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Map Screen Test"

# top/bottom/right/left margin = 5%
# tile spacing = ??
# tile size = ??


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.GRAY_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        pass




def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()







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


# Screen title and size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Map Screen Test"

GAME_TILE_WIDTH = (SCREEN_WIDTH - (SCREEN_WIDTH*.1))/11
GAME_TILE_HEIGHT = (SCREEN_HEIGHT - (SCREEN_HEIGHT*.1))/11

VERTICAL_SPACING_PERCENT = 0.010
HORIZONTAL_SPACING_PERCENT = 0.010

VERTICAL_BORDER_PERCENT = .1
HORIZONTAL_BORDER_PERCENT = .0909


class EgohBattleShipGame(arcade.Window):

    #  """ Main application class. """

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.GRAY_BLUE)

        self.ship = {"Type" : "AircraftCarrier",
                        "MaxHits": 5,
                        "CurrentDamage": 0}
        self.players = []
        self.tileList = []
        self.newTileList = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.newTileList = arcade.SpriteList()


    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()
        # test = arcade.draw_rectangle_filled(
        #     (HORIZONTAL_BORDER_PERCENT*SCREEN_WIDTH)/2  , 
        #     100, GAME_TILE_WIDTH, GAME_TILE_HEIGHT, 
        #     arcade.csscolor.AZURE)
        
        
       
        # arcade.draw_rectangle_filled(
        #     (HORIZONTAL_BORDER_PERCENT*SCREEN_WIDTH)/2 + GAME_TILE_WIDTH + SCREEN_WIDTH*HORIZONTAL_MARGIN_PERCENT , 
        #     100, GAME_TILE_WIDTH, GAME_TILE_HEIGHT, 
        #     arcade.csscolor.AZURE)
        # distance = (HORIZONTAL_BORDER_PERCENT * SCREEN_WIDTH)/2 - (HORIZONTAL_SPACING_PERCENT*SCREEN_WIDTH)/2
        
        
        self.newTileList.draw()
        # newTile = self.createGameTile("A", "3")
        # print(newTile.shape.position)
        # newTile.shape.draw()
        # newTile02 = self.createGameTile("J", "1")
        # newTile02.shape.draw()
        # newTile03 = self.createGameTile("D", "8")
        # newTile03.shape.draw()
        # columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        # rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        # tilesCreated = set()
        # for column in columns:
        #     for row in rows:
        #         if (column, row) not in tilesCreated:
        #             gameTile = self.createGameTile(column, row)
        #             self.placeGameTile(gameTile)
        #             tilesCreated.add((column, row))
        #             gameTile.shape.draw()



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

    def addPlayer(self, name: str):

        if len(self.players) < 2:
            self.players.append(name)
        

    def createACCarrier(self):

        return self.ship

    def createGameTile(self, type, column, row):

        # distance = (HORIZONTAL_BORDER_PERCENT * SCREEN_WIDTH)/2 - (HORIZONTAL_SPACING_PERCENT*SCREEN_WIDTH)/2
        gameTile = GameTile(type, column, row)
       
        return gameTile
       
    def placeGameTile(self, gametile):

        tempTileList = self.tileList.copy()
        tempTileList.append(gametile)

        self.newTileList.append(gametile.shape)

        self.tileList = tempTileList


        


xPositionDict = {"A": .05+1*.09,
                "B": .05+2*.09,
                "C": .05+3*.09,
                "D": .05+4*.09,
                "E": .05+5*.09,
                "F": .05+6*.09,
                "G": .05+7*.09,
                "H": .05+8*.09,
                "I": .05+9*.09,
                "J": .05+10*.09,
                }

yPositionDict = {"1": .05+1*.09,
                "2": .05+2*.09,
                "3" : .05+3*.09,
                "4": .05+4*.09,
                "5": .05+5*.09,
                "6": .05+6*.09,
                "7": .05+7*.09,
                "8": .05+8*.09,
                "9": .05+9*.09,
                "10": .05+10*.09,
                }

class GameTile:
    
    def __init__(self, tileType, column: chr, row: int): 

        typeDict = {
            "water": arcade.csscolor.AZURE,
            "ship" : arcade.csscolor.DIM_GREY,
            "hit" : arcade.csscolor.DARK_RED,
            "miss" : arcade.csscolor.BLACK,
            "damaged" : arcade.csscolor.DARK_ORANGE
        }
            
        self.type = tileType

        self.column = column
        self.row = row

        self.x_pos = xPositionDict[column]*SCREEN_WIDTH
        self.y_pos = yPositionDict[row]*SCREEN_HEIGHT

        self.shape = arcade.SpriteSolidColor(
            int(GAME_TILE_WIDTH), int(GAME_TILE_HEIGHT), 
            typeDict[tileType])
        self.shape.position = self.x_pos, self.y_pos
        
        



# top/bottom/right/left margin = 5%
# tile spacing = ??
# tile size = ??





def main():
    """ Main method """
    window = EgohBattleShipGame()
    window.setup()
    
    # newTile = window.createGameTile("A", "3")
    # window.newTileList.append(newTile.shape)

    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    tilesCreated = set()
    for column in columns:
        for row in rows:
            if (column, row) not in tilesCreated:
                gameTile = window.createGameTile("hit", column, row)
                window.placeGameTile(gameTile)
                tilesCreated.add((column, row))


    arcade.run()


if __name__ == "__main__":
  
    main()





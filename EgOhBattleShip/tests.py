import arcade
import gameFolder
import random

import unittest


class TestEgohBattleShip(unittest.TestCase):


    def setUp(self):
        """
        Method called to prepare the test fixture. This is called 
        immediately before calling the test method; other than AssertionError or SkipTest, 
        any exception raised by this method will be considered an error rather than a 
        test failure. The default implementation does nothing.
        """
        self.game = gameFolder.EgohBattleShipGame()
        self.game.setup()

    def testAddPlayersToGame(self):

        game = self.game

        self.game.addPlayer("Omar")
        self.game.addPlayer("Erle")

        self.assertEqual(game.players, ["Omar", "Erle"])
        self.assertEqual(len(game.players), 2)

        # A game can not have more than 2 players
        self.game.addPlayer("Tim")
        self.assertEqual(len(game.players), 2)
    
    # def testPlayerShipCount(self): # maybe I should be testing 
                                # entire player initialization

        # each player should start with 7 ships
        # 1 x Aircraft Carrier, Size 5
        # 1 x Battleship, Size 4
        # 1 x Cruiser, Size 3
        # 2 x Destroyer, Size 2
        # 2 x Submarine, Size 1


    def testCreateGameTile(self):

        # the game tile can be placed on the grid
        # according to it's x and y - A3
        game = self.game
       
        gameTile01 = game.createGameTile("ship", "A", "3")
       
        
        game.placeGameTile(gameTile01)

        # test that the tile is in the game
        self.assertIn(gameTile01, game.tileList)

        # test that the time is at the correct position
        SCREEN_WIDTH = 1024
        SCREEN_HEIGHT = 768
        self.assertTrue(gameTile01.column == "A")
        self.assertTrue(gameTile01.row == "3")

        self.assertEqual(gameTile01.shape.position, (SCREEN_WIDTH*.14, SCREEN_HEIGHT*.32))

    def testCreateWaterTile(self):
        game = self.game

        gameTile01 = game.createGameTile("water", "A", "3")
        
        
        arcade.start_render()
        gameTile01.shape.draw()
       
        print(gameTile01.shape.color)
        


        self.assertTrue(gameTile01.type == "water")
        self.assertTrue(gameTile01.shape.color == (240, 255, 255))


    def testFullGameMap(self):

        game = self.game
        # game.setup()
        columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        tilesCreated = set()
        for column in columns:
            for row in rows:
                if (column, row) not in tilesCreated:
                    gameTile = game.createGameTile("hit", column, row)
                    game.placeGameTile(gameTile)
                    tilesCreated.add((column, row))
        
        self.assertEqual(len(tilesCreated), 100)


    def testCreateAircraftCarrier(self):

        # an AC Carrier has total hits(5)
        # position on the board - extends on legal positions;
        #   not overlapping with other ships
        # remaining hits?
        game = gameFolder.EgohBattleShipGame()
        acCarrier = gameFolder.EgohBattleShipGame.createACCarrier(game)

        #test the maxhits of a Aircraft Carrier
        self.assertEqual(acCarrier["MaxHits"], 5)
        self.assertEqual(acCarrier["CurrentDamage"], 0)
        self.assertEqual(acCarrier["Type"], "AircraftCarrier")
    
        


if __name__ == "__main__":
    unittest.main()
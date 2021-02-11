import unittest
import random

import gameFolder


class TestEgohBattleShip(unittest.TestCase):


    # def testPlayerShipCount(self): # maybe I should be testing 
                                # entire player initialization

        # each player should start with 7 ships
        # 1 x Aircraft Carrier, Size 5
        # 1 x Battleship, Size 4
        # 1 x Cruiser, Size 3
        # 2 x Destroyer, Size 2
        # 2 x Submarine, Size 1
    def setUp(self):
        """
        Method called to prepare the test fixture. This is called 
        immediately before calling the test method; other than AssertionError or SkipTest, 
        any exception raised by this method will be considered an error rather than a 
        test failure. The default implementation does nothing.
        """
        self.game = gameFolder.EgohBattleShipGame()


    def testAddPlayersToGame(self):

        game = self.game

        self.game.addPlayer("Omar")
        self.game.addPlayer("Erle")

        self.assertEqual(game.players, ["Omar", "Erle"])
        self.assertEqual(len(game.players), 2)

        # A game can not have more than 2 players
        self.game.addPlayer("Tim")
        self.assertEqual(len(game.players), 2)
    
    def testPlaceGameTile(self):

        # the game tile can be placed on the grid
        # according to it's x and y - A3
        game = self.game

        gameTile01 = gameFolder.GameTile("A", 3)
        # game.placeGameTile(gameTile01)

        # test that the tile is on the board
        # self.assertIn(gameTile01, game.tileList)

        # test that the time is at the correct position
        # ??




    # def testPrimaryGridSize(self):
    #     # the map is made up of 10 x 10 squares

    #     # a square is Azure, it has a row (1-10) and column (id)
    #     game = gameFolder.EgohBattleShipGame()
    #     primaryGrid = game.player01.PrimaryGrid()


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
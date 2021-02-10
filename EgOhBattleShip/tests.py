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


    
    def testCreateAircraftCarrier(self):

        # an AC Carrier has total hits(5)
        # position on the board - extends on legal positions;
        #   not overlapping with other ships
        # remaining hits?
        acCarrier = EgohBattleShip.AircraftCarrier()
        self.assertEqual(acCarrier.totalHits, 5)
        


if __name__ == "__main__":
    unittest.main()
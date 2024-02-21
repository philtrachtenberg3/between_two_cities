import random

# Constants for the game
TILE_TYPES = ['Factory', 'Shop', 'Park', 'Monument', 'Residential']
NUM_TILES = 3  # Number of tiles each player drafts per round, simplified
BOARD_SIZE = 2  # Simplified board size (2x2 grid for each city)

class Tile:
    def __init__(self, type):
        self.type = type

class City:
    def __init__(self):
        self.grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def place_tile(self, tile, x, y):
        if self.grid[x][y] is None:
            self.grid[x][y] = tile
            return True
        return False

class Player:
    def __init__(self):
        self.city1 = City()
        self.city2 = City()

    def draft_tile(self, tiles):
        # For simplicity, automatically draft the first available tile
        return tiles.pop(0)

def create_tile_pool():
    # For simplicity, create a small, random set of tiles
    pool = [Tile(random.choice(TILE_TYPES)) for _ in range(NUM_TILES * 2)]  # 2 players * NUM_TILES
    random.shuffle(pool)
    return pool

def main():
    players = [Player() for _ in range(2)]  # Initialize players
    tile_pool = create_tile_pool()  # Create the initial pool of tiles

    # Simulate a single drafting round
    for player in players:
        for _ in range(NUM_TILES):
            tile = player.draft_tile(tile_pool)
            # For simplicity, place the tile in the first available spot in city1
            placed = False
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if player.city1.place_tile(tile, i, j):
                        placed = True
                        break
                if placed:
                    break

    # For demonstration, print out the boards
    for idx, player in enumerate(players):
        print(f"Player {idx + 1}'s City 1:")
        for row in player.city1.grid:
            print(' '.join([tile.type if tile else 'Empty' for tile in row]))

if __name__ == "__main__":
    main()

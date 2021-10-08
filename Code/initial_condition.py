"""A pattern method for adding Glider"""


def addGlider(i, j, grid):
    """Adds a glider with top left cell at (i, j)"""
    glider = np.array([
        [0, 0, 255],
        [255, 0, 255],
        [0, 255, 255]
    ])
    grid[i:i+3, j:j+3] = glider

grid = np.zeros((N, N), dtype=int)
addGlider(1, 1, grid)

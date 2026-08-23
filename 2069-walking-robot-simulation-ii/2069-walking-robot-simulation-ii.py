class Robot:

    def __init__(self, width: int, height: int):
        self.isOrigin = True
        self.index = 0

        self.path = []

        # Starting point
        self.path.append(((0, 0), "South"))

        # Bottom edge: East
        for x in range(1, width):
            self.path.append(((x, 0), "East"))

        # Right edge: North
        for y in range(1, height):
            self.path.append(((width - 1, y), "North"))

        # Top edge: West
        for x in range(width - 2, -1, -1):
            self.path.append(((x, height - 1), "West"))

        # Left edge: South
        for y in range(height - 2, 0, -1):
            self.path.append(((0, y), "South"))

    def step(self, num: int) -> None:
        self.isOrigin = False
        self.index = (self.index + num) % len(self.path)

    def getPos(self):
        return list(self.path[self.index][0])

    def getDir(self):
        if self.isOrigin:
            return "East"

        return self.path[self.index][1]
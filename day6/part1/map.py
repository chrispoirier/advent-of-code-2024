from typing import List

class map:
    def __init__(self, data):
        self.grid: List[List[chr]] = []
        self.direction = 'N'
        for i in range(len(data)):
            line = data[i]
            if '^' in line:
                self.pos = (i, line.index('^'))
            self.grid.append([c for c in line])

    def get(self, pos):
        if not self.on_map(pos):
            return None
        return self.grid[pos[0]][pos[1]]

    def on_map(self, pos=None):
        if pos is None:
            return self.pos[0] >= 0 and self.pos[0] < len(self.grid) and self.pos[1] >= 0 and self.pos[1] < len(self.grid[0])
        else:
            return pos[0] >= 0 and pos[0] < len(self.grid) and pos[1] >= 0 and pos[1] < len(self.grid[0])

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        else:
            self.direction = 'N'
    
    def traverse(self):
        visited = [self.pos]
        while True:
            # print(self.pos, self.direction, visited)
            if self.direction == 'N':
                newpos = (self.pos[0]-1, self.pos[1])
            elif self.direction == 'E':
                newpos = (self.pos[0], self.pos[1]+1)
            elif self.direction == 'S':
                newpos = (self.pos[0]+1, self.pos[1])
            elif self.direction == 'W':
                newpos = (self.pos[0], self.pos[1]-1)

            if not self.on_map(newpos):
                break
            elif self.get(newpos) == '#':
                self.turn_right()
            else:
                self.pos = newpos
                if not self.pos in visited:
                    visited.append(self.pos)

        return len(visited)
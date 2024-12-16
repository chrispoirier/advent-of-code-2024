from typing import List

class map:
    def __init__(self, data):
        self.grid: List[List[chr]] = []
        self.direction = 'N'
        for i in range(len(data)):
            line = data[i]
            if '^' in line:
                self.pos: tuple[int, int] = (i, line.index('^'))
            self.grid.append([c for c in line])

    def get(self, pos):
        if not self.on_map(pos):
            return None
        return self.grid[pos[0]][pos[1]]

    def on_map(self, pos):
        return pos[0] >= 0 and pos[0] < len(self.grid) and pos[1] >= 0 and pos[1] < len(self.grid[0])

    def turn_right(dir):
        if dir == 'N':
            newdir = 'E'
        elif dir == 'E':
            newdir = 'S'
        elif dir == 'S':
            newdir = 'W'
        else:
            newdir = 'N'
        return newdir

    def step(pos, dir):
        if dir == 'N':
            newpos = (pos[0]-1, pos[1])
        elif dir == 'E':
            newpos = (pos[0], pos[1]+1)
        elif dir == 'S':
            newpos = (pos[0]+1, pos[1])
        else:
            newpos = (pos[0], pos[1]-1)
        return newpos
    
    def traverse(self):
        visited = [self.pos]
        curpos = self.pos
        curdir = self.direction

        while True:
            newpos = map.step(curpos, curdir)

            if not self.on_map(newpos):
                break
            elif self.get(newpos) in ['#', '0']:
                curdir = map.turn_right(curdir)
            else:
                curpos = newpos
                if not curpos in visited:
                    visited.append(curpos)

        return visited
    
    def is_loop(self):
        visited = [self.pos]
        visited_cnt = [1]
        curpos = self.pos
        curdir = self.direction
        
        while True:
            newpos = map.step(curpos, curdir)

            if not self.on_map(newpos):
                break
            elif self.get(newpos) in ['#', '0']:
                curdir = map.turn_right(curdir)
            else:
                curpos = newpos
                if curpos in visited:
                    visited_cnt[visited.index(curpos)] += 1
                    if any([x > 3 for x in visited_cnt]):
                        return True
                else:
                    visited.append(curpos)
                    visited_cnt.append(1)
        return False

    def find_obstacles(self):
        visited = [self.pos]
        curpos = self.pos
        curdir = self.direction

        loop_obstacles = []
        while True:
            newpos = map.step(curpos, curdir)
            # print(newpos)

            if not self.on_map(newpos):
                break
            elif self.get(newpos) in ['#', '0']:
                curdir = map.turn_right(curdir)
            else:
                curpos = newpos
                visited.append(curpos)

            if newpos in visited:
                # print('self:')
                # self.print()
                (newmap, obs) = self.add_obstacle(curpos, curdir)
                # print('newmap:')
                # if newmap is not None:
                #     newmap.print()
                if newmap is not None and obs is not None and obs not in loop_obstacles and newmap.is_loop():
                    print('loop', obs)
                    loop_obstacles.append(obs)

        return len(loop_obstacles)
    
    def add_obstacle(self, pos, direction):
        newgrid = [''.join(row) for row in self.grid]
        pos = map.step(pos, direction)
        if self.on_map(pos) and self.get(pos) != '^':
            row = list(newgrid[pos[0]])
            row[pos[1]] = '0'
            newgrid[pos[0]] = ''.join(row)
            # print('trying:',pos)
            return (map(newgrid), pos)
        return (None, None)
    
    def print(self):
        for row in self.grid:
            print(''.join(row))
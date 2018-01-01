class Macgyver:
    def __init__(self, maze):
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.maze = maze
        
    def move(self, direction):

        if direction == "right":
            if self.case_x < 14:
                if self.maze.is_valid_case(self.case_y, self.case_x+1):
                    self.case_x += 1
                    self.x = self.case_x * 30
                
        elif direction == "left":
            if self.case_x > 0:
                if self.maze.is_valid_case(self.case_y, self.case_x-1):
                    self.case_x -= 1
                    self.x = self.case_x * 30

        elif direction == "up":
            if self.case_y > 0:
                if self.maze.is_valid_case(self.case_y-1, self.case_x):
                    self.case_y -= 1
                    self.y = self.case_y * 30

        elif direction == "down":
            if self.case_y < 14:
                if self.maze.is_valid_case(self.case_y+1, self.case_x):
                    self.case_y += 1
                    self.y = self.case_y * 30




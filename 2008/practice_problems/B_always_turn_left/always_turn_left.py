'''
Created on 15/feb/2014

@author: david

Problem B. Always Turn Left
(link: http://code.google.com/codejam/contest/32003/dashboard#s=p1)



***Limits***

1 ≤ N ≤ 100.

***Small dataset***

2 ≤ len(entrance_to_exit) ≤ 100,
2 ≤ len(exit_to_entrance) ≤ 100.

***Large dataset***

2 ≤ len(entrance_to_exit) ≤ 10000,
2 ≤ len(exit_to_entrance) ≤ 10000.

***Sample***

Input 
2
WRWWLWWLWWLWLWRRWRWWWRWWRWLW WWRRWLWLWWLWWLWWRWWRWWLW
WW WW

Output 
Case #1:
ac5
386
9c7
e43
9c5
Case #2:
3


'''
import unittest

# Can character walk (north,south,west,east) ?
ROOM_TYPE = {'1': (1,0,0,0),
              '2': (0,1,0,0),
              '3': (1,1,0,0),
              '4': (0,0,1,0),
              '5': (1,0,1,0),
              '6': (0,1,1,0),
              '7': (1,1,1,0),
              '8': (0,0,0,1),
              '9': (1,0,0,1),
              'a': (0,1,0,1),
              'b': (1,1,0,1),
              'c': (0,0,1,1),
              'd': (1,0,1,1),
              'e': (0,1,1,1),
              'f': (1,1,1,1),
              }

class Theseus(object):

    maze = {(0,0): ROOM_TYPE['1'],} # the current list of room

    def __init__(self, position = (0,0), orientation = 'S'):
        self.position = position # a couple of absolute coordinates (x,y) for the current room
        self.orientation = orientation # N=North, S=South, W=West, E=East

    def move(self, action):
        if action == 'W':
            current_room = self.walk_forward()
            self.maze[current_room] = ROOM_TYPE['1']
        elif action == 'L':
            self.turn_left()
        elif action == 'R':
            self.turn_right()

    def walk_forward(self):
        """ Walk forward into the next room.
        """
        new_position = self.position

        if self.orientation == 'N':
            new_position = (self.position[0],self.position[1]+1)
        elif self.orientation == 'S':
            new_position = (self.position[0],self.position[1]-1)
        elif self.orientation == 'W':
            new_position = (self.position[0]-1,self.position[1])
        elif self.orientation == 'E':
            new_position = (self.position[0]+1,self.position[1])

        # update Theseus position
        self.position = new_position

        return new_position

    def turn_left(self):
        """ Turn left (or counterclockwise) 90 degrees.
        """
        if self.orientation == 'N':
            self.orientation = 'W'
        elif self.orientation == 'S':
            self.orientation = 'E'
        elif self.orientation == 'W':
            self.orientation = 'S'
        elif self.orientation == 'E':
            self.orientation = 'N'

    def turn_right(self):
        """ Turn right (or clockwise) 90 degrees.
        """
        if self.orientation == 'N':
            self.orientation = 'E'
        elif self.orientation == 'S':
            self.orientation = 'W'
        elif self.orientation == 'W':
            self.orientation = 'N'
        elif self.orientation == 'E':
            self.orientation = 'S'


class AlwaysTurnLeft(object):
    
    def __init__(self, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
    
    # file I/O
    def read_word(self, file):
        return next(file).strip()
    
    def read_int(self, file, b=10):
        return int(self.read_word(file), b)
    
    def read_words(self, file, d=' '):
        return self.read_word(file).split(d)
    
    def read_ints(self, file, b=10, d=' '):
        return [int(x, b) for x in self.read_words(file, d)]
    
    def solve(self):
        
        # create I/O files
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.output_file_name, "w")
        
        # read file size
        T = self.read_int(input_file)
        
        # initialize cases to 1
        case = 1
        
        # iterate on each line
        for l in range(T):
            
            line = self.read_words(input_file)
            # get problem data
            entrance_to_exit = line[0]
            exit_to_entrance = line[1]
            
            #===================================================================
            # solve it ...
            #===================================================================
            
            output_file.write("Case #%d: %s\n" % (case, 'TBD'))
            case += 1
        
        # close I/O files
        input_file.close()
        output_file.close()


class AlwaysTurnLeftTest(unittest.TestCase):
    def setUp(self):
        self.theseus = Theseus()

    def test_theseus_init(self):
        self.assertEqual(self.theseus.orientation,'S')
        self.assertEqual(self.theseus.position,(0,0))

    def test_theseus_rotate_left(self):
        self.theseus.turn_left()
        self.assertEqual(self.theseus.position,(0,0))
        self.assertEqual(self.theseus.orientation,'E')
        self.theseus.turn_left()
        self.assertEqual(self.theseus.orientation,'N')
        self.theseus.turn_left()
        self.assertEqual(self.theseus.orientation,'W')
        self.theseus.turn_left()
        self.assertEqual(self.theseus.position,(0,0))
        self.assertEqual(self.theseus.orientation,'S')

    def test_theseus_rotate_right(self):
        self.theseus.turn_right()
        self.assertEqual(self.theseus.position,(0,0))
        self.assertEqual(self.theseus.orientation,'W')
        self.theseus.turn_right()
        self.assertEqual(self.theseus.orientation,'N')
        self.theseus.turn_right()
        self.assertEqual(self.theseus.orientation,'E')
        self.theseus.turn_right()
        self.assertEqual(self.theseus.position,(0,0))
        self.assertEqual(self.theseus.orientation,'S')

    def test_walk_forward(self):
        self.theseus.walk_forward()
        self.assertEqual(self.theseus.position,(0,-1))
        self.assertEqual(self.theseus.orientation,'S')
        self.theseus.turn_right()
        self.theseus.walk_forward()
        self.assertEqual(self.theseus.position,(-1,-1))
        self.assertEqual(self.theseus.orientation,'W')

    def test_theseus_moves(self):
        maze = {(0,0): ROOM_TYPE['1'],(0,-1): ROOM_TYPE['1'],}
        self.theseus.move('W')
        self.assertEqual(self.theseus.position,(0,-1))
        self.assertEqual(self.theseus.orientation,'S')
        self.assertEqual(self.theseus.maze, maze)
        self.theseus.move('L')
        self.assertEqual(self.theseus.position,(0,-1))
        self.assertEqual(self.theseus.orientation,'E')
        self.assertEqual(self.theseus.maze, maze)
        self.theseus.move('R')
        self.theseus.move('R')
        self.assertEqual(self.theseus.position,(0,-1))
        self.assertEqual(self.theseus.orientation,'W')
        self.assertEqual(self.theseus.maze, maze)

    def test_solve(self):
        an_sample = AlwaysTurnLeft("B-sample.in", "B-sample.out")
    #     an_sample = AlienNumbers("B-small-practice.in", "B-small-practice.out")
    #     an_sample = AlienNumbers("B-large-practice.in", "B-large-practice.out")
        an_sample.solve()


if __name__ == '__main__':
    unittest.main()

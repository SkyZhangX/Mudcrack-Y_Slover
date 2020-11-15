import numpy as np



class connect4Board():

    def __init__(self):
        self.board = None
        self.boardsize_length = 7
        self.boardsize_height = 6
        self.black = 'b'
        self.white = 'w'
        self.currentPlayer = None

    
    
    #change from ['b'，'w'] ->[1,2]
    def setStartingPlayer(self):
        if self.currentPlayer is None:
            self.currentPlayer = self.black

    

    def convertPieceInt(self,piece: str):
        pieceInt = None

        if piece == self.black:
            pieceInt = 1
        else:
            pieceInt = 2

        return pieceInt

    '''
      a b c d e f g
     _________________
   6 | 0 0 0 0 0 0 0 | 6
   5 | 0 0 0 0 0 0 0 | 5
   4 | 0 0 0 0 0 0 0 | 4
   3 | 0 0 0 0 0 0 0 | 3
   2 | 0 0 0 0 0 0 0 | 2
   1 | 0 0 0 0 0 0 0 | 1
     _________________
      a b c d e f g
    
    '''
    
    def drawBoard(self):
        self.board = np.zeros((self.boardsize_height,self.boardsize_length))
        return self.board

    def play(self):
        player = self.currentPlayer
        print("current play is ", player)
        change = False
        boardPos = 'abcdefg'
        position = input("Where to play? \n")

        if position not in boardPos:
            print("Wrong position")
            return change

        playPos = boardPos.find(position)
        if 0 not in self.board[:,playPos]:
            print("This column is full!")
            return change

        print("im here",playPos)
        for i in range(self.boardsize_height-1,-1,-1):
            print(i)
            if self.board[i,playPos]==0:
                print("yes")
                self.board[i,playPos] = self.convertPieceInt(player)
               
                change = True
                break
        
        return change

    def changePlayer(self,change):
        if change is True:
            print("test123")
            if self.currentPlayer == self.black:
                self.currentPlayer = self.white
            elif self.currentPlayer == self.white:
                self.currentPlayer = self.black

        return

    def printBoard(self):
        print(self.board)
        return
        
    



board = connect4Board()

print(board.drawBoard())
board.setStartingPlayer()
print(board.currentPlayer)
while True:
    change = board.play()
    print("change is ",change)
    board.changePlayer(change)
    board.printBoard()


        
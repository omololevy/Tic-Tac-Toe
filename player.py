
class Player:
    moves_available = [1,2,3,4,5,6,7,8,9]
    
    def show_av_moves(self):
        """This shows all the available moves before a player makes a move"""
        print(self.moves_available)   

    def move_made(self, move):
        """This eliminates the already made moves from the moves_available list"""
        Player.moves_available.remove(move) 

    def validate_move(self, move):
        """checks if a player has made a valid move"""
        if move in Player.moves_available:
            return True
        else:
            return False  
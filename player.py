
class Player:
    moves_available= [1,2,3,4,5,6,7,8,9]
    
    def show_av_moves(self):
        print(self.moves_available)   

    def move_made(self, move):
        Player.moves_available.remove(move) 

    def validate_move(self, move):
        if move in Player.moves_available:
            return True
        else:
            return False  
# clumsy way to check if solution has been reached
def winner(moves, char):
    #horizontal row 1
    if (moves[0]==char and moves[1]==char and moves[2]==char):
        return True
    #horizontal row 2
    if (moves[3]==char and moves[4]==char and moves[5]==char):
        return True
    #horizontal row 3
    if (moves[6]==char and moves[7]==char and moves[8]==char):
        return True
    #vertical 1
    if (moves[0]==char and moves[3]==char and moves[6]==char):
        return True
    #vertical 2
    if (moves[1]==char and moves[4]==char and moves[7]==char):
        return True
    #vertical 3
    if (moves[2]==char and moves[5]==char and moves[8]==char):
        return True
    #diagonal 1
    if (moves[0]==char and moves[4]==char and moves[8]==char):
        return True
    #diagonal 2
    if (moves[2]==char and moves[4]==char and moves[6]==char):
        return True
import abc
from enum import Enum

class Color(Enum):
    WHITE = 1
    BLACK = 2

class EmptySquare:
    def __init__(self):
        pass

    def __str__(self):
        return ' '

class Piece(metaclass = abc.ABCMeta):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.short_name if self.color == Color.WHITE else self.short_name.lower()

    @staticmethod
    def from_notation(piece_notation):
        if piece_notation is None:
            return EmptySquare()

        piece_class = PIECE_MAPPING[piece_notation.lower()]
        color = Color.WHITE if piece_notation.isupper() else Color.BLACK
        return piece_class(color)

class Rook(Piece):
    name = 'Rook'
    short_name = 'R'

class Knight(Piece):
    name = 'Knight'
    short_name = 'N'

class Bishop(Piece):
    name = 'Bishop'
    short_name = 'B'

class Queen(Piece):
    name = 'Queen'
    short_name = 'Q'

class King(Piece):
    name = 'King'
    short_name = 'K'

class Pawn(Piece):
    name = 'Pawn'
    short_name = 'P'

PIECE_MAPPING = {
    'r': Rook,
    'n': Knight,
    'b': Bishop,
    'q': Queen,
    'k': King,
    'p': Pawn
    }


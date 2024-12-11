class Card: 
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
             'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, rank, suit):
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        self.rank = rank
        self.suit = suit
    
    def __repr__(self) -> str:
        return f"Card(rank='{self.rank}', suit='{self.suit}')"
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
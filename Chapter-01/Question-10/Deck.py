from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = [
            Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        
    def shuffle(self) -> None:
        random.shuffle(self.cards)
        
    def __repr__(self) -> str:
        return f"Deck({len(self.cards)} cards remaining)"

    def __str__(self) -> str:
        return f"Deck with {len(self.cards)} cards"
        
    def deal(self, num: int = 1) -> list[Card]:
        if num > len(self.cards):
            raise ValueError("Not enough cards left in the deck.")
        dealt_cards = self.cards[:num]
        self.cards = self.cards[num:] # remaining
        return dealt_cards
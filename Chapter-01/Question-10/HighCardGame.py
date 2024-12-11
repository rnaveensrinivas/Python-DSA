from Deck import Deck
from Card import Card

class HighCardGame: 
    def __init__(self, num_players: int):
        if num_players < 2: 
            raise ValueError("The game requires at least 2 players.")
        
        self.num_players = num_players
        self.deck = Deck()
        self.deck.shuffle()
        # Set comprehension
        self.players = {f"Player {i+1}": None for i in range(self.num_players)}
        
    def play(self) -> None:
        print("Dealing Cards ...")
        for player in self.players:
            self.players[player] = self.deck.deal()[0]
            
        print("\nCards dealt:")
        for player, card in self.players.items():
            print(f"{player}: {card}")
            
        winner = max(self.players, 
                     key=lambda p: Card.RANKS.index(self.players[p].rank))
        print(f"\nThe winner is {winner} with {self.players[winner]}!")
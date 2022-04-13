import random

dice = ["LEFT", "RIGHT", "CENTER", "FREE", "FREE", "FREE"]

class Player:
    start_money = [1,1,1]
    def __init__(self, position) -> None:
        self.money =list(Player.start_money)
        self.position = position


def play_game(num_players) -> None:
    players = [Player(i) for i in range (num_players)]
    total_money = sum(Player.start_money) * num_players
    center_pot = 0
    num_rolls = 0
    player_count = num_players
    winner = None
    while player_count > 1:
        for player in players:
            for dollar in player.money:
                roll = random.choice(dice)
                num_rolls += 1
                if roll == "CENTER":
                    player.money.remove(dollar)
                    center_pot += dollar
                elif roll == "LEFT":
                    left_pos = (player.position - 1) % (num_players - 1)
                    left_player = players[left_pos]
                    player.money.remove(dollar)
                    left_player.money.append(dollar)
                elif roll == "RIGHT":
                    right_pos = (player.position + 1) % (num_players - 1)
                    right_player = players[right_pos]
                    player.money.remove(dollar)
                    right_player.money.append(dollar)
        
        player_count = 0
        for player in players:
            if len(player.money) > 0:
                player_count += 1
                winner = player
        

    
    print(num_rolls)
    print(winner.position)


def main():
    play_game(10)


if __name__ == "__main__":
    main()
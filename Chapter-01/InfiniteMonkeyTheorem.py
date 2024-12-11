import random
SENTENCE = "methinks it is like a weasel"
LETTERS = "abcdefghijklmnopqrstuvwxyz "
SIMULATION_STEPS = 100_000_000

def generate_random_string(random_string: str) -> str:
    ret = []
    for i in range(len(SENTENCE)):
        if random_string[i] == SENTENCE[i]: 
            ret.append(random_string[i])
        else:
            ret.append(LETTERS[random.randint(0,26)])
        
    return "".join(ret)

def score_random_string(random_string: str) -> int:
    # lower the score, the better the string.
    score = 0
    for i in range(len(SENTENCE)):
        score += abs(ord(SENTENCE[i]) - ord(random_string[i]))
    return score

def simulate(steps:int =SIMULATION_STEPS):
    best_score = float("inf")
    best_string = ""
    random_string = "*" * len(SENTENCE)
    
    print("Attempt\tBest Score\tBest String")
    for i in range(steps):
        random_string = generate_random_string(random_string)
        score = score_random_string(random_string)
        if score < best_score:
            best_score = score
            best_string = random_string
            
        print(f"%7d %10d\t{best_string}"%(i, best_score))
        if best_score == 0:
                break

simulate()
    
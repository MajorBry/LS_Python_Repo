def high_scores_in_round(rounds):
    THRESHOLD = 4
    
    return [scores for scores in rounds if all([score > THRESHOLD for score in scores])]

rounds = [[6, 8], [2, 9], [15, 11], [4, 100]]
print(high_scores_in_round(rounds) == [[6, 8], [15, 11]])

rounds = [[6, 8, 2, 7], [6, 9, 1], [15, 11], [5, 6, 7, 8, 100]]
print(high_scores_in_round(rounds) == [[15, 11], [5, 6, 7, 8, 100]])
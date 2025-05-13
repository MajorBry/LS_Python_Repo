def get_grade(score1, score2, score3):
    score = (score1 + score2 + score3) / 3
    if 90 <= score:
        return 'A'
    if 80 <= score < 90:
        return 'B'
    if 70 <= score < 80:
        return 'C'
    if 60 <= score < 70:
        return 'D'
    else:
        return 'F'
    
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

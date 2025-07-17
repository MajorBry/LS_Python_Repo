class Candidate:
    def __init__(self, name):
        self._name = name
        self._votes = 0
    pass

    @property
    def name(self):
        return self._name
    
    @property
    def votes(self):
        return self._votes

    def __add__(self, other):
        if not isinstance(other, Candidate):
            return NotImplemented
        return self._votes + other

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self._votes += other

class Election:
    def __init__(self, candidates):
        self._candidates = candidates

    def results(self):
        total_votes = 0
        winner = Candidate('')
        
        for candidate in self._candidates:
            if winner.votes < candidate.votes:
                winner = candidate
            
            total_votes += candidate.votes
            
            print(f'{candidate.name}: {candidate.votes} votes')

        print(f'{winner.name} won: {winner.votes / total_votes*100:.1f}% of votes')
        
        

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for vote in votes:
    vote += 1

election = Election(candidates)
election.results()
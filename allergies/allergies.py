class Allergies(object):
    def __init__(self, score):
        self.allergies_by_score = {
            1: 'eggs',
            2: 'peanuts',
            4: 'shellfish',
            8: 'strawberries',
            16: 'tomatoes',
            32: 'chocolate',
            64: 'pollen',
            128: 'cats',
        }
        self.score_by_allergy = {value: key for key, value in self.allergies_by_score.items()}
        self.allergies = self.get_allergies(score)

    def get_allergies(self, score):
        allergies = []
        remaining_score = score

        for the_score in sorted(self.allergies_by_score.keys(), reverse=True):
            allergy = self.allergies_by_score[the_score]
            if  remaining_score >= the_score:
                remaining_score %= the_score
                if allergy not in allergies:
                    allergies.append(allergy)
        return reversed(allergies)

    def allergic_to(self, allergy):
        return allergy in self.allergies

    @property
    def lst(self):
        return sorted(self.allergies, key=lambda allergy: self.score_by_allergy[allergy])
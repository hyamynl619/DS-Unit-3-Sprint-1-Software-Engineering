# Creating a Student Class

import random

class Student():
  def __init__(self, name, age = random.randint(18, 56), 
               precourse_scores = random.sample(range(1, 6), 5),
               passing_score = 3.5, 
               applied = 'Yes'):
    self.name = name
    self.age = age    
    self.precourse_scores = precourse_scores                            
    self.passing_score = passing_score
    self.applied = applied
    
    def results(self):
        total = sum(self.precourse_scores)
        mean = (total / len(self.precourse_scores))
        return mean

    def accepted(self):
        total = sum(self.precourse_scores)
        mean = (total / len(self.precourse_scores))
        if mean > self.passing_score:
            print('Accepted!')
        else:
            print('Not Accepted.')

    def summary(self):
        sample = Student('Name')
        print('---SUMMARY---')
        print('Applicant Name:', self.name)
        print('Applicant Age:', self.age)
        print('Precourse Scores:', self.precourse_scores)
        print('Results:', sample.results())
        print('Accepted:', sample.accepted())

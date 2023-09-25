
class Human:

    def __init__ (self, name, motion, activity, likes):
        self.name = name
        self.motion = motion
        self.activity = activity
        self.likes = likes


    def person(self):
        return '{} is {} because he likes to {}'.format(self.name,self.motion, self.activity)
    
per_1 = Human('joon', 'biking', 'stay fit', 'reading')
per_2 = Human('stephen', 'weight lifting', 'gym', 'coding')


# print(per_1.person())
# print(per_2.activity)

class Kpop:

    def __init__(self, name, category, genre, years):
        self.name = name
        self.category = category
        self.genre = genre
        self.years = years

    def artist(self):
        return '{} is a {} that focuses on {} genre with {} years in existence'.format(self.name, self.category, self.genre, self.years)


group_1 = Kpop('bangtan sonyeongdan' , 'boy band', 'hip pop/rap', '10' )
group_2 = Kpop('Blackpink' , 'girl band', 'pop', '7')

print(group_1.artist())
print(group_2.artist())



















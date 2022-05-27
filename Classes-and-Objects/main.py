class Student:
    name = str
    age = int
    tracks = list
    score = float

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name
        return name

    def change_age(self, age):
        self.age = int(age)
        return age

    def add_track(self, tracks):
        self.tracks.append(tracks)
        return tracks

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(44)
Bob.add_track("UI/UX")
Bob.get_score()

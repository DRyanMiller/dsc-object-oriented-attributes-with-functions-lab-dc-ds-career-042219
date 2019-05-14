class School():
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster
    def add_student(self, full_name, grade_level):
        if grade_level in self.roster.keys():
            self.roster[grade_level].append(full_name)
        else:
            self.roster.update({grade_level: [full_name]})
    def grade(self, grade_level):
        return self.roster[grade_level]
    def sort_roster(self):
        sort_dict = self.roster
        for key in sort_dict:
            sort_dict[key].sort()
        return sort_dict
class Album:
    def __init__(self, id, title, release_year, artist):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist = artist

    def __eq__(self,other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist})"

    # These next two methods will be used by the controller to check if
    # books are valid and if not show errors to the user.
    def is_valid(self):
        if self.title == None or self.title == "":
            return False
        if self.release_year == None or self.release_year == "":
            return False
        if self.artist == None or self.artist == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.title == None or self.title == "":
            errors.append("Title can't be blank")
        if self.release_year == None or self.release_year == "":
            errors.append("Release year can't be blank")
        if self.artist == None or self.artist == "":
            errors.append("Artist can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
class Team(object):
    
    def __init__(self, city, name):
        # todo: logo, stadium name, stadium lat/long
        self.name = name
        self.city = city
    
    @property
    
    def full_name(self):
        return f"{self.city} {self.name}"
    
    def advertise(self):
        print(f"HELLO PLEASE COME TO {self.city.upper()} TO SEE OUR GAMES!")
    
    @staticmethod
    
    def advertise_generic():
        print(f"HELLO PLEASE COME TO OUR GAMES!")


class BasketballTeam(Team):
    
    def __init__(self, city, name, center):
        super().__init__(city, name)
        self.starting_center = center

    
    def advertise(self):
        print(f"HELLO PLEASE COME TO {self.city.upper()} TO SEE OUR STARTING CENTER: {self.starting_center}!")

if __name__ == "__main__":
    
    bball_team = BasketballTeam(city="LA", name="Lakers", center="Shaq")
    print(bball_team.full_name)
    bball_team.advertise()
    print(bball_team.starting_center)
    #team = Team(city="Washington DC", name="Warriors")
    #print(team)
    #print(type(team))
    #print(dir(team))
    #print(team.name)
    #print(team.full_name)
    ##print(team.full_name())
    #team.advertise()
    #team.advertise_generic()
    #teams = [
    #    {"city": "New York", "name": "Yankees"},
    #    {"city": "New York", "name": "Mets"},
    #    {"city": "Boston", "name": "Red Sox"},
    #    {"city": "New Haven", "name": "Ravens"}
    #]
    ##for team in teams:
    ##    print("---------")
    ##    print(full_name(team))
    ##    advertise(team)
    #for d in teams:
    #    team = Team(city=d["city"], name=d["name"])
    #    print(team.full_name)
    #    team.advertise()
    #    print("----")
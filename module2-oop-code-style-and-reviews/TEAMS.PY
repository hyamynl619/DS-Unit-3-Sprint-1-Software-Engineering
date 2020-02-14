

def full_name(team):
    return f"{team['city']} {team['name']}"


def advertise(team):
    print(f"HELLO PLEASE COME TO {team['city']} TO SEE OUR GAMES!")


if __name__ == "__main__":
    teams = [
        {"city": "New York", "name": "Yankees"},
        {"city": "New York", "name": "Mets"},
        {"city": "Boston", "name": "Red Sox"},
        {"city": "New Haven", "name": "Ravens"}
    ]
    for team in teams:
        print("---------")
        print(full_name(team))
        advertise(team)

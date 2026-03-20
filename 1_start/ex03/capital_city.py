import sys

def get_capital_city():
    if len(sys.argv) != 2:
        return

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    state_name = sys.argv[1]
    if state_name in states:
        abbr = states[state_name]
        print(capital_cities[abbr])
    else:
        print("Unknown state")

if __name__ == '__main__':
    get_capital_city()

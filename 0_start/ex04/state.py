import sys

def get_state():
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

    capital_name = sys.argv[1]
    
    abbr = None
    for k, v in capital_cities.items():
        if v == capital_name:
            abbr = k
            break
    
    if abbr is None:
        print("Unknown capital city")
        return

    state_name = None
    for k, v in states.items():
        if v == abbr:
            state_name = k
            break
    
    if state_name:
        print(state_name)
    else:
        print("Unknown capital city")

if __name__ == '__main__':
    get_state()

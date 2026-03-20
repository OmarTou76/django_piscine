import sys

STATES = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
}

CAPITAL_CITIES = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def detect_and_print(expr):
    lower_expr = expr.lower()
    if not lower_expr:
        return

    for state, abbr in STATES.items(): # "Oregon" : "OR" 
        if lower_expr == state.lower():
            capital = CAPITAL_CITIES[abbr]
            print(f"{capital} is the capital of {state}")
            return

    for abbr, capital in CAPITAL_CITIES.items():
        if lower_expr == capital.lower():
            for state, a in STATES.items():
                if a == abbr:
                    print(f"{capital} is the capital of {state}")
                    return

    print(f"{expr} is neither a capital city nor a state")
    

def all_in():
    if len(sys.argv) != 2:
        return

    expressions = sys.argv[1].split(',')
    
    for expr in expressions:
        detect_and_print(expr.strip())

if __name__ == '__main__':
    all_in()

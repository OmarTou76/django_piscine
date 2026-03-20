def sort_by_year(item: tuple[str, str]) -> int:
    return int(item[1])

def sort_musicians() -> None:
    d: dict[str, str] = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
    }

    musicians = list(d.items())

    # Alphabetical sort by name
    musicians.sort()
    
    # Year sort by birth year
    musicians.sort(key=sort_by_year)

    for name, _ in musicians:
        print(name)

if __name__ == '__main__':
    sort_musicians()

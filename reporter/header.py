import datetime
import warnings

def create_header(authors, city="Paris"):
    """Returns the header string
    
    This function creates a header string with place, 
    today's date and the nams of the authors.
    
    Parameters
    ----------
    Authors : list of dictionnaries
    Each list should have at least the keys
    'firs' and 'last'
    City : Str, optional default 'Paris'
    """    
    
    today=datetime.date.today().strftime('%d/%m/%Y')
    txt = []
    txt.append(f"{city}, le {today} /n")
    txt.append(f"### auteurs: /n")
    for elem in authors:
        first = elem.get("first", "XX")
        last = elem.get("last", "XX")
        txt.append(f"- {first} {last} ")
    return "/n".join(txt)

def _validate(author):
    has_first = "first" in author
    has_last = "last" in author
    return has_first and has_last

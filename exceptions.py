
def convert(s):
    try:
        x = int(s)
        
    except (ValueError,TypeError):
        print("Something went wrong")
        
    return x

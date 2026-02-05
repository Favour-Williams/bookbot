def countWord(text):
    string = text.split()
    count = len(string)
    return count


def countChar(text):
    chars={}
    for char in text:
        low = char.lower()
        if low in chars:
            chars[low] += 1
        else:
            chars[low] = 1
    return chars
def sort_on(dict):
    return dict["num"]

def sort(char_dict): 
    sorted_dict = []
    for char, val in char_dict.items():
        sorted_dict.append({"char": char, "num": val})
    sorted_dict.sort(key=sort_on, reverse=True)
    return sorted_dict

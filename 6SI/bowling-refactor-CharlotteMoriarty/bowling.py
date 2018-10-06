def score(game):
    result = 0
    frame = 1
    in_first_half = True
    
    for i in range(len(game)):
        if use_slash(game[i]):
            result += 10 - last_result
        else:
            result += get_value(game[i]) 
            
#### scoop
        if frame < 10  and get_value(game[i]) == 10:
            if use_slash(game[i]):
                result += get_value(game[i+1])
            
            if for_what_i_need_xx(game[i]): 
                result += get_value(game[i+1])
            
                if use_slash(game[i+2]): 
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last_result = get_value(game[i])
####  scoop
        if not in_first_half: 
           frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if for_what_i_need_xx(game[i]):
            in_first_half = True
            frame += 1
    return result

#nowe funkcje
def use_slash(frame):
    return frame == "/"
def for_what_i_need_xx(frame):
    return frame in "Xx"    
#chyba juz
def get_value(char):
    
    if char in '123456789':
        return int(char)
    elif for_what_i_need_xx(char) or use_slash(char):
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
    
        

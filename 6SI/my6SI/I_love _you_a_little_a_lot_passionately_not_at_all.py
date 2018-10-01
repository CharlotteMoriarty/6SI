def how_much_i_love_you(nb_petals):
    # your code
    love = ["I love you","a little","a lot","passionately", "madly","not at all"]
    #return love [nb_petals % len(love) -1]
    if nb_petals %6 == 1:
        return love[0]
    elif nb_petals %6== 2:
        return love[1]
    elif nb_petals %6 ==3:
        return love[2]
    elif nb_petals %6 ==4:
        return love[3]
    elif nb_petals %6 == 5:
        return love[4]
    else:
        return love[-1]
    #elif nb_petals %6 == 6:
     #   return love[5] 


def calculate_love_score(name1, name2):
    str_holder = name1+name2
    print(str_holder)
    #Counting for TRUE
    count_t=0
    for letter in str_holder:
        if "t" == letter:
            count_t += 1
    if count_t==1:
        print(f"T occurs {count_t} time")
    else:
        print(f"T occurs {count_t} times")

    count_r = 0
    for letter in str_holder:
        if "r" == letter:
            count_r += 1
    if count_r==1:
        print(f"R occurs {count_r} time")
    else:
        print(f"R occurs {count_r} times")

    count_u = 0
    for letter in str_holder:
        if "u" == letter:
            count_u += 1
    if count_u == 1:
        print(f"U occurs {count_u} time")
    else:
        print(f"U occurs {count_u} times")

    count_e = 0
    for letter in str_holder:
        if "e" == letter:
            count_e += 1
    if count_e ==1:
        print(f"E occurs {count_e} time")
    else:
        print(f"E occurs {count_e} times")

    count_true= count_t+count_r+count_u+count_e
    print(f"Total = {count_true}")

    # Counting for Love

    count_love_l = 0
    for letter in str_holder:
        if "l" == letter:
            count_love_l += 1
    if count_love_l==1:
        print(f"L occurs {count_love_l} time")
    else:
        print(f"L occurs {count_love_l} times")



    count_love_o = 0
    for letter in str_holder:
        if "0" == letter:
            count_love_o += 1
    if count_love_o == 1:
        print(f"O occurs {count_love_o} time")
    else:
        print(f"O occurs {count_love_o} times")

    count_love_v = 0
    for letter in str_holder:
        if "v" == letter:
            count_love_v += 1
    if count_love_v ==1:
        print(f"V occurs {count_love_v} time")
    else:
        print(f"V occurs {count_love_v} times")

    count_love_e = 0
    for letter in str_holder:
        if "e" == letter:
            count_love_e += 1
    if count_love_e ==1:
        print(f"E occurs {count_love_e} time")
    else:
        print(f"E occurs {count_love_e} times")


    count_love = count_love_l + count_love_o + count_love_v + count_love_e
    print(f"Total = {count_love}")


    love_score = str(count_true+ count_love)
    print(f"Love Score = {count_true}{count_love}")



calculate_love_score("Kanye West", "Kim Kardashian")

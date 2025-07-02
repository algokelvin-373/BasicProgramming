def calculate_love_score(name1, name2):
    keyword1 = 'TRUE'.lower()
    keyword2 = 'LOVE'.lower()

    result1 = 0
    result2 = 0

    for letter in keyword1:
        for key_name in name1:
            if letter == key_name:
                result1 += 1
        for key_name in name2:
            if letter == key_name:
                result1 += 1

    for letter in keyword2:
        for key_name in name1:
            if letter == key_name:
                result2 += 1
        for key_name in name2:
            if letter == key_name:
                result2 += 1

    combine = str(result1) + str(result2)
    print(combine)


calculate_love_score('Angela Yu', 'Jack Bauer')
calculate_love_score("Kanye West", "Kim Kardashian")
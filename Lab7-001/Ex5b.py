celebrities_tuple = ("Taylor Swift", "Lionel Messi", "Max Verstappen", "Keanu Reeves", "Angelina Jolie")
ages_tuple = (34, 36, 26, 59, 48)

celeb_list = [item for item in celebrities_tuple]
ages_list = [age for age in ages_tuple]

celebrities_dict = {
    "celebrities": celeb_list,
    "ages": ages_list
}
print(celebrities_dict)
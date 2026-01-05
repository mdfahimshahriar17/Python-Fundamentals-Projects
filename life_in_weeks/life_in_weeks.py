def life_in_weeks(age):
    life = 70
    weeks_remining = (life - age)*52
    return weeks_remining

print(f"You have {life_in_weeks(25)} weeks left ...")
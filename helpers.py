import random
from russian_names import RussianNames


class InfoAboutPerson:
    first_name = RussianNames().get_person().split()[0]
    last_name = RussianNames().get_person().split()[2]
    random_phone_number = f"+7{random.randint(900, 999)}{random.randint(100, 999)}{random.randint(1001, 9999)}"
    colors = ['grey', 'black']
    random_day = f"{random.randint(10,28)}"
    random_color = f"{random.choice(colors)}"
    random_period = f"{random.randint(1,7)}"
    current_street_name = ['Ленина', 'Калинина', 'Гражданска', 'Комсомольская', 'Независимости']
    street = random.choice(current_street_name)
    house = random.randint(1, 20)
    flat = random.randint(1, 100)
    adress = f"Москва, {street}, {house}, {flat}"

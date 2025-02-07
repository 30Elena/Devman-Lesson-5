from faker import Faker
import file_operations
import random
import os

PATH = 'charsheet/'

LETTERS_MAPPING = {
    'а': 'а͠', 
    'б': 'б̋', 
    'в': 'в͒͠',
    'г': 'г͒͠', 
    'д': 'д̋', 
    'е': 'е͠',
    'ё': 'ё͒͠', 
    'ж': 'ж͒', 
    'з': 'з̋̋͠',
    'и': 'и', 
    'й': 'й͒͠', 
    'к': 'к̋̋',
    'л': 'л̋͠', 
    'м': 'м͒͠', 
    'н': 'н͒',
    'о': 'о̋', 
    'п': 'п̋͠', 
    'р': 'р̋͠',
    'с': 'с͒', 
    'т': 'т͒', 
    'у': 'у͒͠',
    'ф': 'ф̋̋͠', 
    'х': 'х͒͠', 
    'ц': 'ц̋',
    'ч': 'ч̋͠', 
    'ш': 'ш͒͠', 
    'щ': 'щ̋',
    'ъ': 'ъ̋͠', 
    'ы': 'ы̋͠', 
    'ь': 'ь̋',
    'э': 'э͒͠͠', 
    'ю': 'ю̋͠', 
    'я': 'я̋',
    'А': 'А͠', 
    'Б': 'Б̋', 
    'В': 'В͒͠',
    'Г': 'Г͒͠', 
    'Д': 'Д̋', 
    'Е': 'Е',
    'Ё': 'Ё͒͠', 
    'Ж': 'Ж͒', 
    'З': 'З̋̋͠',
    'И': 'И', 
    'Й': 'Й͒͠', 
    'К': 'К̋̋',
    'Л': 'Л̋͠', 
    'М': 'М͒͠', 
    'Н': 'Н͒',
    'О': 'О̋', 
    'П': 'П̋͠', 
    'Р': 'Р̋͠',
    'С': 'С͒', 
    'Т': 'Т͒', 
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 
    'Х': 'Х͒͠', 
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 
    'Ш': 'Ш͒͠', 
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 
    'Ы': 'Ы̋͠', 
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 
    'Ю': 'Ю̋͠', 
    'Я': 'Я̋',
    ' ': ' ',
}

SKILLS = [
    "Стремительный прыжок", 
    "Электрический выстрел",
    "Ледяной удар", 
    "Стремительный удар", 
    "Кислотный взгляд",
    "Тайный побег", 
    "Ледяной выстрел", 
    "Огненный заряд",
]

FAKE = Faker("ru_RU")

def main():

os.makedirs(PATH, exist_ok=True)

    for person in range(0, 10):
        skills_not_repeat = random.sample(SKILLS, 3)
        runic_skills = []

        for index in range(0, len(skills_not_repeat)):
            for letter, rune_letter in LETTERS_MAPPING.items():
                skills_not_repeat[index] = skills_not_repeat[index].replace(
                    letter, rune_letter)
            runic_skills.append(skills_not_repeat[index])

        context = {
            "first_name": FAKE.first_name(),
            "last_name": FAKE.last_name(),
            "job": FAKE.job(),
            "town": FAKE.city(),
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": skills_not_repeat[0],
            "skill_2": skills_not_repeat[1],
            "skill_3": skills_not_repeat[2],
        }

        file_operations.render_template("charsheet.svg", "{}{} {}.svg".format(
            PATH, context['first_name'], context['last_name']), context)


if __name__ == '__main__':  
    main()

import random
from datetime import datetime, timedelta

categories_news = {
    "1": ("Tehnoloogia", ["Suuremad muudatused: eesti keele tasemeeksamid proovivad uut formaati", 
    "Nutikell suures plaanis: Apple valmistab ette kokkupandavat randmevahendit", 
    "Tallinn eraldab 145 000 eurot Saksamaale suunatud ekspordi ja nutikate linnalahenduste toetamiseks"]),
    "2": ("Spordiuudised", ["Londoni maraton: püstitati uus naiste maailmarekord", 
    "Eesti Võimlemisliit kinnitas rahvuskoondise kodustele Euroopa meistrivõistlustele võimlemises", 
    "Eesti jäähokikoondis laupäeval algavaks MM-il on selgunud"]),
    "3": ("Majandus", ["Statistikaamet plaanib muudatusi inflatsiooni arvutamise metoodikas", 
    "Tööandja: välistöötajad tõstavad kõigi Eesti elanike palka", 
    "Eesti elanikud nimetavad peamise murekohana elukalliduse tõusu"])
}


def random_date():
    days_ago = random.randint(0, 6)
    date = datetime.now() - timedelta(days=days_ago)
    return date.strftime("%Y-%m-%d")


def random_news(category_key):
    category = categories_news[category_key]
    news_item = random.choice(category[1])
    date = random_date()
    news = f"[{category[0]}] ({date}): {news_item}"
    return news


def add_news(category_key):
    user_news = input("Sisestage oma uudislugu: ")
    categories_news[category_key][1].append(user_news)
    print("Uudis lisatud.")


def menu():
    print("\nValige kategooria:")
    for key, value in categories_news.items():
        print(f"{key}. {value[0]}")
    print("0. Väljund")


def main():
    while True:
        menu()
        choice = input("Sisestage kategooria number: ")

        if choice == "0":
            print("Hüvasti!")
            break

        if choice not in categories_news:
            print("Vale valik. Proovige uuesti.")
            continue
            
        print(random_news(choice))

        add_more = input("Kas soovite lisada oma uudise? (jah/ei): ").lower()
        if add_more == "jah":
            add_news(choice)

        again = input("Kas soovite luua veel ühe uudise? (jah/ei): ").lower()
        if again != "jah":
            print("Hüvasti!")
            break


if __name__ == "__main__":
    main()

from bs4 import BeautifulSoup as soup
import requests
import csv

ciconias = requests.get("https://ciconia.fandom.com/wiki/Category:Characters")
ciconiasoup = soup(ciconias.text, "html.parser")
charcons = ciconiasoup.findAll("div", {"class": "category-page__member-left"})


with open("ciconias.csv", mode="w", encoding="utf-8") as ciconia_chars:
    fieldnames = ["Name", "Special Abilities"]
    writer = csv.DictWriter(ciconia_chars, fieldnames=fieldnames)
    writer.writeheader()
    for char in charcons:
        character = char.a['title']
        writer.writerow({'Name': character})
        specialspage = requests.get(f"https://ciconia.fandom.com{char.a['href']}")
        specialsoup = soup(specialspage.text, "html.parser")
        specials = specialsoup.findAll("b")
        for ability in specials:
            if character.strip() != ability.text.strip() and "(" in ability.text:
                writer.writerow({'Special Abilities': ability.text})


print(ciconia_chars)

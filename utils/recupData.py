#!/usr/bin/env python3
import requests
from typing import List
import utils.models as models
from tortoise import Tortoise
from bs4 import BeautifulSoup


from nicegui import ui


async def init_db() -> None:
    await Tortoise.init(
        db_url="sqlite://db.sqlite3", modules={"models": ["utils.models"]}
    )
    counter = await models.CounterForWebsiteTrafic.get_or_none(id=1)
    if counter is not None:
        counter.counter += 1
        await counter.save()
    else:
        counter = models.CounterForWebsiteTrafic(counter=1)
        await counter.save()
    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()


@ui.refreshable
async def refresh_CounterForWebsiteTrafic():
    counter: models.CounterForWebsiteTrafic = (
        await models.CounterForWebsiteTrafic.get_or_none(id=1)
    )
    if counter is not 0:
        await counter.save()
        return counter.counter
    else:
        return 0


async def refresh_CounterFoProjectsNumber():
    """Web scrapping sur github pour récupérer le nombre de projets réalisés"""
    url = "https://github.com/ffillouxdev"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            projects_count = soup.find("span", class_="Counter").text.strip()
            print("Projects count:", projects_count)
            return int(projects_count)
        else:
            print("Failed to fetch GitHub profile page:", response.status_code)
    except Exception as e:
        print("An error occurred while scraping GitHub:", str(e))
    return 0


import requests
from bs4 import BeautifulSoup

async def recup_CounterOfCommits():
    """Web scraping sur GitHub pour récupérer le nombre de commits réalisés"""
    pass
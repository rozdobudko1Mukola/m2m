from playwright.sync_api import Page
from pages.e2e.database import ObjectsPage
import random


class ObjectsPage:

    def __init__(self, page: Page):
        self.page = page
        self.objects = ObjectsPage(page)
        self.page.goto("/units")


        self
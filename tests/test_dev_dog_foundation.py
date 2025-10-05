from enum import Enum

import pytest
from playwright.sync_api import expect

from src.pages.dog_page import DogPage
from src.pages.footer import Footer
from src.pages.main_page import MainPage
from src.pages.side_menu import SideMenu


class PersonalDetails(Enum):
    NAME = "Moran Liv"
    EMAIL = "moran.liv2006@gmail.com"


class DogNames(Enum):
    KIKA = "Kika"
    LYCHEE = "Lychee"
    KIMBA = "Kimba"


@pytest.fixture
def items_array():
    return []


@pytest.mark.usefixtures("setup_browser")
class TestDevDogFoundation:
    @pytest.fixture(autouse=True)
    def setup_main(self, setup_browser, items_array):
        self.page = setup_browser

        self.main_page = MainPage(self.page)
        self.side_menu = SideMenu(self.page)
        self.dog_page = DogPage(self.page)
        self.footer = Footer(self.page)

        self.opening(items_array)
        yield

    def opening(self, items_array): # these are the shared steps among all the test cases.
        self.main_page.btn_hamburger.click()
        for value in self.side_menu.list_menu_items.all_inner_texts():  # get all the menu items text
            items_array.append(value)  # save the menu items text in the array

        assert len(items_array) == 4
        self.side_menu.list_menu_items.nth(0).click()  # clicks on the home button
        items_array.pop(0)  # because it's not a dog name, im popping it out from the array

    def fill_personal_details(self, dog_name: str):
        self.footer.input_name.fill(PersonalDetails.NAME.value)
        self.footer.input_email.fill(PersonalDetails.EMAIL.value)
        self.footer.input_message.fill(f"Hello! My name is Moran Liv and I'm interested in adopting {dog_name}.")

    def verify_the_dog_name_exist_in_the_tiles_and_clicks(self, dog_name: str, items_array):
        for value in items_array:
            assert value.upper() in self.main_page.list_tiles.all_inner_texts(), f"{value} not found in tiles"

        for value in self.main_page.list_tiles.all():
            if value.inner_text() == dog_name.upper():
                value.click()
                break
        expect(self.dog_page.txt_title).to_have_text(dog_name)

    def verify_dog_name_is_in_items_array_and_tiles_fill_details_and_send(self, dog_name: str, items_array):
        assert dog_name in items_array, f"{dog_name} not found in menu items"

        self.verify_the_dog_name_exist_in_the_tiles_and_clicks(dog_name, items_array)
        self.fill_personal_details(dog_name)
        self.footer.btn_send.click()

    def test_kika(self, items_array):
        dog_name = DogNames.KIKA.value
        self.verify_dog_name_is_in_items_array_and_tiles_fill_details_and_send(dog_name, items_array)

    def test_lychee(self, items_array):
        dog_name = DogNames.LYCHEE.value
        self.verify_dog_name_is_in_items_array_and_tiles_fill_details_and_send(dog_name, items_array)


    def test_kimba(self, items_array):
        dog_name = DogNames.KIMBA.value
        self.verify_dog_name_is_in_items_array_and_tiles_fill_details_and_send(dog_name, items_array)


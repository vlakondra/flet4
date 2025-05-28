import flet as ft
from ui import UserInterface

def main(page: ft.Page):
    ui =UserInterface(page)
    ui.mainpage.add(ft.Text('qwerty1'))




ft.app(main)
import flet as ft
from peewee import *
from playhouse.reflection import Introspector

from topmenu import TopMenu

class UserInterface:
    def __init__(self,page):
        #фиксируем ссылку на основную страницу
        self.mainpage:ft.Page = page

        #создаем главное меню
        topmenu = TopMenu(self.onmenu_click)
        #и размещаем его на странице
        self.mainpage.add(ft.Row([topmenu]))

        #добавляем file_picker на страницу и делаем его невидимым
        self.file_picker = ft.FilePicker(on_result=self.onfile_open)
        self.mainpage.overlay.append(self.file_picker)
 
        self.mainpage.update()

    def onmenu_click(self,e):
        #открываем диалог выбора файла
        if e.control.content.value == 'Открыть файл':
            self.file_picker.pick_files(allow_multiple=False)

    def onfile_open(self,e: ft.FilePickerResultEvent):
        # print(e.files[0].path)
        #получаем модели таблиц выбранной БД
        odb = SqliteDatabase(e.files[0].path)
        introspector = Introspector.from_database(odb)
        models = introspector.generate_models()
        print(models)
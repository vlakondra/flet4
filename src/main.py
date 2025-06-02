import flet as ft

# Ссылка на файл-диалог
files = ft.Ref[ft.FilePicker()]()

from controls.topmenu import TopMenu
from controls.drawer import Drawer
from database.db import SQLiteDB

# Обработчик клика по пункту меню
def onMenuClick(e):
    if e.control.content.value == "Открыть файл":
        print("FILE", e.control, e.control.data)
        files.current.pick_files(allow_multiple=False)


# Обработик выбора файла
def onFileOpen(e):
    e.page.data=e.files[0].path #сохраним путь к БД для дальнейшего использования

    # проверить путь к файлу!!!
    sqlite = SQLiteDB(e.files[0].path)

    # Получим список таблиц
    table_names = sqlite.get_tables()
    sqlite.close()

    # Сформируем Drawer, содержащий список таблиц
    # в обработчик клика по Drawer передаем список таблиц
    dr = Drawer(table_names, lambda e, tbl=table_names: onDrawerClick(e, tbl))
    e.page.drawer = dr
    e.page.update()
    e.page.open(dr)

#Открытие drawer'a спец.кнопкой
def fab_pressed(e):
    drw = e.page.drawer
    if drw:
        e.page.open(drw)


# Функция для создания строки таблицы
# def create_row(df,index, row, bg_color):
def create_row(df, row):
        return ft.Container(
            ft.Row(
                controls=[
                    ft.Container(
                        ft.Text(str(row[col]), 
                                overflow=ft.TextOverflow.VISIBLE,
                                no_wrap=False),
                        width=100,
                        padding=5,
                        expand=True
                    ) for col in df.columns],
                # vertical_alignment=ft.CrossAxisAlignment.START
            ),
            # bgcolor=bg_color,
            # padding=ft.padding.symmetric(vertical=5),
            # border=ft.border.only(
            #     bottom=ft.border.BorderSide(1, ft.Colors.GREY_300)
            # )
        )


# Обработчик клика по Drawer
def onDrawerClick(e, tbl):
    sqlite = SQLiteDB(e.page.data)
    tname = tbl[e.control.selected_index]
    # получим DF выбранной таблицы
    tdf = sqlite.get_table(tname)
    sqlite.close()


    # Создаем заголовок таблицы
    header = ft.Container(
        ft.Row(
            controls=[
                ft.Container(
                    ft.Text(col, 
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_GREY_700),
                    width=100,
                    padding=5,
                    expand=True
                ) for col in tdf.columns
            ]
        ),
        bgcolor=ft.Colors.BLUE_GREY_50,
        # padding=ft.padding.symmetric(vertical=10),
        border=ft.border.all(1, ft.Colors.GREY_300)
    )

    # Создаем список элементов данных
    rows = []
    # for index, row in tdf.iterrows():
    for index, row in tdf.iterrows():    
        rows.append(
            create_row(
                tdf,
                # index,
                row
                # bg_color=ft.Colors.WHITE if index % 2 == 0 else ft.Colors.GREY_50,
            )
        )
    #Удаляем загруженные ранее данные
    if len(e.page.controls) == 2:
        e.page.controls.pop(1)
        
    # Собираем интерфейс
    e.page.add(
        ft.Column(
            controls=[
                ft.Text(f'Таблица {tname}', 
                       size=20,
                       weight=ft.FontWeight.BOLD),
                header,
                ft.Container(
                    ft.ListView(
                        controls=rows,
                        expand=True,
                        spacing=0,
                        padding=0
                    ),
                    height=400,
                    border=ft.border.all(1, ft.Colors.GREY_300))
            ],
            spacing=1
        )
    )

    #Закроем drawer
    drw = e.page.drawer
    if drw:
        drw.open = False
    e.page.update()    
  

#################-MAIN-##################
def main(page: ft.Page):
    page.title = "SQLite viewer"

    # Добавим верхнее меню
    tp = TopMenu(on_click=onMenuClick)
    page.add(ft.Row([tp]))

    # Добавим диалог выбора файла
    file_picker = ft.FilePicker(ref=files, on_result=onFileOpen)
    page.overlay.append(file_picker)
    page.update()


    # Добавим кнопку открытия drawer'a
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.CONTENT_PASTE_GO, on_click=fab_pressed, bgcolor=ft.Colors.LIME_300
    )

ft.app(main)

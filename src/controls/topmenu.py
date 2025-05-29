import flet as ft


class TopMenu(ft.MenuBar):
    def __init__(self, on_click):
        super().__init__(
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("File"),
                    # on_open=on_click,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Открыть файл"),
                            data=1,
                            leading=ft.Icon(ft.Icons.INFO),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                            ),
                            on_click=on_click,
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Сохранить данные"),
                            data=2,
                            leading=ft.Icon(ft.Icons.SAVE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                            ),
                            on_click=on_click,
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Выйти"),
                            data=3,
                            leading=ft.Icon(ft.Icons.CLOSE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                            ),
                            on_click=on_click,
                        ),
                    ],
                )
            ]
        )
        self.expand=True
        self.style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.Colors.RED_100,
            mouse_cursor={
                ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
            },
        )

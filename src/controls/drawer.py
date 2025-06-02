import flet as ft


class Drawer(ft.NavigationDrawer):
    def __init__(self, data, on_click):
        super().__init__(
            on_change=on_click,
            controls=[
                ft.NavigationDrawerDestination(
                    label=tbl,
                    data=tbl,
                    icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
                )
                for tbl in data
            ],

        )
        

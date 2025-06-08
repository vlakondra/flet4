import flet as ft

def main(page: ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    t = ft.Text(value="Hello, World!", text_align=ft.TextAlign.RIGHT)
    c =ft.Container(t,width=150,height=150)
    c.bgcolor=ft.Colors.GREEN_200
    c.alignment=ft.alignment.center

    c.shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.Colors.BLUE_GREY_300,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    )

    page.add(c)
ft.app(target=main)    
import flet as ft

def main(page: ft.Page):
    page.title = "Счётчик нажатий"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    count = 0
    text_hello = ft.Text("Нажато: 0 раз", size=30)

    def on_button_click(e):
        nonlocal count
        count += 1
        text_hello.value = f"Нажато: {count} 
        page.update()
    btn = ft.ElevatedButton("Нажми на меня", on_click=on_button_click)
    page.add(text_hello, btn)

ft.app(target=main)

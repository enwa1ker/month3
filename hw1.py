import flet as ft

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello Geeks')
    greeting_history = []
    history_text = ft.Text(value='История приветствий: ')

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6)

    def toggle_theme(_):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    theme_button.on_click = toggle_theme

    def on_button_click(_):
        name = name_input.value
        if name:
            text_hello.color = None
            text_hello.value = f"Hello {name}"
            name_input.value = None
            greeting_history.append(name)
            history_text.value = "История приветствий\n" + '\n'.join(greeting_history)
        else:
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Введите имя'
        page.update()

    name_input = ft.TextField(on_submit=on_button_click, label='Введите имя', expand=True)
    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.RED,
                                        icon_color=ft.Colors.GREEN, on_click=on_button_click)

    main_object = ft.Row([name_input, elevated_button, theme_button])

    page.add(text_hello, main_object, history_text)

ft.app(main_page)



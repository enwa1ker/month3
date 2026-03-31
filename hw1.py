count = 0

def setup_button():
    def on_button_click():
        global count 
        count += 1
        print(f"Нажато {count} раз")
    return on_button_click

click_handler = setup_button()
click_handler() 
click_handler() 
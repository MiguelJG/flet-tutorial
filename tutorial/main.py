import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

    ##To display updates at the page
    tt = ft.Text()
    page.add(tt) # it's a shortcut for page.controls.append(t) and then page.update()
    for i in range(10):
        tt.value = f"Step {i}"
        page.update()
        time.sleep(1)
        
    #Some controls are "container" controls (like Page) which could contain other controls. For example, Row control allows arranging other controls in a row one-by-one, or TextField and ElevatedButton next to it.
    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
        ])
    )   
    page.update()

    page.add(
    ft.Row(controls=[
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!")
        ])
    )
    page.update()
    
    #"smart" behaviour of page.update
    temp = len(page.controls)
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(temp)
        page.update()
        time.sleep(0.3)

    #Controls event handlers

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))   

    # more advanced example for a simple To-Do
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    #Properties examples: if you have a form with multiple entry control you can set disabled property for each control individually
    first_name = ft.TextField(hint_text="First Name", width=300)
    last_name = ft.TextField(hint_text="Last Name", width=300)
    first_name.disabled = False
    last_name.disabled = True
    page.add(first_name, last_name)

    #or you can put form controls into container, e.g. Column and then set disabled for the column:

    first_name = ft.TextField(hint_text="First Name", width=300)
    last_name = ft.TextField(hint_text="Last Name Name", width=300)
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True
    page.add(c)

    #Buttons

    btn = ft.ElevatedButton("Click me!")
    page.add(btn)

    ### Event handlers
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    ## Text field example

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            #page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

    #CheckBox
    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

    #Dropdown

    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)
    page.scroll = "always"

ft.app(main)
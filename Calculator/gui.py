# gui.py
import flet as ft
from logic import Calculator

def main(page: ft.Page):
    page.title = "Calculator"
    page.bgcolor = "#1E1E1E"  # Dark background for a modern look
    page.padding = 20
    
    calc = Calculator()
    display = ft.Text(value="0", size=60, color="white", text_align=ft.TextAlign.RIGHT, weight=ft.FontWeight.BOLD)
    
    def on_button_click(e):
        display.value = calc.process_input(e.control.text)
        page.update()
    
    button_texts = [
        ["AC", "+/-", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", "", "="]
    ]
    
    button_grid = ft.Column(spacing=5, alignment=ft.MainAxisAlignment.CENTER)
    for row in button_texts:
        row_buttons = []
        for text in row:
            if text:
                btn = ft.ElevatedButton(
                    text=text,
                    width=85, height=85,
                    on_click=on_button_click,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=20),
                        color="white" if text not in ["AC", "+/-", "%"] else "black",
                        bgcolor="#FFA500" if text in ["/", "*", "-", "+", "="] else "#A9A9A9" if text in ["AC", "+/-", "%"] else "#333333",
                        padding=10,
                    )
                )
                row_buttons.append(btn)
        button_grid.controls.append(ft.Row(row_buttons, alignment=ft.MainAxisAlignment.CENTER))
    
    page.add(
        ft.Column([
            ft.Container(display, padding=15, alignment=ft.alignment.center_right, width=400, bgcolor="#2E2E2E", border_radius=10),
            button_grid
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
    )

ft.app(target=main)

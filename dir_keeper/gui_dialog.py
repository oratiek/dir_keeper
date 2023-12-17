import flet as ft

def dialog(page: ft.Page):
    # window config
    page.window_height = 100
    page.window_width = 210
    #page.window_frameless = True 
    page.window_resizable = False

    def pick_files_result(e: ft.FilePickerResultEvent):
        print(e.path)

    def __open():
        pick_files_dialog.get_directory_path()


    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Choose Directory",
                    icon = ft.icons.UPLOAD_FILE,
                    on_click = lambda _:pick_files_dialog.get_directory_path()
                ),
                selected_files,
            ]
        )
    )
    __open()


if __name__ == "__main__":
    ft.app(target=dialog)

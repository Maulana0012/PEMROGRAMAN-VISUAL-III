import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profil", layout=[
    [sg.Text("FTI UNISKA", font="Helvetica 24")],
    [sg.Text("FAKULTAS   INFORMASI")],
    [sg.Text("UNISKA MAB BANJARMASIN")]],size=(430, 200), font="Times 18")
window()
window.close()

import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profil", layout=[
    [sg.Text("TEKNOLOGI INNFORMASI", size=(21, 1), justification="center")],
    [sg.Text("TEKNOLOGI INNFORMASI", size=(25, 1), justification="left")],
    [sg.Text("TEKNOLOGI INNFORMASI", size=(25, 1), justification="right")],
    [sg.Text(("TEKNOLOGI INNFORMASI" + " ") * 2, size=(25, 2), justification="center")],
    [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FFCC00")]], size=(430, 250), font="Times 18")
window()
window.close()

import PySimpleGUI as sg

preMadLayout = [[sg.Push(), sg.Text("UNISKA MAAB", font="helvetica 24")],
                [sg.Push(), sg.Text("BANJARMASIN", font="courier 18")]]

sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Element Text", layout=preMadLayout, size=(430, 200))
window()
window.close()

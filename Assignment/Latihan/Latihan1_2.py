import PySimpleGUI as sg
sg.theme("DarkGreen2")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Latihan Pertama", layout=[
    [sg.Text("Selamat Data DiKelas:", font=("Arial", 24, "italic", "bold","underline","overstrike"))],
    [sg.Text("NPM: 2210010498")],
    [sg.Text("Name: Ahmad Maulana Malik Ibrahim")],
    [sg.Text("Kelas: 5M Reguler Banjarmain")], ], size=(400, 200))
window()
window.close()

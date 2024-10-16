import PySimpleGUI as sg
sg.theme("LightPurple")
# sg.theme_list() to check theme list
# sg.theme_text_color("#FFFF00") to change txt color
window = sg.Window(title="Latihan Pertama", layout=[
    [sg.Text("NPM: 2210010498")],
    [sg.Text("Nama: Ahmad Maulana Malik Ibrahim")],
    [sg.Text("Kelas: 5M Reguler Pagi")],
    [sg.Text("Matakuliah: Pemrograman Visual 3")],], size=(400, 200), font=("Times", 11))
window()
window.close()

import PySimpleGUI as sg

layout = [
    [sg.Input(key='-INPUT-'), sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'), sg.Button('Convert', key='-SUBMIT-')],
    [sg.Text('Output: ', key='-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    unit = values['-UNITS-']
    input = values['-INPUT-']
    
    if event == '-SUBMIT-':
        if input.isnumeric():
            if(unit == 'km to mile'):
                output = round(float(input) * 0.621371, 2)
                output_string = f'Output: {input} kilometer(s) is {output} mile(s)'
            if(unit == 'kg to pound'):
                output = round(float(input) * 2.20462, 2)
                output_string = f'Output: {input} kilogram(s) is {output} pound(s)'
            if(unit == 'sec to min'):
                output = round(float(input)/60, 2)
                output_string = f'Output: {input} second(s) is {output} minute(s)'
            window['-OUTPUT-'].Update(output_string)
        else:
            window['-OUTPUT-'].Update("Please Enter a Number")
    
window.close()
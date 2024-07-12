import math
import copy
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

dic1 = {}
dic2 = {}
# Indica si ya se usó o no el dic1
original = 0

lista = []
transformada = []

numCoord = -1
numCoord3D = -1


def orden(lista):
    uso = lista.copy()
    ordenada = []
    # Ordena primero de menor x a mayor x
    term = False
    mayory = [copy.deepcopy(uso[0])]
    while term == False:
        if len(uso) != 0:
            temp = []
            menx = uso[0][0]
            meny = uso[0][1]

            mod = 0
            for i in range(0, len(uso)):
                if menx > uso[i][0]:
                    menx = uso[i][0]
                    meny = uso[i][1]
                    if len(temp) == 0:
                        temp.append(uso[i])
                    else:
                        temp.pop(0)
                        temp.append(uso[i])
                    mod += 1
                elif menx == uso[i][0]:
                    if meny > uso[i][1]:
                        meny = uso[i][1]
                        if len(temp) == 0:
                            temp.append(uso[i])
                        else:
                            temp.pop(0)
                            temp.append(uso[i])
                        mod += 1
                    elif meny == uso[i][1]:
                        continue
                if mayory[0][1] < uso[i][1]:
                    mayory = [copy.deepcopy(uso[i])]

            if mod == 0:
                ordenada.append(uso[0])
                uso.pop(0)
            else:
                ordenada.append(temp[0])
                uso.pop(uso.index(temp[0]))

        else:
            term = True
    # Ordena el poligono

    # Ordena primero por arriba hacia la 'y' más grande, al llegar a esta la agrega y luego toma la lista ordenada de menor a mayor y la une al reves
    copordenada = []
    ind = 0
    copordenada.append(ordenada[0])
    ordenada.pop(0)
    entrada = 0

    while term == True:
        if len(ordenada) != 0:
            temp = []
            x1 = copordenada[ind][0]
            y1 = copordenada[ind][1]
            x2 = ordenada[-1][0]
            y2 = ordenada[-1][1]
            mod = 0
            iguales = 0
            mendis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            menordistancia = mendis
            for i in range(0, len(ordenada)):
                x2 = ordenada[i][0]
                y2 = ordenada[i][1]

                if x2 != x1 and y2 != y1:
                    mendis2 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                elif x2 == x1 and y2 > y1:
                    temp.append(ordenada[i])
                    copordenada.append(temp[0])
                    ordenada.pop(ordenada.index(temp[0]))
                    ind += 1
                    mod += 1
                    iguales += 1
                    break

                if mendis2 < menordistancia and y2 > y1:
                    menordistancia = mendis2
                    temp.append(ordenada[i])
                    mod += 1
                elif mendis2 == mendis:
                    continue

            if copordenada[-1] == mayory[0]:
                entrada = 1
                term = False

            if mod == 0 and entrada == 0:
                copordenada.append(ordenada[0])
                ordenada.pop(0)
                ind += 1
            else:
                if entrada == 0 and iguales == 0:
                    copordenada.append(temp[0])
                    ordenada.pop(ordenada.index(temp[0]))
                    ind += 1

    for i in range(0, len(ordenada)):
        copordenada.append(ordenada[-1])
        ordenada.pop(-1)

    return copordenada


#Funciones 2D

def traslacion(lista, dx, dy):
    for i in range(0, len(lista)):
        lista[i][0] += dx
        lista[i][1] += dy


def rotacionorigen(lista, grados):
    for i in range(0, len(lista)):
        equis = lista[i][0]
        ye = lista[i][1]
        lista[i][0] = round(((equis * math.cos(math.radians(grados))) - (ye * math.sin(math.radians(grados)))), 2)
        lista[i][1] = round(((equis * math.sin(math.radians(grados))) + (ye * math.cos(math.radians(grados)))), 2)


def rotacionpivote(lista, pivote, grados):
    for i in range(0, len(lista)):
        equis = lista[i][0]
        ye = lista[i][1]
        pivx = pivote[0]
        pivy = pivote[1]
        lista[i][0] = round(
            (pivx + ((equis - pivx) * math.cos(math.radians(grados))) - ((ye - pivy) * math.sin(math.radians(grados)))),
            2)
        lista[i][1] = round(
            (pivy + ((equis - pivx) * math.sin(math.radians(grados))) + ((ye - pivy) * math.cos(math.radians(grados)))),
            2)


def escalamiento(lista, escx, escy):
    for i in range(0, len(lista)):
        lista[i][0] *= escx
        lista[i][0] = round(lista[i][0], 2)
        lista[i][1] *= escy
        lista[i][1] = round(lista[i][1], 2)

#Funciones 3D
def traslacion3D(lista, dx, dy, dz):
    for i in range(0, len(lista)):
        lista[i][0] += dx
        lista[i][1] += dy
        lista[i][2] += dz

def rotacionZ(lista, grados):
    for i in range(0, len(lista)):
        equis = lista[i][0]
        ye = lista[i][1]
        lista[i][0] = round(((equis * math.cos(math.radians(grados))) - (ye * math.sin(math.radians(grados)))), 2)
        lista[i][1] = round(((equis * (math.sin(math.radians(grados)))) + (ye * math.cos(math.radians(grados)))), 2)

def rotacionX(lista, grados):
    for i in range(0, len(lista)):
        zeta = lista[i][2]
        ye = lista[i][1]
        lista[i][1] = round(((ye * math.cos(math.radians(grados))) - (zeta * math.sin(math.radians(grados)))), 2)
        lista[i][2] = round(((ye * math.sin(math.radians(grados))) + (zeta * math.cos(math.radians(grados)))), 2)

def rotacionY(lista, grados):
    for i in range(0, len(lista)):
        equis = lista[i][0]
        zeta = lista[i][2]
        lista[i][0] = round(((zeta * math.cos(math.radians(grados))) - (equis * math.sin(math.radians(grados)))), 2)
        lista[i][2] = round(((equis * math.cos(math.radians(grados))) + (zeta * math.sin(math.radians(grados)))), 2)

def escalamiento3D(lista, escx, escy, escz):
    for i in range(0, len(lista)):
        lista[i][0] *= escx
        lista[i][0] = round(lista[i][0], 2)
        lista[i][1] *= escy
        lista[i][1] = round(lista[i][1], 2)
        lista[i][2] *= escz
        lista[i][2] = round(lista[i][2], 2)

# Crea un diccionario para utilizarlo en la gráfica
def creardic(lista):
    id = 0
    global original
    if original == 0:
        for elem in lista:
            dic1[str(id)] = elem
            id += 1
        original = 1
    elif original == 1:
        for elem in lista:
            dic2[str(id)] = elem
            id += 1


_VARS = {'window': False, 'fig_agg': False, 'pltFig': False}


def draw_figure(canvas, figura):
    figure_canvas_agg = FigureCanvasTkAgg(figura, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


AppFont = 'Any 9'

sg.theme('Purple')

layout1 = [
           [sg.Checkbox('Ordenar Puntos (Experimental)', key='ordenar')],

           [sg.Text('Coordenada X', s=13), sg.Text('Coordenada Y')],
           [sg.Input(key='coordenadaX', s=15, disabled=True),
            sg.Input(key='coordenadaY', s=15, disabled=True),
            sg.Button('Agregar Coordenada', font=AppFont, disabled=True)],

           [sg.Checkbox('Transformadas Compuestas', key='transcomp'),
            sg.Button('Aplicar Transformada Compuesta', font=AppFont, disabled=True)],

           [sg.Text('Traslación')],
           [sg.Text('Desplazamiento X', s=13), sg.Text('Desplazamiento Y')],
           [sg.Input(key='desplazamientoX', s=15, disabled=True),
            sg.Input(key='desplazamientoY', s=15, disabled=True),
            sg.Button('Traslación', font=AppFont, disabled=True)],

           [sg.Text('Rotación respecto al Origen')],
           [sg.Text('Grados')],
           [sg.Input(key='grados', s=15, disabled=True),
            sg.Button('Rotación respecto al Origen', font=AppFont, disabled=True)],

           [sg.Text('Rotación respecto a un punto Pivote')],
           [sg.Text('Coordenada X', s=13), sg.Text('Coordenada X', s=13), sg.Text('Grados', s=15)],
           [sg.Input(key='pivoteX', s=15, disabled=True), sg.Input(key='pivoteY', s=15, disabled=True),
            sg.Input(key='gradosPiv', s=15, disabled=True),
            sg.Button('Rotación', font=AppFont, disabled=True)],

           [sg.Text('Escalamiento')],
           [sg.Text('Escalamiento X (%)', s=15), sg.Text('Escalamiento Y (%)')],
           [sg.Input(key='escalamientoX', s=17, disabled=True),
            sg.Input(key='escalamientoY', s=17, disabled=True),
            sg.Button('Escalamiento', font=AppFont, disabled=True)],

           ]

layout3 = [[sg.Canvas(key='figCanvas', size=(1,1))]]

layout4 = [[sg.Column(layout1, key='-COL1-'),
           sg.Column(layout3, key='-COL3-')]]

layout2 = [[sg.Text('Coordenada X', s=13), sg.Text('Coordenada Y', s=13), sg.Text('Coordenada Z')],
           [sg.Input(key='coordenadaX3D', s=15, disabled=True),
            sg.Input(key='coordenadaY3D', s=15, disabled=True),
            sg.Input(key='coordenadaZ3D', s=15, disabled=True),
            sg.Button('Agregar Coordenada', key='agCor3D', font=AppFont, disabled=True)],

           [sg.Text('Traslación')],
           [sg.Text('Desplazamiento X', s=13), sg.Text('Desplazamiento Y', s=13), sg.Text('Desplazamiento Z')],
           [sg.Input(key='desplazamientoX3D', s=15, disabled=True),
            sg.Input(key='desplazamientoY3D', s=15, disabled=True),
            sg.Input(key='desplazamientoZ3D', s=15, disabled=True),
            sg.Button('Traslación', key='tras3D', font=AppFont, disabled=True)],

           [sg.Text('Rotación Respecto A:')],
           [sg.Radio('Eje X', 'ejerot', key='ejex', disabled=True),
            sg.Radio('Eje Y', 'ejerot', key='ejey', disabled=True),
            sg.Radio('Eje Z', 'ejerot', key='ejez', disabled=True)],
           [sg.Text('Grados')],
           [sg.Input(key='grados3D', s=15, disabled=True),
            sg.Button('Rotación', key='rot3D', font=AppFont, disabled=True)],

           [sg.Text('Escalamiento')],
           [sg.Text('Escalamiento X (%)', s=15), sg.Text('Escalamiento Y (%)', s=15), sg.Text('Escalamiento Z (%)')],
           [sg.Input(key='escalamientoX3D', s=17, disabled=True),
            sg.Input(key='escalamientoY3D', s=17, disabled=True),
            sg.Input(key='escalamientoZ3D', s=17, disabled=True),
            sg.Button('Escalamiento', key='esc3D', font=AppFont, disabled=True)],

           ]

layout5 = [[sg.Canvas(key='fig3D', size = (1,1))]]

layout6 = [[sg.Column(layout2,  key='-COL2-'),
           sg.Column(layout5,  key='-COL5-'),
           ]]

layout = [[sg.Text('Escoger espacio:')],
          [sg.Button('2D', font=AppFont, disabled=True), sg.Button('3D', font=AppFont)],
          [sg.Text('Número de Puntos')],
          [sg.Input(key='numCoord', s=15), sg.Button('Agregar Número de Coordenadas', font=AppFont)],
          [sg.Frame('', key='frame1', layout=layout4, visible=True), sg.Frame('', key='frame2', layout=layout6, visible=False)],
          [sg.Button('Nuevos Puntos', font=AppFont), sg.Button('Salir', font=AppFont)]
          ]

_VARS['window'] = sg.Window('Transformaciones',
                            layout,
                            finalize=True,
                            resizable=True,
                            location=(100, 100),
                            element_justification="left")


def drawChart():
    _VARS['pltFig'] = plt.figure()

    for i in range(0, len(dic1)):
        #Marca Aristas
        if i != len(dic1) - 1:
            x, y = [[dic1[str(i)][0], dic1[str(i + 1)][0]], [dic1[str(i)][1], dic1[str(i + 1)][1]]]
        else:
            x, y = [[dic1[str(i)][0], dic1[str(0)][0]], [dic1[str(i)][1], dic1[str(0)][1]]]

        plt.plot(x, y, color='black')
    #Marca Vertices
    for i in range(0, len(dic1)):
        x, y = [[dic1[str(i)][0], dic1[str(i)][0]], [dic1[str(i)][1], dic1[str(i)][1]]]

        plt.plot(x, y, marker="o", color='black')
        plt.text(dic1[str(i)][0], dic1[str(i)][1], '({}, {})'.format(dic1[str(i)][0], dic1[str(i)][1]))

    plt.axis('equal')
    plt.axhline(0, color='gray')
    plt.axvline(0, color='gray')
    plt.plot()
    _VARS['fig_agg'] = draw_figure(_VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])


def mostrarTransformada():
    _VARS['fig_agg'].get_tk_widget().forget()
    plt.clf()
    for i in range(0, len(dic1)):
        if i != len(dic1) - 1:
            x, y = [[dic1[str(i)][0], dic1[str(i + 1)][0]], [dic1[str(i)][1], dic1[str(i + 1)][1]]]
        else:
            x, y = [[dic1[str(i)][0], dic1[str(0)][0]], [dic1[str(i)][1], dic1[str(0)][1]]]
        plt.plot(x, y, color='black')
    for i in range(0, len(dic1)):
        x, y = [[dic1[str(i)][0], dic1[str(i)][0]], [dic1[str(i)][1], dic1[str(i)][1]]]
        plt.plot(x, y, marker="o", color='black')

    for i in range(0, len(dic2)):
        if i != len(dic2) - 1:
            x, y = [[dic2[str(i)][0], dic2[str(i + 1)][0]], [dic2[str(i)][1], dic2[str(i + 1)][1]]]
        else:
            x, y = [[dic2[str(i)][0], dic2[str(0)][0]], [dic2[str(i)][1], dic2[str(0)][1]]]
        plt.plot(x, y, color='pink')
        plt.text(dic2[str(i)][0], dic2[str(i)][1], '({}, {})'.format(dic2[str(i)][0], dic2[str(i)][1]))
    for i in range(0, len(dic2)):
        x, y = [[dic2[str(i)][0], dic2[str(i)][0]], [dic2[str(i)][1], dic2[str(i)][1]]]

        plt.plot(x, y, marker="o", color='pink')
        plt.text(dic2[str(i)][0], dic2[str(i)][1], '({}, {})'.format(dic2[str(i)][0], dic2[str(i)][1]))

    plt.axis('equal')
    plt.axhline(0, color='gray')
    plt.axvline(0, color='gray')
    plt.plot()
    _VARS['fig_agg'] = draw_figure(_VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

def drawChart3D():
    _VARS['pltFig'] = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_aspect('auto')
    ax.set_box_aspect([1, 1, 1])

    #Lineas
    #for i in range(0, len(dic1)):
        #if i != len(dic1) - 1:
            #x, y = [[dic1[str(i)][0], dic1[str(i + 1)][0]], [dic1[str(i)][1], dic1[str(i + 1)][1]]]
        #else:
            #x, y = [[dic1[str(i)][0], dic1[str(0)][0]], [dic1[str(i)][1], dic1[str(0)][1]]]

        #plt.plot(x, y, color='black')

    for i in range(0, len(dic1)):
        x, y, z = [[dic1[str(i)][0], dic1[str(i)][0]],
                   [dic1[str(i)][1], dic1[str(i)][1]],
                   [dic1[str(i)][2], dic1[str(i)][2]]]

        ax.plot3D(x, y, z, marker="o", color='black')
        ax.text(dic1[str(i)][0], dic1[str(i)][1], dic1[str(i)][2],
                 '({}, {}, {})'.format(dic1[str(i)][0], dic1[str(i)][1], dic1[str(i)][2]))

    _VARS['fig_agg'] = draw_figure(_VARS['window']['fig3D'].TKCanvas, _VARS['pltFig'])

def mostrarTransformada3D():
    _VARS['fig_agg'].get_tk_widget().forget()
    ax = plt.axes(projection='3d')
    ax.set_aspect('auto')
    ax.set_box_aspect([1,1,1])
    for i in range(0, len(dic1)):
        x, y, z = [[dic1[str(i)][0], dic1[str(i)][0]],
                   [dic1[str(i)][1], dic1[str(i)][1]],
                   [dic1[str(i)][2], dic1[str(i)][2]]]

        ax.scatter(x, y, z, marker="o", color='black')

    for i in range(0, len(dic2)):
        x, y, z = [[dic2[str(i)][0], dic2[str(i)][0]],
                   [dic2[str(i)][1], dic2[str(i)][1]],
                   [dic2[str(i)][2], dic2[str(i)][2]]]

        ax.scatter(x, y, z, marker="o", color='pink')
        ax.text(dic2[str(i)][0], dic2[str(i)][1], dic2[str(i)][2],
                 '({}, {}, {})'.format(dic2[str(i)][0], dic2[str(i)][1], dic2[str(i)][2]))

    _VARS['fig_agg'] = draw_figure(_VARS['window']['fig3D'].TKCanvas, _VARS['pltFig'])

gpiv = 0
dx = 0
dy = 0
dz = 0
g = 0
ex = 1
ey = 1
ez = 1
pivx = 0
pivy = 0
piv = []
layout = 1

while True:
    event, values = _VARS['window'].read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Salir':
        break

    if event == '3D':
        _VARS['window']['frame1'].update(visible=False)
        _VARS['window']['frame2'].update(visible=True)
        _VARS['window']['2D'].update(disabled=False)
        _VARS['window']['3D'].update(disabled=True)

        _VARS['window'].find_element('coordenadaX3D').Update(disabled=True)
        _VARS['window'].find_element('coordenadaY3D').Update(disabled=True)
        _VARS['window'].find_element('coordenadaZ3D').Update(disabled=True)
        _VARS['window'].find_element('agCor3D').Update(disabled=True)

        _VARS['window'].find_element('esc3D').Update(disabled=True)
        _VARS['window'].find_element('escalamientoX3D').Update(disabled=True)
        _VARS['window'].find_element('escalamientoY3D').Update(disabled=True)
        _VARS['window'].find_element('escalamientoZ3D').Update(disabled=True)

        _VARS['window'].find_element('rot3D').Update(disabled=True)
        _VARS['window'].find_element('grados3D').Update(disabled=True)
        _VARS['window'].find_element('ejex').Update(disabled=True)
        _VARS['window'].find_element('ejey').Update(disabled=True)
        _VARS['window'].find_element('ejez').Update(disabled=True)


    if event == '2D':
        _VARS['window']['frame2'].update(visible=False)
        _VARS['window']['frame1'].update(visible=True)
        _VARS['window']['2D'].update(disabled=True)
        _VARS['window']['3D'].update(disabled=False)

    if event == 'Nuevos Puntos' or event == '3D' or event == '2D':
        _VARS['window'].find_element('Agregar Número de Coordenadas').Update(disabled=False)
        _VARS['window'].find_element('numCoord').Update(disabled=False)
        _VARS['window']['numCoord'].update('')
        _VARS['window'].find_element('coordenadaX').Update(disabled=True)
        _VARS['window'].find_element('coordenadaY').Update(disabled=True)
        _VARS['window'].find_element('Agregar Coordenada').Update(disabled=True)

        _VARS['window'].find_element('ordenar').Update(disabled=False)
        _VARS['window'].find_element('desplazamientoX').Update(disabled=True)
        _VARS['window'].find_element('desplazamientoY').Update(disabled=True)
        _VARS['window'].find_element('Traslación').Update(disabled=True)
        _VARS['window'].find_element('grados').Update(disabled=True)
        _VARS['window'].find_element('Rotación respecto al Origen').Update(disabled=True)
        _VARS['window'].find_element('gradosPiv').Update(disabled=True)
        _VARS['window'].find_element('pivoteX').Update(disabled=True)
        _VARS['window'].find_element('pivoteY').Update(disabled=True)
        _VARS['window'].find_element('Rotación').Update(disabled=True)
        _VARS['window'].find_element('escalamientoX').Update(disabled=True)
        _VARS['window'].find_element('escalamientoY').Update(disabled=True)
        _VARS['window'].find_element('Escalamiento').Update(disabled=True)
        _VARS['window'].find_element('Aplicar Transformada Compuesta').Update(disabled=True)

        _VARS['window']['coordenadaX3D'].update(disabled=True)
        _VARS['window']['coordenadaY3D'].update(disabled=True)
        _VARS['window']['coordenadaZ3D'].update(disabled=True)
        _VARS['window'].find_element('agCor3D').Update(disabled=True)
        _VARS['window'].find_element('desplazamientoX3D').Update(disabled=True)
        _VARS['window'].find_element('desplazamientoY3D').Update(disabled=True)
        _VARS['window'].find_element('desplazamientoZ3D').Update(disabled=True)
        _VARS['window'].find_element('tras3D').Update(disabled=True)
        _VARS['window'].find_element('esc3D').Update(disabled=True)
        _VARS['window'].find_element('escalamientoX3D').Update(disabled=True)
        _VARS['window'].find_element('escalamientoY3D').Update(disabled=True)
        _VARS['window'].find_element('escalamientoZ3D').Update(disabled=True)
        _VARS['window'].find_element('rot3D').Update(disabled=True)
        _VARS['window'].find_element('ejex').Update(disabled=True)
        _VARS['window'].find_element('ejey').Update(disabled=True)
        _VARS['window'].find_element('ejez').Update(disabled=True)


        if bool(dic1):
            _VARS['fig_agg'].get_tk_widget().forget()
            plt.clf()
            plt.axis('equal')
            plt.axhline(0, color='gray')
            plt.axvline(0, color='gray')
            plt.plot()
            _VARS['fig_agg'] = draw_figure(_VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

        dic1 = {}
        dic2 = {}
        original = 0
        lista = []
        transformada = []
        numCoord = -1
        numCoord3D = -1

    if event == 'Agregar Número de Coordenadas':
        numCoord = int(values['numCoord'])
        numCoord3D = int(values['numCoord'])
        _VARS['window'].find_element('coordenadaX').Update(disabled=False)
        _VARS['window'].find_element('coordenadaY').Update(disabled=False)
        _VARS['window'].find_element('Agregar Coordenada').Update(disabled=False)

        _VARS['window'].find_element('coordenadaX3D').Update(disabled=False)
        _VARS['window'].find_element('coordenadaY3D').Update(disabled=False)
        _VARS['window'].find_element('coordenadaZ3D').Update(disabled=False)
        _VARS['window'].find_element('agCor3D').Update(disabled=False)

        _VARS['window'].find_element('Agregar Número de Coordenadas').Update(disabled=True)
        _VARS['window'].find_element('numCoord').Update(disabled=True)

    if event == 'Agregar Coordenada':
        x = float(values['coordenadaX'])
        y = float(values['coordenadaY'])
        lista.append([x, y])
        _VARS['window']['coordenadaX'].update('')
        _VARS['window']['coordenadaY'].update('')
        numCoord -= 1

    if numCoord == 0:
        _VARS['window'].find_element('coordenadaX').Update(disabled=True)
        _VARS['window'].find_element('coordenadaY').Update(disabled=True)
        _VARS['window'].find_element('Agregar Coordenada').Update(disabled=True)
        _VARS['window'].find_element('ordenar').Update(disabled=True)
        _VARS['window'].find_element('desplazamientoX').Update(disabled=False)
        _VARS['window'].find_element('desplazamientoY').Update(disabled=False)
        _VARS['window'].find_element('Traslación').Update(disabled=False)
        _VARS['window'].find_element('grados').Update(disabled=False)
        _VARS['window'].find_element('Rotación respecto al Origen').Update(disabled=False)
        _VARS['window'].find_element('gradosPiv').Update(disabled=False)
        _VARS['window'].find_element('pivoteX').Update(disabled=False)
        _VARS['window'].find_element('pivoteY').Update(disabled=False)
        _VARS['window'].find_element('Rotación').Update(disabled=False)
        _VARS['window'].find_element('escalamientoX').Update(disabled=False)
        _VARS['window'].find_element('escalamientoY').Update(disabled=False)
        _VARS['window'].find_element('Escalamiento').Update(disabled=False)
        _VARS['window'].find_element('Aplicar Transformada Compuesta').Update(disabled=False)

        if values['ordenar']:
            lista = orden(lista)

        transformada = copy.deepcopy(lista)
        creardic(lista)
        drawChart()
        numCoord = -1

    if event == 'agCor3D':
        x = float(values['coordenadaX3D'])
        y = float(values['coordenadaY3D'])
        z = float(values['coordenadaZ3D'])
        lista.append([x, y, z])
        print(lista)
        _VARS['window']['coordenadaX3D'].update('')
        _VARS['window']['coordenadaY3D'].update('')
        _VARS['window']['coordenadaZ3D'].update('')
        numCoord3D -= 1

    if numCoord3D == 0:
        _VARS['window']['coordenadaX3D'].update(disabled=True)
        _VARS['window']['coordenadaY3D'].update(disabled=True)
        _VARS['window']['coordenadaZ3D'].update(disabled=True)
        _VARS['window'].find_element('agCor3D').Update(disabled=True)
        _VARS['window'].find_element('desplazamientoX3D').Update(disabled=False)
        _VARS['window'].find_element('desplazamientoY3D').Update(disabled=False)
        _VARS['window'].find_element('desplazamientoZ3D').Update(disabled=False)
        _VARS['window'].find_element('tras3D').Update(disabled=False)
        _VARS['window'].find_element('esc3D').Update(disabled=False)
        _VARS['window'].find_element('escalamientoX3D').Update(disabled=False)
        _VARS['window'].find_element('escalamientoY3D').Update(disabled=False)
        _VARS['window'].find_element('escalamientoZ3D').Update(disabled=False)
        _VARS['window'].find_element('rot3D').Update(disabled=False)
        _VARS['window'].find_element('grados3D').Update(disabled=False)
        _VARS['window'].find_element('ejex').Update(disabled=False)
        _VARS['window'].find_element('ejey').Update(disabled=False)
        _VARS['window'].find_element('ejez').Update(disabled=False)


        transformada = copy.deepcopy(lista)
        creardic(lista)
        drawChart3D()
        numCoord3D = -1

    if event == 'tras3D':
        dx += float(values['desplazamientoX3D'])
        dy += float(values['desplazamientoY3D'])
        dz += float(values['desplazamientoZ3D'])
        traslacion3D(transformada, dx, dy, dz)
        print(transformada)
        _VARS['window']['desplazamientoX3D'].update('')
        _VARS['window']['desplazamientoY3D'].update('')
        _VARS['window']['desplazamientoZ3D'].update('')
        creardic(transformada)
        mostrarTransformada3D()
        dx = 0
        dy = 0
        dz = 0

    if event == 'rot3D':
        if values['ejex']:
            g += float(values['grados3D'])
            rotacionX(transformada, g)
            print(transformada)
            _VARS['window']['grados3D'].update('')
            creardic(transformada)
            mostrarTransformada3D()
            g = 0

        if values['ejey']:
            g += float(values['grados3D'])
            rotacionY(transformada, g)
            print(transformada)
            _VARS['window']['grados3D'].update('')
            creardic(transformada)
            mostrarTransformada3D()
            g = 0

        if values['ejez']:
            g += float(values['grados3D'])
            rotacionZ(transformada, g)
            print(transformada)
            _VARS['window']['grados3D'].update('')
            creardic(transformada)
            mostrarTransformada3D()
            g = 0

    if event == 'esc3D':
        ex = float(values['escalamientoX3D']) / 100
        ey = float(values['escalamientoY3D']) / 100
        ez = float(values['escalamientoZ3D']) / 100
        escalamiento3D(transformada, ex, ey, ez)
        print(transformada)
        _VARS['window']['escalamientoX3D'].update('')
        _VARS['window']['escalamientoY3D'].update('')
        _VARS['window']['escalamientoZ3D'].update('')
        creardic(transformada)
        mostrarTransformada3D()
        ex = 1
        ey = 1
        ez = 1



    if values['transcomp']:

        _VARS['window'].find_element('Aplicar Transformada Compuesta').Update(disabled=False)

        if event == 'Traslación':
            dx += float(values['desplazamientoX'])
            dy += float(values['desplazamientoY'])
            _VARS['window']['desplazamientoX'].update('')
            _VARS['window']['desplazamientoY'].update('')

        if event == 'Rotación respecto al Origen':
            g += float(values['grados'])
            _VARS['window']['grados'].update('')

        if event == 'Rotación':
            pivx = float(values['pivoteX'])
            pivy = float(values['pivoteY'])
            piv = [pivx, pivy]
            gpiv += float(values['gradosPiv'])
            _VARS['window']['gradosPiv'].update('')
            _VARS['window'].find_element('pivoteX').Update(disabled=True)
            _VARS['window'].find_element('pivoteY').Update(disabled=True)

        if event == 'Escalamiento':
            ex *= float(values['escalamientoX']) / 100
            ey *= float(values['escalamientoY']) / 100
            _VARS['window']['escalamientoX'].update('')
            _VARS['window']['escalamientoY'].update('')

        if event == 'Aplicar Transformada Compuesta':
            piv = [pivx, pivy]
            traslacion(transformada, dx, dy)
            rotacionorigen(transformada, g)
            rotacionpivote(transformada, piv, gpiv)
            escalamiento(transformada, ex, ey)

            _VARS['window']['pivoteX'].update('')
            _VARS['window']['pivoteY'].update('')

            creardic(transformada)
            mostrarTransformada()
            gpiv = 0
            dx = 0
            dy = 0
            g = 0
            ex = 1
            ey = 1
            pivx = 0
            pivy = 0
            piv = []

    else:

        _VARS['window'].find_element('pivoteX').Update(disabled=False)
        _VARS['window'].find_element('pivoteY').Update(disabled=False)
        _VARS['window'].find_element('Aplicar Transformada Compuesta').Update(disabled=True)

        if event == 'Traslación':
            dx = float(values['desplazamientoX'])
            dy = float(values['desplazamientoY'])
            traslacion(transformada, dx, dy)
            _VARS['window']['desplazamientoX'].update('')
            _VARS['window']['desplazamientoY'].update('')
            creardic(transformada)
            mostrarTransformada()
            dx = 0
            dy = 0

        if event == 'Rotación respecto al Origen':
            g = float(values['grados'])
            rotacionorigen(transformada, g)
            _VARS['window']['grados'].update('')
            creardic(transformada)
            mostrarTransformada()
            g = 0

        if event == 'Rotación':
            pivx = float(values['pivoteX'])
            pivy = float(values['pivoteY'])
            piv = [pivx, pivy]
            gpiv = float(values['gradosPiv'])
            rotacionpivote(transformada, piv, gpiv)
            _VARS['window']['gradosPiv'].update('')
            _VARS['window']['pivoteX'].update('')
            _VARS['window']['pivoteY'].update('')
            creardic(transformada)
            mostrarTransformada()
            gpiv = 0
            piv = []
            pivx = 0
            pivy = 0

        if event == 'Escalamiento':
            ex = float(values['escalamientoX']) / 100
            ey = float(values['escalamientoY']) / 100
            escalamiento(transformada, ex, ey)
            _VARS['window']['escalamientoX'].update('')
            _VARS['window']['escalamientoY'].update('')
            creardic(transformada)
            mostrarTransformada()
            ex = 1
            ey = 1

_VARS['window'].close()

import time
import json
import os


# j = '{"fecha_registro":"2021/02/02","hora_inicio":"23:37:55","hora_cierre":"23:38:15","trabajo":"nasa","observaciones":"nada","estado":"cerrado"}'
# jD = json.loads(j)

# print(jD["hora_inicio"])

#{
#    "fecha_registro":"2021/02/02",
#    "hora_inicio":"23:37:55",
#    "hora_cierre":"23:38:15",
#    "trabajo":"nasa",
#    "observaciones":"nada",
#    "estado":"cerrado"
#}

class registro:

    def __init__(self, fechaReg, horaInicio, horaCierre, trabajo, obvs, estado):
        self.fechaReg   = fechaReg
        self.horaInicio = horaInicio
        self.horaCierre = horaCierre
        self.trabajo    = trabajo
        self.obvs       = obvs
        self.estado     = estado
    
    def GetfechaReg(self):
        return self.fechaReg
    def GethoraInicio(self):
        return self.horaInicio
    def GethoraCierre(self):
        return self.horaCierre
    def Gettrabajo(self):
        return self.trabajo
    def Getobvs(self):
        return self.obvs
    def Getestado(self):
        return self.estado
    def SethoraCierre(self, horaCierre):
        self.horaCierre = horaCierre
    def Setestado(self, estado):
        self.estado = estado

    def VerRegistro(self):
        print('\nDia:           ' +self.fechaReg+
              '\nHora Inicio:   ' +self.horaInicio+
              '\nHora Cierre:   ' +self.horaCierre+
              '\nTrabajo:       ' +self.trabajo+
              '\nObservaciones: ' +self.obvs+
              '\nEstado:        ' +self.estado)

# reg = registro(time.strftime("%x"), time.strftime("%X"), '', '', '')

# reg.VerRegistro()
# print('\n/////////////////---\\\\\\\\\\\\\\\\ \n')

# reg.SethoraCierre(time.strftime("%X"))

# reg.VerRegistro()


# num | trabajo |   fecha    | hora inicio | hora final | estado
# 000 | CUS0556 | 2021/02/02 |   00:00:00  |  00:00:00  | abierto
listaRegistros = []

def ImprimirRegistros():
    x = len(listaRegistros)
    print('NUM | Trabajo |  Fecha   | hora inicio | Hora Final | Estado')
    for i in range(x):
        print(str(i) +'   | ' +listaRegistros[i].Gettrabajo() +' | ' +listaRegistros[i].GetfechaReg() +' |   ' +listaRegistros[i].GethoraInicio() +'  |  ' +listaRegistros[i].GethoraCierre() +'  | ' +listaRegistros[i].Getestado())

def FileTxt():
    # nombre = 'export - ' ++'.txt'
    # f = open("fichero_num_%s.txt" % time.strftime("%x") , 'w')
    f = open('Export test.txt' , 'w')
    x = len(listaRegistros)
    f.write('NUM | Trabajo |  Fecha   | hora inicio | Hora Final | Estado | Observaciones')
    for i in range(x):
        f.write(str(i) +'   | ' +listaRegistros[i].Gettrabajo() +' | ' +listaRegistros[i].GetfechaReg() +' |   ' +listaRegistros[i].GethoraInicio() +'  |  ' +listaRegistros[i].GethoraCierre() +'  | ' +listaRegistros[i].Getestado() +' | ' +listaRegistros[i].Getobvs())
    f.close()

while True:

    comando = input('Comando:\n')

    if comando == 'exit':
        break
    if comando == 'cargar registro':
        tipo = input('Tipo de registro:\n')
        if tipo == 'abierto':
            rTrabajo = input('Trabajo:\n')
            rObvs    = input('Observaciones:\n')
            listaRegistros.append(registro(time.strftime("%x"), time.strftime("%X"), '', rTrabajo, rObvs, 'abierto'))
            print('Registro creado satisfactoriamente')
        elif tipo == 'controlado':
            print('todavia no lo pensaste')
        elif tipo == 'cerrado':
            rTrabajo = input('Trabajo:\n')
            rObvs    = input('Observaciones:\n')
            hTrabajo = input('Horas de trabajadas\n')
            horaIni = time.gmtime(time.time() - (int(hTrabajo) *3600))
            rHoraCierre = str(horaIni.tm_hour) +':' +str(horaIni.tm_min) +':' +str(horaIni.tm_sec)
            listaRegistros.append(registro(time.strftime("%x"), rHoraCierre, time.strftime("%X"), rTrabajo, rObvs, 'cerrado'))
            print('Registro creado satisfactoriamente')
    if comando == 'cerrar registro':
        ImprimirRegistros()
        regACerrar = input('\nRegistro a cerrar:\n')
        if (listaRegistros[int(regACerrar)].Getestado()) == 'abierto':
            listaRegistros[int(regACerrar)].SethoraCierre(time.strftime("%X"))
            listaRegistros[int(regACerrar)].Setestado('cerrado')
            print('Registro cerrado')
        else:
            print('El registro ya esta cerrado')
    if comando == 'ver registro':
        ImprimirRegistros()
        regAVer = input('\nRegistro a ver:\n')
        listaRegistros[int(regAVer)].VerRegistro()
    if comando == 'export':
        FileTxt()

    print('\n')

    # print(listaRegistros)
    # print(listaRegistros[0].VerRegistro())






import time


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

listaRegistros = []


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
        elif tipo == 'controlado':
            print('todavia no lo pensaste')
        elif tipo == 'cerrado':
            print('todavia no lo pensaste')
            # hTrabajo = input('Horas de trabajo\n')
            # horaIni = time.time() - (int(hTrabajo) *3600)
            # print(time.strftime()
    if comando == 'cerrar registro':
        regACerrar = input('Registro a cerrar:\n')
        if (listaRegistros[int(regACerrar)].Getestado()) == 'abierto':
            listaRegistros[int(regACerrar)].SethoraCierre(time.strftime("%X"))
            listaRegistros[int(regACerrar)].Setestado('cerrado')
            print('Registro cerrado')
        else:
            print('El registro ya esta cerrado')
    if comando == 'ver registro':
        regAVer = input('Registro a ver:\n')
        listaRegistros[int(regAVer)].VerRegistro()
        print('\n')
    

    # print(listaRegistros)
    # print(listaRegistros[0].VerRegistro())






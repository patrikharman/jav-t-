import Auto


def beolvas():
    automLista = []
    beFajl = open("auto.txt","r",encoding="utf-8")
    sorok = beFajl.readline()
    for index in range(0,len(sorok),1):
        mostsor = sorok[index].strip()
        tipus = Auto.Auto (mostsor[0],mostsor[1],mostsor[2],mostsor[3],mostsor[4],mostsor[5],mostsor[6])
        automLista.append(tipus)
        print(automLista)
        beFajl.close()

        return automLista
def tabla():
    pass

def flotta():
    pass

def ertekes():
    pass


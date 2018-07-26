# -*- coding: latin-1 -*-
pnumber = 115413
purl = "http://www.tjrs.jus.br/site_php/precatorios/precatorio.php?aba_opcao_consulta=numero&Numero_Informado={0}&tipo_pesquisa=por_precatorio&btnPEsquisar=Pesquisar".format(pnumber)

import re
import urllib2
import sqlite3
import datetime
import threading
import signal
import time
from HTMLParser import HTMLParser

# pfile = 'ptest'
#
# with open('ptest') as f1:
#     data = f1.read()

# number, date,

hparser = HTMLParser()

delay = 600
thw = None
stop = False

def sighand(signal, frame):
    global thw
    global stop
    print "bye"
    thw.cancel()
    stop = True

def queryp():

    global thw

    req = urllib2.urlopen(purl)
    data = req.read()

    encoding = req.headers.getparam('charset')

    udata = unicode(data, encoding)
    tofile = hparser.unescape(udata)

    ofile = open("ptestp.html", 'w')
    ofile.write(tofile.encode("utf-8"))
    ofile.close()

    datenow = datetime.datetime.now().strftime("%m/%d/%y %H:%M")

    if re.search(r'n.o est. na fila', data):
        print "not on line"
        quit()

    crongroups = re.search(r'na Fila Ordem Cronol[\D\s]+([0-9]+).*', data)
    cronord = crongroups.group(1)

    valuegroups = re.search(r'Fila Ordem Crescente de Valor[\D\s]+([0-9]+).*[\D\s]+([0-9]+).*', data)
    #valueord = valuegroups.group(2)
    valueord = 0

    print cronord, valueord

    conn = sqlite3.connect('pdata.db')
    c = conn.cursor()

    c.execute("INSERT INTO history(number, cronord, valueord, qdate) VALUES({0}, {1}, {2}, '{3}');".format(pnumber, cronord, valueord, datenow))

    conn.commit()
    conn.close()

    thw = threading.Timer(delay, queryp)
    thw.start()

signal.signal(signal.SIGINT, sighand)
queryp()
while not stop:
    time.sleep(1)

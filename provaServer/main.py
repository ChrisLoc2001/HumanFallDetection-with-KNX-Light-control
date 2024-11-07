import asyncio
import socket
import sys
import subprocess

from xknx import XKNX
from xknx.devices import Light

async def ricevi_notifica(conn):
    while True:
        notifica = conn.recv(4096)
        print(notifica.decode())
        await gestione_Luci(notifica.decode())

async def gestione_Luci(notifica):
    try:
        async with XKNX() as xknx:
                light = Light(xknx,
                name="prova",
                group_address_switch="0/0/1")
                print("KNX connection ok")
                if (notifica == "FALL"):
                    print("accendi")
                    await light.set_on()
                if(notifica == "SPEGNI"):
                    await light.set_off()
    except Exception as e:
        print(e)

async def sub_server(indirizzo, backlog = 1):
    try:
        s = socket.socket()
        s.bind(indirizzo)
        s.listen(backlog)
        print("Server inizializzato")
    except socket.error as err:
        print("Errore")

    conn, indirizzo_client = s.accept()
    print("connessione --> ")
    await ricevi_notifica(conn)

if __name__ == "__main__":
    asyncio.run(sub_server(("",15000)))


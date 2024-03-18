from partida import Partida
from gestorDePartida import GestorDePartida
from arbitro import Arbitro
from administradorDeEventos import AdministradorDeEventos


if __name__ == "__main__":
    partida = Partida()
    gestorDePartida = GestorDePartida(partida)
    arbitro = Arbitro(partida)

    gestorDePartida.agregarArbitro(arbitro)
    administradorDeEventos = AdministradorDeEventos(partida.tablero, arbitro)
    gestorDePartida.agregarAdministradorDeEventos(administradorDeEventos)

    gestorDePartida.iniciarPartida()
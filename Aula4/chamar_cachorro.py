#!/usr/bin/env python3

# from Cachorro import Cachorro
import Cachorro

dados_do_cachorro = {
    'nome':'Rex',
    'idade': 8,
    'cor':'Branco',
    'raca':'Poodle',
    'porte':'Pequeno'
}
rex = Cachorro.Cachorro(**dados_do_cachorro)

rex.latir()
rex.cagar()
rex.dormir()
rex.cheirar()

rex.focinho = False

rex.cheirar()

input()


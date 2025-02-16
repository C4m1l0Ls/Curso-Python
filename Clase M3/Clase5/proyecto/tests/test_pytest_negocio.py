import sys
import os

#fijar ruta directta a lalogica del negocio 
sys.path.insert(0, os.expandtabs(os.path.join(os.path.dirname(__file__), '../src')))
from negocio import VendedorBase, VendedorPremiun


import pytest

def test_calcular_comision_base():
    vendedor = VendedorBase ("pedro", 1000)
    assert vendedor.calcular_comision() == 100.0

def test_calcular_comision_premium():
    vendedor = VendedorPremiun("Maria", 2000)
    assert vendedor.calcular_comision() == 300.0
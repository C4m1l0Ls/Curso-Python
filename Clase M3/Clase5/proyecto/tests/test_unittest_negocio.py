import sys
import os

#fijar ruta directa ala lofgica del negocio (negocio.py y __init__.py)
sys.path.insert(0, os.path.abspath(os.path.join((os.path.dirname)(__file__), '../src')))

from negocio import VendedorBase, VendedorPremiun
import unittest

class TestVendedor(unittest.TestCase):
    def setUp(self):
        self.vendedor_base = VendedorBase ("luis", 1000) # comision = 100.0
        self.vendedor_premiun = VendedorPremiun ("carlos", 2000) #comision = 300.0
    
    def test_clacular_comision_base (self):
        self.assertEqual(self.vendedor_base.calcular_comision(), 100.0)

    def test_clacular_comision_base (self):
        self.assertEqual(self.vendedor_premiun.calcular_comision(), 300.0)

if __name__ == '__main__':
    unittest.main

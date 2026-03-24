# tests/test_calculator.py

import sys
import os

# Ajouter le dossier parent au chemin pour pouvoir importer le module app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.calculator import addition, multiplication

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 5) == 0
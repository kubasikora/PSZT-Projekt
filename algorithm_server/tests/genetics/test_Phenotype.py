import pytest
from genetics import Phenotype

def test_name_exists():
    assert Phenotype

def test_correct_argument():
    ph = Phenotype(6)
    assert ph

def test_if_correctly_creates_genes():
	ph = Phenotype(10)
	assert len(ph.genes) == 10

def test_if_raises_typeerror_on_incorrect_arg():
    with pytest.raises(TypeError):
        ph = Phenotype('5')

def test_if_sets_fitness_correctly():
    ph = Phenotype(10)
    ph.set_fitness(3)
    assert ph.fitness == 3

def test_if_raises_typeerror_on_incorrect_fitness():
    with pytest.raises(TypeError):
        ph = Phenotype(10).set_fitness('3')

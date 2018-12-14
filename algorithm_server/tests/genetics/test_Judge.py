import pytest
from genetics import Judge, Phenotype


def test_name_exists():
    assert Judge

def test_if_creates_judge():
    judge = Judge([1, 2, 3])
    assert judge

def test_if_raises_typeerror_when_cards_are_missing():
    with pytest.raises(Exception):
        judge = Judge()
    
def test_if_correctly_evals_error():
    judge = Judge([1, 2, 3])
    ph1 = Phenotype(3)
    ph1.genes = [True, False, False]
    assert judge.goal_eval(6, 0, ph1) == 50

def test_if_correctly_evals_zero_on_perfect_match():
    judge = Judge([1, 2, 3])
    ph1 = Phenotype(3)
    ph1.genes = [True, True, True]
    assert judge.goal_eval(6, 0, ph1) == 0
    


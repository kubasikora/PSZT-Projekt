import pytest
from genetics import Population, Judge, Phenotype

mock_params = {
    "cards": [1,2,3],
    "mi": 3,
    "lambda": 1,
    "crosses": 1,
    "epochs": 10
}

mock_judge = Judge(mock_params['cards'])

def test_name_exists():
    assert Population

def test_if_creates_empty_population():
    pop = Population(mock_params, mock_judge, 10, 10)
    assert len(pop.parents) == 0

def test_if_raises_typeerror_on_incorrect_A_param():
    with pytest.raises(TypeError):
        pop = Population(mock_params, mock_judge, '10', 10)

def test_if_raises_typeerror_on_incorrect_B_param():
    with pytest.raises(TypeError):
        pop = Population(mock_params, mock_judge, 10, '10')

def test_if_correctly_pushes_new_phenotype():
    pop = Population(mock_params, mock_judge, 10, 10)
    ph = Phenotype(3)
    pop.push_phenotype(ph)
    assert len(pop.parents) == 1

def test_if_returns_best_phenotype():
	pop = Population(mock_params, mock_judge, 1, 5)
	ph1 = Phenotype(3)
	ph2 = Phenotype(3)
	ph3 = Phenotype(3)
	
	ph1.genes = [True, True, True]
	ph2.genes = [True, False, False]
	ph3.genes = [False, False, False]

	mock_judge.goal_eval(1, 5, ph1)
	mock_judge.goal_eval(1, 5, ph2)
	mock_judge.goal_eval(1, 5, ph3)

	pop.push_phenotype(ph1)
	pop.push_phenotype(ph2)
	pop.push_phenotype(ph3)
	
	assert pop.get_the_best_error() == [True, False, False]

def test_if_creates_next_population_of_given_size():
	pop = Population(mock_params, mock_judge, 1, 5)
	pop.generate_random_population()
	pop.create_next_epoch()
	assert len(pop.parents) == mock_params['mi']
	
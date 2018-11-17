import axios from 'axios'
import endpoint from '../const/endpoint';
import fetchGeneticResponseStart from "./fetchGeneticResponseStart";
import fetchGeneticResponseAck from "./fetchGeneticResponseAck";
import fetchGeneticResponseError from "./fetchGeneticResponseError";

const fetchGeneticResponse = (A, B) => {
	return dispatch => {
		const args = {
			A,
			B
		};
		dispatch(fetchGeneticResponseStart(args));
		axios.get(`${endpoint}/test?A=${A}&B=${B}`)
			.then(response => {
				dispatch(fetchGeneticResponseAck(response))
			})
			.catch(error => dispatch(fetchGeneticResponseError(error)))	
	}
}

export default fetchGeneticResponse;
import axios from 'axios'
import endpoint from '../const/endpoint';
import fetchGeneticResponseStart from "./fetchGeneticResponseStart";
import fetchGeneticResponseAck from "./fetchGeneticResponseAck";
import fetchGeneticResponseError from "./fetchGeneticResponseError";

const fetchGeneticResponse = (A, B) => {
	return dispatch => {
		dispatch(fetchGeneticResponseStart());
		axios.get(`${endpoint}/api/betHistory?A=${A}&=${B}`)
		.then(response => dispatch(fetchGeneticResponseAck(response)))
		.catch(error => dispatch(fetchGeneticResponseError(error)))
	}
}

export default fetchGeneticResponse;
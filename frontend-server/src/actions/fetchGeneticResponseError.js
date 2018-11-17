import {FETCH_GENETIC_RESPONSE_ERROR} from "../const/actionTypes";

const fetchGeneticResponseError = error => {
    return {
        type: FETCH_GENETIC_RESPONSE_ERROR,
        error
    }
}

export default fetchGeneticResponseError;
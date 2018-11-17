import {FETCH_GENETIC_RESPONSE_START} from "../const/actionTypes";

const fetchGeneticResponseStart = error => {
    return {
        type: FETCH_GENETIC_RESPONSE_START,
    }
}

export default fetchGeneticResponseStart;
import {FETCH_GENETIC_RESPONSE_START} from "../const/actionTypes";

const fetchGeneticResponseStart = args => {
    return {
        type: FETCH_GENETIC_RESPONSE_START,
        args
    }
}

export default fetchGeneticResponseStart;
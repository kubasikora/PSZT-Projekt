import {FETCH_GENETIC_RESPONSE_ACK} from "../const/actionTypes";

const fetchGeneticResponseAck = response => {
    return {
        type: FETCH_GENETIC_RESPONSE_ACK,
        payload: response.data
    }
}

export default fetchGeneticResponseAck;
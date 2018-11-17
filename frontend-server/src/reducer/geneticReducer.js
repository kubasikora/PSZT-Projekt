import {
    FETCH_GENETIC_RESPONSE_START,
    FETCH_GENETIC_RESPONSE_ACK,
    FETCH_GENETIC_RESPONSE_ERROR
} from '../const/actionTypes';

const geneticReducer = (state = [], action) => {
    switch(action.type){
        case FETCH_GENETIC_RESPONSE_START:
            return {
                ...state
            }

        case FETCH_GENETIC_RESPONSE_ACK:
            return {
                ...state
            }

        case FETCH_GENETIC_RESPONSE_ERROR:
            return {
                ...state
            }
    
        default:
            return {
                ...state
            }
    }
}

export default geneticReducer;
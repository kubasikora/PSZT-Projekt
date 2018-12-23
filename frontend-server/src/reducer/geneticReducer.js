import {
    FETCH_GENETIC_RESPONSE_START,
    FETCH_GENETIC_RESPONSE_ACK,
    FETCH_GENETIC_RESPONSE_ERROR,
    RESET_ALL_VALUES
} from '../const/actionTypes';


const initialState = {
    fetching: false,
    error: false,
    actualResult: undefined,
    actualArguments: undefined,
    errorMessage: undefined
}

const geneticReducer = (state = initialState, action) => {
    switch(action.type){
        case FETCH_GENETIC_RESPONSE_START:
            return {
                ...state,
                fetching: true,
                actualArguments: action.args
            }

        case FETCH_GENETIC_RESPONSE_ACK:
            return {
                ...state,
                fetching: false,
                actualResult: { A: action.payload.A, B: action.payload.B },
                error: false,
                errorMessage: undefined
            }

        case FETCH_GENETIC_RESPONSE_ERROR:
            return {
                ...state,
                error: true,
                fetching: false,
                errorMessage: action.error
            }

        case RESET_ALL_VALUES:
            return {
                ...state,
                error: false,
                fetching: false,
                errorMessage: undefined,
                actualResult: undefined,
                actualArguments: undefined
            }
    
        default:
            return {
                ...state
            }
    }
}

export default geneticReducer;
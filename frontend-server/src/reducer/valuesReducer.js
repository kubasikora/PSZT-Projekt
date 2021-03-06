import {
    MODIFY_A_VALUE,
    MODIFY_B_VALUE,
    RESET_ALL_VALUES
} from '../const/actionTypes';


const initialState = {
    A_value: 0,
    B_value: 0
}

const valuesReducer = (state = initialState, action) => {
    switch(action.type){
        case MODIFY_A_VALUE:
            return {
                ...state,
                A_value: state.A_value + action.payload.value
            }
        
        case MODIFY_B_VALUE:
            return {
                ...state,
                B_value: state.B_value + action.payload.value
            }

        case RESET_ALL_VALUES:
            return {
                ...state,
                A_value: 0,
                B_value: 0
            }


        default: 
            return {
                ...state
            }
    }
}

export default valuesReducer;
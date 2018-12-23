import { combineReducers } from "redux";
import geneticReducer from "./geneticReducer.js";
import valuesReducer from "./valuesReducer.js";

const reducer = combineReducers({
    genetic: geneticReducer,
    values: valuesReducer
});

export default reducer;



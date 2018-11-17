import { combineReducers } from "redux";
import geneticReducer from "./geneticReducer.js";

const reducer = combineReducers({
    genetic: geneticReducer
});

export default reducer;



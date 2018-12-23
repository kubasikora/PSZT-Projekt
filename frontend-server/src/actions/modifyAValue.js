import { MODIFY_A_VALUE } from "../const/actionTypes";

const modifyAValue = (value) => {
    return {
        type: MODIFY_A_VALUE,
        payload: {
            value
        }
    }
}

export default modifyAValue;
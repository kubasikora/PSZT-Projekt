import { MODIFY_B_VALUE } from "../const/actionTypes";

const modifyBValue = (value) => {
    return {
        type: MODIFY_B_VALUE,
        payload: {
            value
        }
    }
}

export default modifyBValue;
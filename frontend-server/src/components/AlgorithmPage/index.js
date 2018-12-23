import { connect } from 'react-redux';
import AlgorithmPageView from './AlgorithmPageView';
import fetchGeneticResponse from '../../actions/fetchGeneticResponse';
import modifyAValue from '../../actions/modifyAValue';
import modifyBValue from '../../actions/modifyBValue';
import resetAllValues from '../../actions/resetAllValues';

const mapStateToProps = (state, ownProps) => {
    return {
        A_value: state.values.A_value,
        B_value: state.values.B_value,
        lastArguments: state.genetic.actualArguments,
        lastResult: state.genetic.actualResult,
        error: state.genetic.error,
        isFetching: state.genetic.fetching
    }
}


const mapDispatchToProps = dispatch => {
    return {
        fetchGeneticResponse: (A,B) => dispatch(fetchGeneticResponse(A, B)),
        modifyAValue: (value) => dispatch(modifyAValue(value)),
        modifyBValue: (value) => dispatch(modifyBValue(value)),
        resetAllValues: () => dispatch(resetAllValues())
    }
}


const AlgorithmPage = connect(mapStateToProps, mapDispatchToProps)(AlgorithmPageView);

export default AlgorithmPage;
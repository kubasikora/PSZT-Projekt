import { connect } from 'react-redux';
import AlgorithmPageView from './AlgorithmPageView';
import fetchGeneticResponse from '../../actions/fetchGeneticResponse';

const mapStateToProps = (state, ownProps) => {
    return {
        
    }
}


const mapDispatchToProps = dispatch => {
    return {
        fetchGeneticResponse: (A,B) => dispatch(fetchGeneticResponse(A, B))
    }
}


const AlgorithmPage = connect(mapStateToProps, mapDispatchToProps)(AlgorithmPageView);

export default AlgorithmPage;
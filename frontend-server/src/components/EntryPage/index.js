import { connect } from 'react-redux';
import EntryPageView from './EntryPageView';
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


const EntryPage = connect(mapStateToProps, mapDispatchToProps)(EntryPageView);

export default EntryPage;
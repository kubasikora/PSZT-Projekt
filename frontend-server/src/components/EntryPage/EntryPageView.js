import React, { Component } from 'react';


class EntryPageView extends Component {
    constructor(props){
        super(props);
        this.onClickHandler = this.onClickHandler.bind(this);
    }

    onClickHandler() {
        console.log('handling the click...')
        this.props.fetchGeneticResponse(30, 40);
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <img src="./helix.gif" className="App-logo" alt="logo" />
                    <p className="App-text" onClick={this.onClickHandler}>
                        Podstawy Sztucznej Inteligencji
            </p>
                </header>
            </div>
        );
    }
}


export default EntryPageView;
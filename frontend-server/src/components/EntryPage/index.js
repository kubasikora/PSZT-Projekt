import React from 'react';
import { Link, Redirect } from "react-router-dom";


import "./EntryPage.css";

class EntryPage extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            shouldRedirect: false
        }
        this.redirectToHome = this.redirectToHome.bind(this);
    }
    
    componentDidMount(){
        setTimeout(this.redirectToHome, 3000);
    }

    redirectToHome = () => {
        this.setState({shouldRedirect: true});
    }

    render() {
        if(this.state.shouldRedirect) return <Redirect to="/home" />;
        return (
            <div className="transition-item">
                <header className="entry-header">
                    <img src="./helix.gif" className="entry-logo" alt="logo" />
                        <Link to="/home" className="entry-text">
                            Podstawy Sztucznej Inteligencji
                        </Link>
                </header>
            </div>
        );
    }
}


export default EntryPage;

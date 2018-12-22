import React from 'react';
import { Link } from "react-router-dom";

import "./EntryPage.css";

const EntryPage = () => {
    return (
        <div className="transition-item">
            <header className="App-header">
                <img src="./helix.gif" className="App-logo" alt="logo" />
                    <Link to="/home" className="entry-text">
                        Dzień dobry
                    </Link>
            </header>
        </div>
    );
}


export default EntryPage;

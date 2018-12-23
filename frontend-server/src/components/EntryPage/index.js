import React from 'react';
import { Link } from "react-router-dom";

import "./EntryPage.css";

const EntryPage = () => {
    return (
        <div className="transition-item">
            <header className="entry-header">
                <img src="./helix.gif" className="entry-logo" alt="logo" />
                    <Link to="/home" className="entry-text">
                        Dzień dobry
                    </Link>
            </header>
        </div>
    );
}


export default EntryPage;

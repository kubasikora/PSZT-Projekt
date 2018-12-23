import React from 'react';
import { Link, Redirect } from "react-router-dom";


import "./EntryPage.css";

const EntryPage = () => {
    const redirectToHome = () => {
        window.location = "/home";
    }
    setTimeout(redirectToHome, 3000)
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


export default EntryPage;

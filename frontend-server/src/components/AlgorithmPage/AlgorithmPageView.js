import React, { Component } from 'react';
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Divider from "@material-ui/core/Divider";
import CardPicker from "./CardPicker";


import "./AlgorithmPage.css";



class AlgorithmPageView extends Component {
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
            <Grid container spacing={16} className="algorithm-page">
                <Grid item xs={12} className="algorithm-main-section">
                    {/* MAIN CONTENT HERE*/}
                    <Grid container spacing={24} alignItems="center">
                    
                    <Grid item xs={12}>
                        <Typography style={{marginLeft: "50px", marginTop: "15px"}} gutterBottom variant="h2">
                            Genetic Shuffler
                        </Typography>
                    </Grid>

                    <Grid item xs={12}>
                        <Divider variant="middle" />
                    </Grid>

                    <Grid item xs={1} />

                    <Grid item xs={4}>
                        <CardPicker title="Kupka A" content="Podaj sumę na kupce A" />  
                    </Grid>

                    <Grid item xs={2} />

                    <Grid item xs={4}>
                        <CardPicker title="Kupka B" content="Podaj sumę na kupce B" />  
                    </Grid>
                    <Grid item xs={1} />

                    </Grid>
                </Grid>
            </Grid>        
        );
    }
}


export default AlgorithmPageView;

import React, { Component } from 'react';
import Grid from "@material-ui/core/Grid";
import Hidden from "@material-ui/core/Hidden";

import CardPicker from "./CardPicker";
import Header from "./Header";

import "./AlgorithmPage.css";
import { Button } from '@material-ui/core';

class AlgorithmPageView extends Component {
    constructor(props){
        super(props);
        this.sendRequest = this.sendRequest.bind(this);
        this.resetValues = this.resetValues.bind(this);
    }

    sendRequest(){  
        this.props.fetchGeneticResponse(this.props.A_value, this.props.B_value);
    }

    resetValues(){
        this.props.resetAllValues();
    }

    render() {
        return (
            <Grid container spacing={16} className="algorithm-page">
                <Grid item xs={12} className="algorithm-main-section">
                    {/* MAIN CONTENT HERE*/}
                    <Header />
                    <Grid container spacing={16} direction="row" alignItems="center">
                    <Hidden only={["xs", "xl"]}>
                        <Grid item  sm={1} md={1} style={{marginTop: "20vh"}}></Grid>
                    </Hidden>
                    
                    <Grid item xs={12} sm={10} md={5}>
                        <CardPicker 
                         title="Kupka A" 
                         content={this.props.A_value}
                         image="./cards1.jpg" 
                         valueModifier={this.props.modifyAValue}
                        />  
                    </Grid> 
                    <Hidden only={["xs", "md", "lg", "xl"]}>
                        <Grid item sm={1}></Grid>
                    </Hidden>

                    <Hidden only={["xs", "md", "lg", "xl"]}>
                        <Grid item sm={1}></Grid>
                    </Hidden>
                    <Grid item xs={12} sm={10} md={5}>
                        <CardPicker
                         title="Kupka B"
                         content={this.props.B_value}
                         image="./cards2.png"
                         valueModifier={this.props.modifyBValue}
                        />  
                    </Grid>
                    <Hidden only={["xs", "xl"]}>
                        <Grid item sm={1} md={1}></Grid>
                    </Hidden>

                    <Grid container spacing={16} style={{marginTop: "20px", marginBottom: "20px"}}>
                        <Grid item xs={6} container direction="column" alignItems="flex-end">
                            <Button size="large" variant="contained" color="primary" onClick={this.sendRequest}>
                                Znajdź podział!  
                            </Button> 
                        </Grid>
                        <Grid item xs={6}>
                            <Button size="large" variant="outlined" color="primary" onClick={this.resetValues}>
                                Resetuj 
                            </Button>
                        </Grid>
                    </Grid>

                    <Grid container spacing={20} alignItems="center" direction="column" item xs={6}>
                        
                    </Grid>

                    <Grid container spacing={20} alignItems="center" direction="column" item xs={6}>
                        
                    </Grid>


                    </Grid>
                </Grid>
            </Grid>        
        );
    }
}


export default AlgorithmPageView;

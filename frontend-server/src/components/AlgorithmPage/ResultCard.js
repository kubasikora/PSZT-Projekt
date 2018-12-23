import React from 'react';
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import Slide from "@material-ui/core/Slide";

const ResultCard = (props) => {
    const primary = "white";
    const secondary = "#3f51b5"

    let color = props.group === 'A'? primary : secondary;
    let textColor = props.group === 'A'? secondary : primary;

    return (
        <Grid item xs={6} md={1}>
            <Slide direction="left" in={true} mountOnEnter unmountOnExit>
                <Paper style={{minHeight: "100px", minWidth: "60px", backgroundColor: color}}>
                    <Typography variant="h6" style={{marginLeft: "5%", color: textColor}}>
                        {props.value}
                    </Typography>
                    <Typography style={{marginTop: "60%", marginLeft: "60%", color: textColor }} variant="h6">
                        {props.value}
                    </Typography>
                </Paper>
            </Slide>
        </Grid>
    )
}

export default ResultCard;
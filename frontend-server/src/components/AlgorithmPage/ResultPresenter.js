import React, { Fragment } from "react";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";

import ResultCard from "./ResultCard";

const ResultPresenter = (props) => {
    return (
        <Fragment>
            <Grid item xs={12}>
                <Typography style={{ marginLeft: "50px", marginTop: "15px" }} gutterBottom variant="h5">
                    Grupa {props.group}
                </Typography>
            </Grid>

            <Grid container spacing={40} alignItems="center" direction="row">
                {props.result.length === 0 ?    
                    <Typography style={{ marginLeft: "50px", minHeight: "100px", width: "100%" }} align="center" gutterBottom variant="h7">
                        Brak kart
                    </Typography>:
                    props.result.map(el => <ResultCard group={props.group} value={el} />)
                }
            </Grid>
        </Fragment>
    );
}

export default ResultPresenter;
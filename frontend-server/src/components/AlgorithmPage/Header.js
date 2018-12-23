import React, { Fragment } from "react";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";
import Divider from "@material-ui/core/Divider";

const Header = () => {
    return (
    <Fragment>
        <Grid item xs={12}>
            <Typography style={{ marginLeft: "50px", marginTop: "15px" }} gutterBottom variant="h2">
                Genetic Shuffler
            </Typography>
        </Grid>

        <Grid item xs={12}>
            <Divider variant="middle" gutterBottom/>
        </Grid>
        <Grid item xs={12} > &nbsp; </Grid>
    </Fragment>
    );
}

export default Header;
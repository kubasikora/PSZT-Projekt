import React from "react";
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';

const CardPicker = (props) => {

    const addOne = () => {
        props.valueModifier(1);
    }

    const addTen = () => {
        props.valueModifier(10);
    }

    const removeOne = () => {
        props.valueModifier(-1);
    }

    const removeTen = () => {
        props.valueModifier(-10);
    }

    
    return (
        <Card>
            <CardActionArea>
                <CardMedia
                    component="img"
                    alt="Po makale karta stop"
                    height="200"
                    image={props.image}
                    title="Contemplative Reptile"
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="h2">
                        {props.title}
                    </Typography>
                    <Typography component="p">
                        Zadana suma kart na kupce: {props.content}
                    </Typography>
                </CardContent>
            </CardActionArea>
            
            <Grid container spacing={0} direction="column">
                <CardActions>   
                    <Grid container direction="column" alignItems="flex-end" item xs={12} sm={6} md={2}>
                        <Button size="small" variant="contained" color="primary" onClick={addOne}>
                            +1
                        </Button>
                    </Grid>
                    
                    <Grid container direction="column" alignItems="flex-start" item xs={12} sm={6} md={4}>
                        <Button size="small" variant="contained" color="primary" onClick={addTen}>
                            +10
                        </Button>
                    </Grid>
            
                    <Grid container direction="column" alignItems="flex-end" item xs={12} sm={6} md={4}>
                        <Button size="small" variant="outlined" color="primary" onClick={removeOne}>
                            -1   
                        </Button>
                    </Grid>
                
                    <Grid container direction="column" alignItems="flex-start" item xs={12} sm={6} md={2}>
                        <Button size="small" variant="outlined" color="primary" onClick={removeTen}>
                            -10
                        </Button>
                    </Grid>
                
            </CardActions>
            </Grid>
        </Card>
    )
}

export default CardPicker;
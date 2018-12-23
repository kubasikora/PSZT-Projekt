import React from "react";
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const CardPicker = (props) => {
    return (
        <Card>
            <CardActionArea>
                <CardMedia
                component="img"
                alt="Po makale karta stop"
                image="./sk8.jpg"
                title="Contemplative Reptile"
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="h2">
                        {props.title}
                    </Typography>
                    <Typography component="p">
                        {props.content}
                    </Typography>
                </CardContent>
            </CardActionArea>
            
            <CardActions>
                <Button size="small" variant="contained" color="primary">
                    +1
                </Button>

                <Button size="small" variant="contained" color="primary">
                    +10
                </Button>

                <Button size="small" style={{marginLeft: "auto"}} variant="contained" color="secondary">
                    -1
                </Button>

                <Button size="small" variant="contained" color="secondary">
                    -10
                </Button>
            </CardActions>
        </Card>
    )
}

export default CardPicker;
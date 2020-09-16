import React from 'react';
import './App.css';
import axios from 'axios';
import Player from './Player';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';

import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';


import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

function App() {
  const [videos, setVideos] = React.useState([]);
  React.useEffect(() => {
    const fetchData = async () => {
    	const response = await axios.get('/api/videolist');
    	setVideos(response.data);
    }
    
    fetchData();
    
    // 隐藏后不可用，待解决
    setShowPlayer(true);

  }, []);

  
  const [playerVideoUrl, setPlayerVideoUrl] = React.useState([]);
  
  const [showPlayer, setShowPlayer] = React.useState([]);

  function handleClick(url, e) {
    e.preventDefault();
    //console.log("http://192.168.30.55/api/static/media/"+url);
    setPlayerVideoUrl("/api/static/media/"+url);
    setShowPlayer(true);
  }

  const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
      width: 550,
    },
    menuButton: {
      marginRight: theme.spacing(2),
    },
    title: {
      flexGrow: 1,
    },
  }));
  const classes = useStyles();

  return (
      <Container maxWidth="sm" >            
        <AppBar position="static">
          <Toolbar>
            <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" className={classes.title}>
              听视频
            </Typography>
            <Player url={playerVideoUrl} isShow={showPlayer} />
          </Toolbar>
        </AppBar>
        <Grid >        
          {videos.map(video =>    
            <Card className={classes.root}>
              <CardActionArea>
                <CardMedia
                  component="img"
                  alt={video.videoTitle}
                  height="140"
                  image={video.videoThumbnail}
                  title={video.videoTitle}
                />
                <CardContent onClick={handleClick.bind(this, video.videoFile)}>
                  <Typography gutterBottom variant="h5" component="h2">
                  {video.videoTitle}
                  </Typography>
                  <Typography variant="body2" color="textSecondary" component="p">
                    {video.videoDescription}
                  </Typography>
                </CardContent>
              </CardActionArea>
              <CardActions>
                <Button size="small" color="secondary">
                  删除
                </Button>
                <Button size="small" color="primary"  onClick={handleClick.bind(this, video.videoFile)}>
                  播放
                </Button>
              </CardActions>
            </Card>
          )}          

        </Grid>
      </Container>
    
  );
}

export default App;

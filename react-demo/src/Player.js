import React from 'react';

function Player(props) {
  const isShow = props.isShow;
  if (isShow) {
    return (
      <div>
          <audio autoPlay="autoplay" 
                controls="controls"
                preload="auto"
                controlsList="nodownload"
                src={props.url}
                >
          </audio>
      </div>
    );
  }

}

export default Player;


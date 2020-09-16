import React from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [videoLists, setVideoLists] = React.useState([]);
  React.useEffect(() => {
    const fetchData = async () => {
    	const response = await axios.get('/api/videolist');
    	setRepos(response.data);
    }
    
    fetchData();
  }, []);

  return (
    <div className="App">
      <ul>
         {repos.map(repo =>
            <li key={repo.id}>{repo.videoTitle}</li>
          )}
      </ul>
    </div>
  );
}

export default App;

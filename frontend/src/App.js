import './App.css';
import {useState, useEffect} from 'react';
import UsecaseList from './components/UsecaseList';

function App() {

  const [usecases,setUsecases] = useState([])
  const [editedUsecase,setEditUsecase] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5000/get',{
      'method':'GET',
      headers: {
        'Content-Type':'application/json'
      }
    })
    .then(resp => resp.json())
    .then(resp => setUsecases(resp))
    .catch(error => console.log(error))
  },[])

  const editUsecase = (usecase) => {
    setEditUsecase(usecase)
  }
  
  return (
    <div className="App">
      <h1>Fast and ReactJS CRUD application</h1>

        <UsecaseList usecases = {usecases}/>
    </div>
  );
}

export default App;

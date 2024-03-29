// import { useEffect, useState } from 'react';
import './App.css';
import { useGarfield } from './components/api';

function App() {
  const {data, loading} = useGarfield();

  return (
    <>
    <div>
      {loading && <div>Loading...</div>}
      {!loading && <div>
          <img src={data.data} />
        </div>
      }
    </div>
    </>
  )
}

export default App

import { useEffect, useState } from "react";
import axios from "axios"


function App() {
  
  const [matches, setData] = useState([]) 
  const [second, setSecond] = useState()
  useEffect(()=>{
    get_data()
  }, [])
  async function get_data()
  {
    await axios.get('cricket/inquire/',
		{ 
      headers: {    
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*' 
      },
    }
  )
    .then((res)=>{
      setData(res.data)
    })
    .catch((err)=>console.log(err))
  }
  const changeSecond = (event) =>{
    setSecond(event.target.value);
  }
  async function change_interval()
  {
    await axios.post('cricket/inquire/',
		{ 
      headers: {    
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*' 
      },
      data : second
    }
    )
    .then((res)=>{
      console.log(res)
    })
    .catch((err)=>console.log(err))
  }


  return (
    
    <div>
      <div className="flex-box">
      <button onClick={get_data}>조회</button>
      <input type="number"
            onChange={changeSecond}></input> <button onClick={change_interval}>시간변경</button>
      </div>
      <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">First</th>
                  <th scope="col">Last</th>
                  <th scope="col">Handle</th>
                </tr>
              </thead>
              <tbody>
      {
        matches.length === 0 ? null : matches.map((res, i)=>
        {
          return (
              <tr>
                <th scope="row">{i}</th>
                <td>{res.title}</td>
                <td>{res.start_date}</td>
                <td>{res.start_date}</td>
              </tr>  
          )
        })
      }
      </tbody>
      </table>
    </div>
  );
}

export default App;

import { useEffect, useState } from "react";
import axios from "axios"
import CustomizedTables from "./components/table_box"
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
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
      <div style={{ display:"flex", flexWrap:"wrap", justifyContent:"space-between", marginBottom: "20px"}}>
      <Button variant="contained" onClick={get_data}>조회</Button>
      <TextField
          id="outlined-number"
          label="Number"
          type="number"
          InputLabelProps={{
            shrink: true,
          }}
          onChange={changeSecond}
        /> <Button variant="contained" color="secondary" onClick={change_interval}>시간변경</Button>
      </div>
      {
        matches.length === 0 ? null : <CustomizedTables rows={matches}/>
      }
    </div>
  );
}

export default App;

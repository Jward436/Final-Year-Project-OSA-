import './App.css';
import * as React from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';






function App() {
  return (
    <div className="App">
      
      <FormControl>
  <FormLabel id="demo-radio-buttons-group-label">Sex</FormLabel>
  <RadioGroup
    aria-labelledby="demo-radio-buttons-group-label"
    defaultValue=""
    name="radio-buttons-group"
  >
    <FormControlLabel value="F" control={<Radio />} label="Female" />
    <FormControlLabel value="M" control={<Radio />} label="Male" />
    <FormControlLabel value="" control={<Radio />} label="Any" />
  </RadioGroup>
</FormControl>
<FormControl>
  <FormLabel id="demo-radio-buttons-group-label">Smoker</FormLabel>
  <RadioGroup
    aria-labelledby="demo-radio-buttons-group-label"
    defaultValue=""
    name="radio-buttons-group"
  >
    <FormControlLabel value="yes" control={<Radio />} label="Smoker" />
    <FormControlLabel value="no" control={<Radio />} label="Non-smoker" />
    <FormControlLabel value="" control={<Radio />} label="Any" />
  </RadioGroup>
</FormControl>




    </div>
  );
}

export default App;


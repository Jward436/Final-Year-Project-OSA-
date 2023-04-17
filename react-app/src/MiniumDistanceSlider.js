import './MiniumDistanceSlider.css';
import * as React from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';
import { Grid, Typography } from '@mui/material';

function valuetext(value) {
  return `${value}`;
}

const minDistance = 1;

export default function MinimumDistanceSlider() {
  const [value1, setValue1] = React.useState([0, 100]);

  const handleChange1 = (event, newValue, activeThumb) => {
    if (!Array.isArray(newValue)) {
      return;
    }

    if (activeThumb === 0) {
      setValue1([Math.min(newValue[0], value1[1] - minDistance), value1[1]]);
    } else {
      setValue1([value1[0], Math.max(newValue[1], value1[0] + minDistance)]);
    }
  };

  const [value2, setValue2] = React.useState([10, 70]);

  const handleChange2 = (event, newValue, activeThumb) => {
    if (!Array.isArray(newValue)) {
      return;
    }

    if (newValue[1] - newValue[0] < minDistance) {
      if (activeThumb === 0) {
        const clamped = Math.min(newValue[0], 100 - minDistance);
        setValue2([clamped, clamped + minDistance]);
      } else {
        const clamped = Math.max(newValue[1], minDistance);
        setValue2([clamped - minDistance, clamped]);
      }
    } else {
      setValue2(newValue);
    }

  };

  return (
 
    <>
    <Grid container sx={{display: 'fixed',  justifyContent:'center', alignItems:'center', paddingTop:'1%'}}spacing={2} columns={100}>
        <Grid item xs = {15}>
             <Box sx={{ width: 300 }}>
                <Typography sx = {{ textAlign: 'center', marginBottom:'12%'}}>Age</Typography>
                 <Slider
                 getAriaLabel={() => 'Age Slider'}
                 value={value1}
                 onChange={handleChange1}
                 valueLabelDisplay ="on"
                 getAriaValueText={valuetext}
                 disableSwap
             />
            </Box>
        </Grid>
        
        <Grid item xs = {1}/>

        <Grid item xs = {15}>
            
            <Box sx={{ width: 300 }}>
            <Typography sx = {{ textAlign: 'center', marginBottom:'12%'}}>BMI</Typography>
                <Slider
                    getAriaLabel={() => 'BMI Slider'}
                    value={value2}
                    onChange={handleChange2}
                    getAriaValueText={valuetext}
                    valueLabelDisplay="on"
                    disableSwap
                  />
                  
            </Box>
        </Grid>
    </Grid>
    </>
   
  );
}

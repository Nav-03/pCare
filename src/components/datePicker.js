import * as React from "react";
import TextField from "@mui/material/TextField";

export const DatePicker = () => {
  // const [value, setValue] = React.useState(new Date("2014-08-18T21:11:54"));

  // const handleChange = (newValue) => {
  //   setValue(newValue);
  // };

  return (
    <div>
      <TextField
        id="datetime-local"
        label="Next appointment"
        type="datetime-local"
        defaultValue="2017-05-24T10:30"
        sx={{ width: 250 }}
        InputLabelProps={{
          shrink: true,
        }}
      />
    </div>
  );
};

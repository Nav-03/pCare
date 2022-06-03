import "../src/css/App.css";
import { MedicationTable } from "../src/components/medicationTable.js";
import { AppointmentsTable } from "../src/components/appointmentsTable.js";
import { NavBar } from "./components/navBar.js";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";

function App() {
  return (
    <>
      <Box
        sx={{ flexGrow: 1 }}
        className="App"
        style={{
          justifyContent: "space-around",
          flexDirection: "row",
          margin: 5,
        }}
      >
        <NavBar />
        <Grid container spacing={6}>
          <Grid item xs={12} sm={6}>
            <MedicationTable />
          </Grid>
          <Grid item xs={12} sm={6}>
            <AppointmentsTable />
          </Grid>
        </Grid>
      </Box>
    </>
  );
}

export default App;

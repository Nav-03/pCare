import * as React from "react";
import { DataGrid } from "@mui/x-data-grid";
import {
  randomCreatedDate,
  randomTraderName,
  randomUpdatedDate,
} from "@mui/x-data-grid-generator";
// import { red } from "@mui/material/colors";
// import { ThemeProvider, createTheme } from "@mui/material/styles";

const columns = [
  {
    field: "Perscription",
    headerName: "Perscription",
    width: 180,
    editable: true,
  },
  {
    field: "Doze",
    headerName: "Dosage",
    type: "number",
    width: 80,
    editable: true,
  },
  {
    field: "dateCreated",
    headerName: "Next Dosage",
    type: "dateTime",
    width: 180,
    editable: true,
  },
  {
    field: "lastLogin",
    headerName: "Last Dosage",
    type: "dateTime",
    width: 180,
    editable: true,
  },
];

const rows = [
  {
    id: 1,
    Perscription: randomTraderName(),
    Doze: 25,
    dateCreated: randomCreatedDate(),
    lastLogin: randomUpdatedDate(),
  },
  {
    id: 2,
    Perscription: randomTraderName(),
    Doze: 36,
    dateCreated: randomCreatedDate(),
    lastLogin: randomUpdatedDate(),
  },
  {
    id: 3,
    Perscription: randomTraderName(),
    Doze: 19,
    dateCreated: randomCreatedDate(),
    lastLogin: randomUpdatedDate(),
  },
  {
    id: 4,
    Perscription: randomTraderName(),
    Doze: 28,
    dateCreated: randomCreatedDate(),
    lastLogin: randomUpdatedDate(),
  },
  {
    id: 5,
    Perscription: randomTraderName(),
    Doze: 23,
    dateCreated: randomCreatedDate(),
    lastLogin: randomUpdatedDate(),
  },
];
// const theme = createTheme({
//   palette: {
//     primary: {
//       main: "#1976d2",
//     },
//   },
// });

export const MedicationTable = () => {
  return (
    // <ThemeProvider theme={theme}>
    <div style={{ height: 350, width: "100%" }}>
      Medications
      <DataGrid rows={rows} columns={columns} />
    </div>
    // </ThemeProvider>
  );
};

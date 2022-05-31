import * as React from "react";
import { DataGrid } from "@mui/x-data-grid";
import {
  randomCreatedDate,
  randomTraderName,
  randomUpdatedDate,
} from "@mui/x-data-grid-generator";

export const MedicationTable = () => {
  return (
    <div style={{ height: 300, width: "50%" }}>
      <DataGrid rows={rows} columns={columns} />
    </div>
  );
};

const columns = [
  {
    field: "Perscription",
    headerName: "Perscription",
    width: 220,
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
    width: 220,
    editable: true,
  },
  {
    field: "lastLogin",
    headerName: "Last Dosage",
    type: "dateTime",
    width: 220,
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

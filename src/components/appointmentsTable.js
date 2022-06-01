import * as React from "react";
import { DataGrid } from "@mui/x-data-grid";
import {
  randomCreatedDate,
  randomTraderName,
  randomAddress,
  randomPhoneNumber,
} from "@mui/x-data-grid-generator";

export const AppointmentsTable = () => {
  return (
    <div style={{ height: 350, width: "100%" }}>
      <DataGrid rows={rows} columns={columns} />
    </div>
  );
};

const columns = [
  {
    field: "doctor",
    headerName: "Doctor",
    width: 140,
    editable: true,
  },
  {
    field: "phonenumber",
    headerName: "Phone Number",
    width: 140,
    editable: true,
  },
  {
    field: "date",
    headerName: "Date",
    type: "dateTime",
    width: 180,
    editable: true,
  },
  {
    field: "address",
    headerName: "Address",
    width: 220,
    editable: true,
  },
];

const rows = [
  {
    id: 1,
    doctor: randomTraderName(),
    phonenumber: randomPhoneNumber(),
    date: randomCreatedDate(),
    address: randomAddress(),
  },
  {
    id: 2,
    doctor: randomTraderName(),
    phonenumber: randomPhoneNumber(),
    date: randomCreatedDate(),
    address: randomAddress(),
  },
  {
    id: 3,
    doctor: randomTraderName(),
    phonenumber: randomPhoneNumber(),
    date: randomCreatedDate(),
    address: randomAddress(),
  },
  {
    id: 4,
    doctor: randomTraderName(),
    phonenumber: randomPhoneNumber(),
    date: randomCreatedDate(),
    address: randomAddress(),
  },
  {
    id: 5,
    doctor: randomTraderName(),
    phonenumber: randomPhoneNumber(),
    date: randomCreatedDate(),
    address: randomAddress(),
  },
];

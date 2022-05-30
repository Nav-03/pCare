import "../src/css/App.css";
import { DatePicker } from "../src/components/datePicker.js";
import { MedicationTable } from "../src/components/medicationTable.js";

function App() {
  return (
    <div className="App">
      <MedicationTable />
      <DatePicker />
    </div>
  );
}

export default App;

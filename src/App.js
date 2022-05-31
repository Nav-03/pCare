import "../src/css/App.css";
import { MedicationTable } from "../src/components/medicationTable.js";
import { NavBar } from "./components/navBar.js";

function App() {
  return (
    <div className="App">
      <NavBar />
      <div>
        <MedicationTable />
      </div>
    </div>
  );
}

export default App;

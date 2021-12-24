import {
  Routes,
  Route
} from "react-router-dom";
import Home from "./pages/Home";
import Prayerscreen from "./pages/Prayerscreen";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/prayerscreen" element={<Prayerscreen />} />
    </Routes>
  );
}

export default App;

import Header from "./Header";
import EmployeeCard from "./EmployeeCard";
import Footer from "./Footer";

function App() {
  return (
    <>
      <Header />

      <EmployeeCard
        name="Aswin"
        role="Flutter Developer"
        department="Mobile Team"
      />

      <EmployeeCard
        name="Priya"
        role="UI/UX Designer"
        department="Design Team"
      />

      <EmployeeCard
        name="Arun"
        role="Frontend Developer"
        department="Web Team"
      />

      <Footer />
    </>
  );
}

export default App;
function EmployeeCard(props) {
  return (
    <div className="card">
      <h2>{props.name}</h2>
      <p>Role: {props.role}</p>
      <p>Department: {props.department}</p>
    </div>
  );
}

export default EmployeeCard;
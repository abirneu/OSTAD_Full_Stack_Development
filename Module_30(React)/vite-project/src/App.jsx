import React from "react";
const App = () => {
  
  const submitData =(event) =>{
    event.preventDefault();
    //do the work
    alert("ok")

  }
  return(
    <div>
      <form onSubmit={submitData}>
        <input type="text"  placeholder="write here"/>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};
export default App;










import React from "react";

const App = () => {
  const user = {isAdmin : true}
  return(
    <div>
      <p>Hello</p>
      {user.isAdmin ? <p>You are admin</p>: <p>you are user</p>}
    </div>
  )
  
    


     

  
};

export default App;










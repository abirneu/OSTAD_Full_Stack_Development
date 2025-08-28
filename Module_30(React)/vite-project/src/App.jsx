import React from "react";

const App = () => {
  // const user = {isAdmin : true}
  // return(
  //   <div>
  //     <p>Hello abir</p>
  //     {user.isAdmin ? <p>You are admin</p>: <p>you are user</p>}
  //   </div>
  // )
  const isLoggedIn = true
  return(
    <div>
      <p>Hello</p>
      {isLoggedIn && <h1>Welcome Back</h1>}
    </div>
  )
  
    
};

export default App;










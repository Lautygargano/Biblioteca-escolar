import { useContext } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthContext } from "./context/AuthContext";
import Libreria from "./libreria/libreria";
import Login from "./pages/login";
function App() {

  const { currentUser } = useContext(AuthContext);

  const RequireAuth = ({ children }) => {
    return currentUser ? children : <Navigate to="/login" />;
  };

  return (
    <div className={"app"}>
        <BrowserRouter>
          <Routes>
            <Route
              path="/"
              element={currentUser ? <Navigate to="/libreria" /> : <Navigate to="/login" />}
            />
            <Route path="/login" element={<Login />} />
            <Route
              path="/libreria"
              element={
                <RequireAuth>
                  <Libreria />
                </RequireAuth>
              }
            />
            <Route />
          </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
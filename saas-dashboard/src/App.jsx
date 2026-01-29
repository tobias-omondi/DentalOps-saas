// APP COMPONENT
import { createBrowserRouter } from "react-router"
import { RouterProvider } from "react-router-dom"

// IMPORTING PAGES AND COMPONETS
import Overview from "./components/Pages/Overview"
import Dashboard from "./components/MainDashboard/Dashboard"
import LogIn from "./components/Pages/LogIn"
import LogOut from "./components/Pages/LogOut"
import ClinicPage from "./components/Pages/ClinicPage"
import PatientPage from "./components/Pages/PatientPage"
import RootLayout from "./components/Layoults/RootLayout"
import DashboardLayout from "./components/Layoults/DashboardLayout"


function App() {

  const router = createBrowserRouter([
    {
      path: "/", // ROOT LAYOUT
      Component: RootLayout,
      children :[
        {index: true, Component: Overview},
        {path: "overview", Component: Overview},
        {path: "login", Component: LogIn},
        {path: "clinic/:clinicid", Component: ClinicPage},
        {path: "patient/:patientid", Component: PatientPage},
        {path: "dashboard", Component: DashboardLayout, children: [
          {index: true, Component: Dashboard},
        {path: "logout", Component: LogOut},
       
        ]},
      ]
    },
  ])
  
  return (
    <>
    <RouterProvider router={router} />
    </>
  )
}

export default App

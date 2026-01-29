import React from 'react'
import { Link } from 'react-router'

const SideNavbar = () => {
  return (
    <div className='bg-blue-500'>
      <Link to="/"> Overview</Link>
      <Link to= "/clinic/:clinicid" > Clinic</Link>
      <Link to= "/Patient/:patientid" > Patient</Link>
      <Link to="/Login" > Login</Link>
      <Link to= "/Logout">Logout</Link>
    </div>
  )
}

export default SideNavbar

import React from 'react'
import SideNavbar from '../Navbarpage/SideNavbar'
import { Outlet } from 'react-router'

const DashboardLayout = () => {
  return (
    <div>
      <SideNavbar />
      <main p-6>
        <Outlet />
      </main>
    </div>
  )
}

export default DashboardLayout

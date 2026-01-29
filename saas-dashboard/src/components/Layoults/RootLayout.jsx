import React from 'react'
import SideNavbar from '../Navbarpage/SideNavbar'
import { Outlet } from 'react-router'

const RootLaults = () => {
  return (
    <div>
      <SideNavbar />
      <main className='p-5'>
        <Outlet />
      </main>
    </div>
  )
}

export default RootLaults

import React from 'react'
import PropTypes from 'prop-types'
import { container, navContainer, link } from './styles.css'
import { Link } from 'react-router-dom'

function Links () {
  return (
    <ul>
      <li><Link className={link} to='/'>{'Home'}</Link></li>
      <li><Link className={link} to='/feed'>{'Feed'}</Link></li>
    </ul>
  )
}

export default function Navigation ({isAuthed}) {
  return (
    <div className={container}>
      <nav className={navContainer}>
        <Links />
      </nav>
    </div>
  )
}

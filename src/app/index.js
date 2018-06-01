import React from 'react'
import ReactDOM from 'react-dom'
import getRoutes from './config/routes'

function checkAuth() {
  return true
}

ReactDOM.render(
  getRoutes(checkAuth),
  document.getElementById('app')
)

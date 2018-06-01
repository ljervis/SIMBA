import React from 'react'
import PropTypes from 'prop-types'
import * as styles from './styles.css'
import { errorMsg } from 'sharedStyles/styles.css'

function displayJson(object) {
  return <pre>{JSON.stringify(object, null, ' ')}</pre>
}

Feed.propTypes = {
  text: PropTypes.string.isRequired
}

export default function Feed (props) {
  return (
    <div>
      {displayJson(props.text)}
    </div>
  )
}

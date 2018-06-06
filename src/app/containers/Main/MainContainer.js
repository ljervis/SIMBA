import React from 'react'
import PropTypes from 'prop-types'
import { container, innerContainer } from './styles.css'
import { Navigation } from 'components'

class MainContainer extends React.Component {
  constructor(props) {
    super(props)
  }
  static contextTypes = {
    router: PropTypes.object.isRequired,
  }
  render() {
    return (
      <div className={container}>
        <Navigation />
        <div className={innerContainer}>
          {this.props.children}
        </div>
      </div>
    )
  }
}

export default MainContainer

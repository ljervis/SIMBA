import React from 'react'
import PropTypes from 'prop-types'
import { Feed } from 'components'
import { PromptContainer } from 'containers'

class FeedContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      text: 'Hello World!'
    }
  }
  render () {
    return (
      <PromptContainer />
    )
  }
}

export default FeedContainer

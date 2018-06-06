import React from 'react'
import PropTypes from 'prop-types'
import { Prompt } from 'components'
import { sendSpeechDataToBackend } from 'helpers/api'
import { serverUrl } from 'config/constants'

function displayJson(object) {
  return (
    <pre>
      {JSON.stringify(object, null, ' ')}
    </pre>
  )
}

function isValidFormatNum(val) {
  const numInputData = Number(val)

  if (isNaN(numInputData)) {
    return false
  }
  if (!val.includes(".")) {
    return true
  }
  const splitNum = val.split(".")
  if (splitNum.length != 2) {
    return false
  }
  if (splitNum[1].length != 2) {
    return false
  }
  return true
}

class PromptContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      donationAmount: '',
      isMatchingDonations: false,
      isDollarMatching: false,
      isDonorMatching: false,
      dollarMultiplier: 1,
      perDonorDonation: 0,
      maxDonationAmount: 0,
      response: {}
    }
    this.handleSubmitData = this.handleSubmitData.bind(this)
    this.handleUpdateData = this.handleUpdateData.bind(this)
  }

  handleUpdateData(e) {
    if (e.target.type === 'checkbox') {
      this.setState({
        [e.target.name]: e.target.checked
      })
    } else {
      this.setState({
        [e.target.name]: e.target.value
      })
    }
  }

  handleSubmitData(e) {
    e.preventDefault()

    const formData = this.state

    // if (!isValidFormatNum(inputData)) {
    //   this.setState({
    //     response: {
    //       'Error': 'Input value not valid format (eg: 100.55)'
    //     }
    //   })
    //   return
    // } else {
    //   this.setState({
    //     response: {
    //       'Success': 'Input is valid'
    //     }
    //   })
    // }

    // const numInputData = Number(inputData) * 100

    console.log('sent data', formData)

    sendSpeechDataToBackend(formData)
      .then((response) => {
        console.log('Sent request.')
        console.log(response)
        this.setState({
          response: response.data
        })
      })
      .catch((err) => {
  			console.log(err)
  			this.setState({
  				response: {
            'ERROR': 'Invalid symbols found in input string. Try removing obscure symbols or retyping symbols such as apostrophes, commas, and quotes.' }
  			})
  		})
  }



  render () {
    console.log('State:', this.state)
    return (
      <div>
        <Prompt
          isMatchingDonations={this.state.isMatchingDonations}
          isDollarMatching={this.state.isDollarMatching}
          isDonorMatching={this.state.isDonorMatching}
          onSubmitData={this.handleSubmitData}
          onUpdateData={this.handleUpdateData}
        />
        { displayJson(this.state.response) }
      </div>
    )
  }
}

export default PromptContainer

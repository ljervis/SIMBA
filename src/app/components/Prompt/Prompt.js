import React from 'react'
import PropTypes from 'prop-types'
import { submitTicketBtn, newTicketInput, newTicketInputSmallContainer } from './styles.css'
import { center, largeHeader } from 'sharedStyles/styles.css'

Prompt.propTypes = {
  onSubmitData: PropTypes.func.isRequired,
  onUpdateData: PropTypes.func.isRequired,
  isMatchingDonations: PropTypes.bool.isRequired,
  isDollarMatching: PropTypes.bool.isRequired,
  isDonorMatching: PropTypes.bool.isRequired,
}

export default function Prompt (props) {
  return (
    <div className={center}>
      <div>
        <form onSubmit={props.onSubmitData}>
          <div className={newTicketInputSmallContainer}>
          <input
            placeholder="donationAmount"
            name={"donationAmount"}
            onChange={props.onUpdateData}
            className={newTicketInput}
            type="text"/>
            <input
              placeholder="dollarMultiplier"
              name={"dollarMultiplier"}
              onChange={props.onUpdateData}
              className={newTicketInput}
              type="number"/>
            <input
              placeholder="perDonorDonation"
              name={"perDonorDonation"}
              onChange={props.onUpdateData}
              className={newTicketInput}
              type="number"/>
            <input
              placeholder="maxDonationAmount"
              name={"maxDonationAmount"}
              onChange={props.onUpdateData}
              className={newTicketInput}
              type="number"/>

            
            <input
              placeholder="isMatchingDonations"
              label="isMatchingDonations"
              name={"isMatchingDonations"}
              checked={props.isMatchingDonations}
              onChange={props.onUpdateData}
              className={newTicketInput}
              type="checkbox"/>

            <input
              label="isDollarMatching"
              placeholder="isDollarMatching"
              name={"isDollarMatching"}
              checked={props.isDollarMatching}
              onChange={props.onUpdateData}
              className={newTicketInput}
              type="checkbox"/>

            <input
              label="isDonorMatching"
              placeholder="isDonorMatching"
              name={"isDonorMatching"}
              checked={props.isDonorMatching}
              onChange={props.onUpdateData}
              className={newTicketInput}
              type="checkbox"/>
          </div>
          <div className={center}>
            <button
              className={submitTicketBtn}
              type="submit">
                Send
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

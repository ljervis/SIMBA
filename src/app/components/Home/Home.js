import React from 'react'
import PropTypes from 'prop-types'
import FontAwesome from 'react-fontawesome'
import { container, title, slogan } from './styles.css'
import { submitTicketBtn, stopRecordingBtn, newTicketInput, newTicketInputSmallContainer } from './styles.css'
import { center, largeHeader } from 'sharedStyles/styles.css'

export default function Home (props) {
  return (
    <div className={container}>
      <p className={title}>{'SIMBA'}</p>
      <p className={slogan}>{props.displayText}</p>
      <p className={slogan}>Sentiment Score: {props.sentimentScore}</p>
      <form onSubmit={props.onStartRecording}>
        <div className={center}>
          <button
            className={submitTicketBtn}
            type="submit">
              Start Recording
          </button>
        </div>
      </form>
      <form onSubmit={props.onStopRecording}>
        <div>
          <button
            className={stopRecordingBtn}
            type="submit">
              Stop Recording
          </button>
        </div>
      </form>
      {
        props.isRecording
          ? <div>
              <FontAwesome
                name='microphone'
                size='4x'
                style={{marginTop: '15px'}}
              />
            </div>
          : <div>
              <FontAwesome
                name='microphone-slash'
                size='4x'
                style={{marginTop: '15px'}}
              />
            </div>
      }
    </div>
  )
}

Home.propTypes = {
  isRecording: PropTypes.bool.isRequired,
  displayText: PropTypes.string.isRequired,
  onStartRecording: PropTypes.func.isRequired,
  onStopRecording: PropTypes.func.isRequired,
  sentimentScore: PropTypes.number.isRequired,
}

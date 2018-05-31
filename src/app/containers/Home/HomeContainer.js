import React from 'react'
import { sendSpeechDataToBackend } from 'helpers/api'
import { Home } from 'components'

class HomeContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      displayText: 'How are you feeling today?',
      sentimentScore: 0.0,
      recording: false
    }
    this.recognition = new webkitSpeechRecognition()
    this.handleStartRecording = this.handleStartRecording.bind(this)
    this.startRecording = this.startRecording.bind(this)
    this.handleStopRecording = this.handleStopRecording.bind(this)
  }

  startRecording() {
    this.recognition.continuous = true;   // Suitable for dictation.
    this.recognition.interimResults = true;  // If we want to start receiving results even if they are not final.
    this.recognition.lang = "en-US";
    this.recognition.maxAlternatives = 1; // Since from our experience, the highest result is really the best...

    this.recognition.onstart = () => {
      this.setState({
        recording: true
      })
      console.log("starting..")
    }

    this.recognition.onend = () => {
      console.log("ending..")
    }

    this.recognition.onresult = (event) => { // the event holds the results
      console.log("result found")
      if (typeof(event.results) === 'undefined') { // Something is wrong…
          this.setState({
            displayText: 'Something went wrong',
            recording: false
          })
          this.recognition.stop();
          return;
      }

      for (var i = event.resultIndex; i < event.results.length; ++i) {
          if (event.results[i].isFinal) { //Final results
              console.log("final results: " + event.results[i][0].transcript);   //Of course – here is the place to do useful things with the results.
          } else {   //i.e. interim...
              console.log("interim results: " + event.results[i][0].transcript);  //You can use these results to give the user near real time experience.
          }
          this.setState({
            displayText: event.results[i][0].transcript
          })

      }
    }
    this.recognition.start()
  }

  handleStopRecording(e) {
    e.preventDefault()
    this.setState({
      recording: false
    })
    this.recognition.stop()
    const formData = {
      'inputString': this.state.displayText
    }
    sendSpeechDataToBackend(formData)
      .then((response) => {
        console.log('Sent request.')
        console.log(response)
        this.setState({
          sentimentScore: response.data['sentiment_score']
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

  handleStartRecording(e) {
    e.preventDefault()
    if (!('webkitSpeechRecognition' in window)) {
      this.setState({
        displayText: 'Webkit speech recognition not supported',
        recording: true
      })
    } else {
      this.startRecording()
    }
  }

  render () {
    return (
      <Home
        displayText={this.state.displayText}
        onStartRecording={this.handleStartRecording}
        onStopRecording={this.handleStopRecording}
        isRecording={this.state.recording}
        sentimentScore={this.state.sentimentScore}
      />
    )
  }
}

export default HomeContainer

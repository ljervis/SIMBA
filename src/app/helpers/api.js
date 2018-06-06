import axios from 'axios'
import { serverUrl } from 'config/constants'

export function sendSpeechDataToBackend(formData) {
  return axios({
    method: 'post',
    url: `${serverUrl}/api/process`,
    data: formData
  })
}

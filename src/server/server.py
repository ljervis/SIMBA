from flask import Flask, request, jsonify
import random, string, json
import os, time
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/api/hash', methods=['GET'])
def create_hash():
  print 'Creating new hash code..'
  hash_code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
  print 'Created new hash code: %s' % hash_code

  return jsonify(hash_code)

@app.route('/api/donate', methods=['POST'])
def donate():
    input_data = json_loads_byteified(json.dumps(request.get_json(), ensure_ascii=False))

    print input_data
    print type(input_data)

    print 'reading file'
    json_file = open("data.json", "rw")
    backend_data = json_load_byteified(json_file)

    if input_data['isMatchingDonations'] == True:
        donor_name = "donor" + str(len(backend_data['donors']) + 1)
        matching_types = []
        if input_data['isDollarMatching'] == True:
            matching_types.append('DOLLAR')
        if input_data['isDonorMatching'] == True:
            matching_types.append('DONOR')
        backend_data['donors'][donor_name] = {
            "totalDonated": 0,
            "isMatchingDonations": input_data['isMatchingDonations'],
            "donationMatchingTypes": matching_types, # DOLLAR, DONOR, NONE
            "maxAmountMatching": input_data['maxDonationAmount'],
            "dollarMultiplier": input_data['dollarMultiplier'],
            "perDonorDonation": input_data['perDonorDonation']
        }

        with open('data.json', 'w') as outfile:
            json.dump(backend_data, outfile)

        return jsonify(backend_data)

    amount_donated = int(input_data['donationAmount']) * 100

    print 'adding to donors'
    count = 0
    for donor in backend_data['donors']:
        count = count + 1
        curr_donor = backend_data['donors'][donor]
        is_matching_donations = curr_donor['isMatchingDonations']
        total_currently_donated = int(curr_donor['totalDonated'])
        dollar_multiplier = int(curr_donor['dollarMultiplier'])
        per_donor_donation = int(curr_donor['perDonorDonation'])
        donors_max_amount = int(curr_donor['maxAmountMatching'])
        donation_matching_types = curr_donor['donationMatchingTypes']
        if is_matching_donations and len(donation_matching_types) != 0:
            total_amount_to_be_donated = 0
            for i in range(0, len(donation_matching_types)):
                donation_type = donation_matching_types[i]
                if donation_type == "DOLLAR":
                    total_amount_to_be_donated = total_amount_to_be_donated + (amount_donated * dollar_multiplier)
                elif donation_type == "DONOR":
                    total_amount_to_be_donated = total_amount_to_be_donated + per_donor_donation
                else:
                    return error_message('Invalid donation type found.')

            total_amount_to_be_donated = total_amount_to_be_donated + total_currently_donated

            if total_amount_to_be_donated >= donors_max_amount:
                backend_data['donors'][donor]['totalDonated'] = donors_max_amount
            else:
                backend_data['donors'][donor]['totalDonated'] = total_amount_to_be_donated

    donor_num = str(count + 1)
    backend_data['donors']['donor' + donor_num] = {
        "totalDonated": amount_donated,
        "isMatchingDonations": False,
        "donationMatchingTypes": [], # DOLLAR, DONOR, NONE
        "maxAmountMatching": -1, # Not Matching
        "dollarMultiplier": 1,
        "perDonorDonation": 0
    }

    with open('data.json', 'w') as outfile:
        json.dump(backend_data, outfile)

    print 'process complete'
    return jsonify(backend_data)

@app.route('/api/process', methods=['POST'])
def process_string():
  try:
    json_body = json_loads_byteified(json.dumps(request.get_json(), ensure_ascii=False))
  except:
    return error_message('Unable to convert json in request body to readable format.')

  if json_body is None:
    return error_message('No valid json found in request body.')

  if json_body['inputString'] is None:
    return error_message('inputString not found in request body.')

  input_string = json_body['inputString']

  if input_string == '':
    return error_message('inputString is empty.')

  print 'Input: ' + input_string

  blob = TextBlob(input_string)
  POS_tags = blob.tags
  first_word = POS_tags[0]

  output_data = {
    'sentiment_score': blob.sentiment.polarity,
    'subjectivity_score': blob.sentiment.subjectivity,
    'is_verb': first_word[1][:2] == 'VB'
  }

  print 'Output: '
  print output_data

  return jsonify(output_data)

def error_message(message):
  return jsonify({
    'error_message': message
    }
  )

def json_load_byteified(file_handle):
    return byteify(
        json.load(file_handle, object_hook=byteify),
        ignore_dicts=True
    )

def json_loads_byteified(json_text):
    return byteify(
        json.loads(json_text, object_hook=byteify),
        ignore_dicts=True
    )


def byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            byteify(key, ignore_dicts=True): byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

if __name__ == "__main__":
  app.run()

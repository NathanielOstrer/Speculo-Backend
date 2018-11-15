from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

# required for all twilio access tokens
account_sid = 'AC1be40ce267a78f2d47549d8864a8f3e6'
api_key = 'SK670f5fa86e1f6b8a949591b3789f1593'
api_secret = 'gQxx6pdJZU4g48s9682iHGM3nRB1wOlK'

identity = 'alice'

# Create access token with credentials
token = AccessToken(account_sid, api_key, api_secret, identity=identity)

# Create a Video grant and add to token
video_grant = VideoGrant(room='TestRoom')
token.add_grant(video_grant)

# Return token info as JSON
print(token.to_jwt())

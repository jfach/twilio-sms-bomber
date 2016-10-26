# Twilio SMS Bomber

## Setup

```shell
export twilio_bomb_sid=TWILIO_ACCOUNT_SID
export twilio_bomb_token=TWILIO_AUTH_TOKEN
export twilio_bomb_number=TWILIO_NUMBER
```

## Execution

The arguments are formatted as follows:

```shell
python bomb.py recipient_number "message" messages_to_send
```
for example...
```shell
python bomb.py +15551239999 "Hello world!" 100
```

```py
# THIS IS A COMMENT
# Format: method:url:payload:header
# Set "NONE" to disable payload or header

# Example -> React to message on discord:
PUT|https://discord.com/api/v9/channels/997090855213088841/messages/997493217324969984/reactions/%E2%9C%85/%40me?location=Message|NONE|{"accept": "*/*","accept-language": "fr,fr-FR;q=0.9","authorization": "your_token","content-type": "application/json","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","x-debug-options": "bugReporterEnabled","x-discord-locale": "en-US","x-fingerprint": "997469677376765992.qhJS-tPeI3HjyIoKMSQcUAP3WTY","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDA1Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDQiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2OTIxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}

# Example -> Send message on discord:
POST|https://discord.com/api/v9/channels/997090855213088841/messages|{"content":"THIS MESSAGE WAS SENT BY PMX LANG"}|{"accept": "*/*","accept-language": "fr,fr-FR;q=0.9","authorization": "your_token","content-type": "application/json","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","x-debug-options": "bugReporterEnabled","x-discord-locale": "en-US","x-fingerprint": "997469677376765992.qhJS-tPeI3HjyIoKMSQcUAP3WTY","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDA1Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDQiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2OTIxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}
```

ForeverErnarBot
================
Telegram bot for Forever Living (Ernar).
Includes bilingual start menu, PDF catalog selection, registration/referral link and WhatsApp contact.

Files:
- main.py
- requirements.txt

Deploy on Render.com:
1. Create GitHub repo and push these files.
2. On Render, create a Web Service and connect the repo.
3. Set Environment variable BOT_TOKEN to your bot token.
4. Start command: python main.py

Local run:
  pip install -r requirements.txt
  BOT_TOKEN=<token> python main.py

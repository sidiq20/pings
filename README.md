# Render App Pinger (GitHub Actions)

Keeps your Render app awake by pinging it every 5 minutes using GitHub Actions and Python.

## URL

Currently pinging: https://creativehunt.onrender.com

## How It Works

This repo uses a GitHub Actions cron job (`ping.yml`) to send a GET request every 5 minutes.

No external service needed.

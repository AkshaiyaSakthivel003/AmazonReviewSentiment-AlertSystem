#  Amazon Review Sentiment & Alert System

A smart monitoring pipeline to extract, analyze, and alert on customer sentiment from Amazon product reviews.


## Purpose

Designed for Amazon FBA sellers to:

- Detect product defects early through negative review spikes.
- Gather feature requests and improvement ideas from real users.
- Compare reviews of top competing ASINs.
- Send alerts via Slack or Email and store insights in Google Sheets or Airtable.


## Features

- ASIN-based review scraping (yours & competitors)
- Sentiment classification using OpenAI or VADER
- Topic/complaint clustering
- Spike detection for defect alerts
- Monthly product feedback digest
- Output to Google Sheet or Airtable
- Slack/email notifications


## Project Structure

amazon_review_alert/
├── main.py                (Entry point for pipeline)
├── analyze.py             (LLM/VADER-based sentiment & topic extractor)
├── fetch_reviews.py       (Scrapes reviews using Amazon Product API or HTML parser)
├── utils.py               (Helper functions (e.g., deduplication, formatting)
├── alert.py               (Alert system (Slack/email/webhook))
├── store.py               (Google Sheets/Airtable writer)
├── requirements.txt
├── .env                   (API keys & configuration)
└── README.md


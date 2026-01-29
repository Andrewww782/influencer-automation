# Influencer Outreach Automation (Python + Playwright)

## Overview
This project demonstrates an end-to-end automation pipeline for outreach operations.
It simulates real-world influencer marketing workflows by automating profile data extraction
and preparing it for outreach and tracking.

## What This Does
- Scrapes public profile-style listing pages using Playwright
- Extracts name, profile URL, and metadata
- Stores structured data in CSV format
- Designed for integration with email automation tools (n8n / Zapier)

## Tech Stack
- Python
- Playwright
- Pandas
- Git & GitHub

## How to Run Locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
python scraper/scrape_profiles.py

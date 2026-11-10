1.	Project Overview
This project is an automated Python tool that creates a Spotify playlist containing the Billboard Hot 100 songs from a specific date in history.
It combines web scraping, API integration, and automation to turn a music lover’s nostalgia into a ready-to-play playlist.
Intermediate+ Create a Spotify Playlist using the Musical Time Machine.

2.	Features
•	Scrape Billboard Hot 100: Get the top 100 songs from any date.
•	Spotify Authentication: Securely log in using Spotify’s API.
•	Song Matching: Search Spotify for the scraped Billboard tracks.
•	Playlist Creation: Automatically create a new Spotify playlist.
•	Bulk Add Tracks: Add all found songs in one go.

3.	Tech Stack
•	Language: Python 3.x
•	Libraries:
o	requests – HTTP requests for scraping
o	BeautifulSoup – HTML parsing for Billboard Hot 100
o	spotipy – Spotify Web API Python client
o	dotenv – Environment variable management

4.	How It Works
Scraping Billboard Hot 100
•	Takes a date input in the format YYYY-MM-DD.
•	Fetches Billboard’s Hot 100 chart for that date.
Spotify Authentication
•	Uses OAuth 2.0 with spotipy to connect to your Spotify account.
•	Requires SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, and SPOTIPY_REDIRECT_URI in .env.
 Search Songs on Spotify
•	Searches each scraped track on Spotify.
•	Skips songs that are not found, while logging missing tracks.
Create Playlist & Add Songs
•	Creates a playlist named

5.	Learning Outcomes
•	Web Scraping with BeautifulSoup.
•	OAuth 2.0 Authentication with Spotify API.
•	Automating playlist creation and track addition.
•	Data cleaning & handling missing items during automation.
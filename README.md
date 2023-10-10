# Podcast-Transcription-Data-Pipeline-with-Airflow
Episodes Airflow built data pipeline that can download and store podcast episodes using Apache Airflow, a powerful and widely used data engineering tool.
Podcast Transcription Data Pipeline with Airflow
This project demonstrates the creation of a data pipeline using Apache Airflow to download podcast episodes, transcribe them using speech recognition, and store the results in a SQLite database. The pipeline can be scheduled to run daily, and tasks are designed to run independently with error logs. Additionally, the project is designed for easy extension, allowing for the addition of speech recognition, summaries, and more using Airflow.

**Table of Contents**
-  Project Description
-  Prerequisites
-  Getting Started
-  Usage
-  Contributing
-  License
**Table of Contents**
- Introduction
- Project Steps
- Local Setup
- Installation
- Data
- File Overview
- Usage
- Contributing 

# Introduction
The goal of this project is to create a data pipeline using Airflow to automate the transcription of podcast episodes. The pipeline consists of several steps, including downloading podcast metadata, creating a SQLite database to store the metadata, downloading podcast audio files, and transcribing the audio using the Vosk speech recognition library.

# Project Steps
Download Podcast Metadata and Parse XML: Download the podcast metadata in XML format and parse it to extract necessary information.

Create SQLite Database: Set up a SQLite database to store the podcast metadata.

Download Podcast Audio Files: Utilize requests to download the podcast audio files.

Transcribe Audio Files using Vosk: Use Vosk to transcribe the podcast audio files.

# Local Setup
Installation
Ensure you have the following installed locally:

Airflow 2.3+
Python 3.8+
Python packages:
pandas
sqlite3
xmltodict
requests
vosk
pydub
Refer to the Airflow documentation for instructions on installation.

# Data
During this project, data such as podcast metadata, language models for Vosk, and podcast episodes will be downloaded as needed. Please refer to the link_to_data for more information.

# File Overview
podcast_summary.py: Contains the code to create the data pipeline.
steps.md: Provides a description of the steps needed to complete the project.
Usage
To use this project, follow the steps outlined in steps.md to create and run the data pipeline using Airflow.

# Contributing
We welcome contributions! Feel free to fork this repository, make your changes, and submit a pull request. Please ensure to follow our contribution guidelines.

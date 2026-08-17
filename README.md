 SyntecxHub News Aggregator CLI

A Python command-line application that fetches the latest news articles from online sources, filters and organizes the results, and displays them directly in the terminal.

This project was developed as part of the SyntecxHub Python Programming Internship.

 Project Overview

The SyntecxHub News Aggregator CLI provides a simple way to search for and view news articles from the command line.

The application is designed to demonstrate practical Python programming skills, including:

* Command-line interface development
* Working with APIs
* HTTP requests
* JSON data processing
* Data filtering
* Error handling
* Logging
* Python virtual environments
* Project organization
* Git and GitHub version control

Features

* Search for news articles using keywords
* Display article titles
* Display article descriptions
* Display publication dates
* Display article sources
* Display article URLs
* Limit the number of displayed articles
* Handle API and network errors
* Provide clear command-line error messages
* Use environment variables for API credentials
* Log application activity and errors

Technologies Used

* Python 3
* Requests
* Python-dotenv
* News API
* argparse
* logging
* Git
* GitHub

 Project Structure

```text
Syntecxhub_News_Aggregator_CLI/
|
+-- .venv/
|
+-- src/
|   +-- __init__.py
|   +-- main.py
|   +-- news_api.py
|
+-- logs/
|   +-- app.log
|
+-- .env
+-- .gitignore
+-- requirements.txt
+-- README.md
```

Requirements

Before running the project, make sure Python 3 is installed.

Check your Python version:

```powershell
python --version
```

The project also requires an API key from News API.

 Installation

1. Clone the repository

```powershell
git clone https://github.com/Sbhombolozi/Syntecxhub_News_Aggregator_CLI.git
```

Move into the project directory:

```powershell
cd Syntecxhub_News_Aggregator_CLI
```

2. Create a virtual environment

```powershell
python -m venv .venv
```

3. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the terminal should display:

```text
(.venv)
```

 4. Install dependencies

```powershell
pip install -r requirements.txt
```

If pip does not work directly, use:

```powershell
python -m pip install -r requirements.txt
```

API Configuration

The application requires a News API key.

Create a file named:

```text
.env
```

in the project root directory.

Add your API key:

```env
NEWS_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual News API key.

Do not publish your API key to GitHub.

The `.env` file should be included in `.gitignore`.

Example:

```text
.env
.venv/
__pycache__/
*.pyc
logs/
```

 Running the Application

From the project root directory, run:

```powershell
python -m src.main
```

You can also provide a search keyword.

Example:

```powershell
python -m src.main --query technology
```

Another example:

```powershell
python -m src.main --query cybersecurity
```

 Command-Line Options

The application supports command-line arguments.

 Search for news

```powershell
python -m src.main --query artificial intelligence
```

 Limit the number of results

```powershell
python -m src.main --query cybersecurity --limit 5
```

 Display help

```powershell
python -m src.main --help
```

The help command displays the available arguments and usage instructions.

 Example Output

```text
========================================
        SYNTECXHUB NEWS AGGREGATOR
========================================

Search: cybersecurity

1. New Cybersecurity Developments
   Source: Example News
   Published: 2026-08-17
   Description: Latest developments in cybersecurity...
   URL: https://example.com/article

2. Security Industry Updates
   Source: Example News
   Published: 2026-08-17
   Description: New developments in the information security industry...
   URL: https://example.com/article
```

 Error Handling

The application handles common errors, including:

* Missing API key
* Invalid API key
* Network connection failures
* API request failures
* Invalid API responses
* Empty search results
* Unexpected application errors

Users receive readable error messages instead of application crashes whenever possible.

 Logging

Application activity and errors can be recorded in:

```text
logs/app.log
```

Logging helps with troubleshooting and monitoring application behavior.


 Security

Sensitive credentials are stored using environment variables rather than being hard-coded into the source code.

The API key is stored in:

```text
.env
```

The `.env` file should never be committed to GitHub.


 Git and GitHub

The project uses Git for version control.

Initialize Git if required:

```powershell
git init
```

Add project files:

```powershell
git add .
```

Create a commit:

```powershell
git commit -m "Complete SyntecxHub News Aggregator CLI"
```

Add the GitHub repository:

```powershell
git remote add origin https://github.com/Sbhombolozi/Syntecxhub_News_Aggregator_CLI.git
```

Push the project:

```powershell
git branch -M main
git push -u origin main
```

Learning Objectives

This project demonstrates practical experience with:

1. Python application development
2. CLI application design
3. REST API integration
4. HTTP requests
5. JSON processing
6. Environment variables
7. Exception handling
8. Logging
9. Virtual environments
10. Git and GitHub
11. Project documentation

 Future Improvements

Possible future improvements include:

* Add support for multiple news providers
* Add category-based filtering
* Add country filtering
* Add date-range filtering
* Add sorting by publication date
* Export news results to CSV
* Export news results to JSON
* Add colored terminal output
* Add pagination
* Add automated tests
* Add caching
* Add a configuration file
* Package the application for easier installation

 Internship Project

This project was created for the SyntecxHub Python Programming Internship.

The objective is to demonstrate the ability to design, develop, test, document, and publish a practical Python command-line application.

 Author

Sbhombolozi

GitHub:

https://github.com/Sbhombolozi

 License

This project is intended for educational and internship purposes.

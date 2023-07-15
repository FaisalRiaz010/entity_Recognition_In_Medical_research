# Entity-Recognition-In-Medical-Research-Website-
**Description**
Welcome to the Flask Medical Entity Search project! This project is the result of our final year project, designed to demonstrate the use of Flask to create a web application that allows users to search and explore medical articles published between 2000 and 2022. The application utilizes Natural Language Processing (NLP) to extract medical entities from the articles' abstracts and presents the information in an interactive and user-friendly manner.

**Features**
Show the total number of articles published between 2000 and 2022 in a bar chart.
Click on each year in the bar chart to display article titles published in that particular year.
View the number of total articles and authors corresponding to the selected year.
Access the backend model "last" to extract medical entities from article abstracts.
Medical entities extracted include Drug, Agents, Treatment, Cell, Enzyme, Micro-organism, Nucleic Acid, Amino Acid, ORG, Date, Person, Percentage, etc.
Medical entities are color-coded and labeled based on their corresponding abstract context.
Users can perform a search for specific medical terms, but they must log in or register an account to access this feature.
Researchers can access the search option using a pay offer.
Simple users have 10 free searches before being prompted to pay for additional searches.
Search results display tagged and labeled entities, similar to the entities shown on the article details page.
Users can log out of their accounts, and a "Forgot Password" option is available for account recovery.

**How to Run**
Ensure you have Python installed on your system (Python 3.6 or higher).
Clone this repository to your local machine.
Navigate to the project's root directory.

use to run
$ cd Flask_Medical_Entity_Search

Install the required dependencies using pip.

$ pip install -r requirements.txt

Ensure you have MongoDB installed on your system.
Run the MongoDB server.

$ mongod

Run the Flask web application.

$ python MYFlask.py
Access the application in your web browser by visiting http://127.0.0.1:5000/.

**Technologies Used**
Flask: Python-based web framework.
HTML, CSS, and JavaScript: Front-end development.
Natural Language Processing (NLP): To extract medical entities from article abstracts.
Chart.js: To create interactive bar charts.
MongoDB: As the database to store user information and other data.
Directory Structure
Flaskpy.py: The main Python file containing the Flask application code.
templates/: Contains all HTML templates used in the project.
static/: Contains CSS and JavaScript files for front-end styling and functionality.

**Future Improvements**
This project is a starting point, and there are several ways to improve it:

Enhance the NLP model for more accurate medical entity extraction.
Implement user roles and permissions for better access control.
Add pagination for the article titles and search results to handle large datasets efficiently.
Provide more options for data visualization and exploration, such as word clouds or network graphs.
Improve security measures, such as implementing HTTPS and using secure authentication practices.

**Contributing**
We welcome contributions to this project. If you find any issues or have ideas for improvements, feel free to submit a pull request or open an issue on the GitHub repository.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

Thank you for checking out our Flask Medical Entity Search project! We hope you find it useful and informative. If you have any questions or feedback, please don't hesitate to contact us.

**Happy searching!**

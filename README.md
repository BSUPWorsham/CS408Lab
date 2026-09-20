Project: 04.01 Mini Lab Warmup
Description:
The Rest API allows us to access different data points within Canvas. We can attach a token and it
Lets us log in and access things like courses, assignments, due dates, and so much more.

Setup Instructions:
Open a new project in your chosen IDE, then in the terminal type
git clone https://github.com/BSUPWorsham/CS408Lab.git
Then you will need to install dependencies
Do this by typing in the terminal:
    pip install python-dotenv
    pip install requests

Then you need to create a .env file with this structure:
CANVAS_API_TOKEN=your_api_token_here
SCHOOL="https://boisestatecanvas.instructure.com/api/v1"

Then once all of that is added you should be able to run the program.

API Endpoints: Get courses which returns an array of JSON course objects. We can go through
the courses and use Get assignments and that gives us an array of JSON assignment objects from the
specified course ID.

I really enjoyed this lab warmup as it was very similar to the internship I did this summer. I got 
to work with Rest API's for the first time this summer and I really enjoyed it so working with a 
new one that has data that relates to me was cool. If I had more time I would love to make my output
a UI, in the terminal it is pretty ugly but it could look really good with some html.








# Diet Recommendation based on BMI and Multiple Diseases

### Description
This project focuses on designing a diet recommendation system that suggests the most suitable diet plan to help individuals stay healthy and happy. The system operates in two main stages.

In the first stage, the system recommends a diet based on personal attributes such as height, weight, age, gender, and physical activity level. In the second stage, it provides disease-specific diet recommendations tailored to individuals suffering from particular health conditions. For the current implementation, the system focuses on three diseases — heart disease, liver disease, and diabetes.

The model is developed using machine learning techniques implemented in Python, leveraging its powerful statistical and mathematical computation capabilities. The process begins with user input, which is used to calculate the Body Mass Index (BMI) through trained machine learning models. Based on this, an appropriate diet plan is recommended. Similarly, for disease-specific recommendations, the system employs specialized algorithms to generate suitable diets and corresponding recipes.

This approach aims to deliver accurate and efficient diet suggestions, improving upon previous systems that suffered from issues like the cold start problem, which negatively affected their performance. By integrating optimized algorithms and refined methods within the region of interest (ROI), the proposed system enhances overall accuracy and effectiveness in personalized diet recommendation.

### Architecture
Here the front end was done by Stream lit. Streamlit is an open source app framework in Python language. It helps to create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc. For our case the front-end is composed of three web pages. The main page is Hello.py which is a welcoming page used to introduce you to project. The side bar on the left allows the user to navigate too the automatic diet recommendation page and the custom food recommendation page. In the diet recommendation page the user can fill information about his age, weight, height.. and gets a diet recommendation based on his information. Besides, the custom food recommendation allows the user to specify more his food preference using nutritional values.   
Back end is built using the FastAPI framework, which allows for the creation of fast and efficient web When a user makes a request to the API (user data, nutrition data...) the model is used to generate 
a list of recommended food similar/suitable to his request (data) which are then returned to the user via the API.
APIs. When a user makes a request to the API (user data, nutrition data...) the model is used to generate 
a list of recommended food similar/suitable to his request (data) which are then returned to the user 
via the API.

✅ Core Tools / Interpreter
python (install from python.org or via package manager)
✅ Web Frameworks & Servers
fastapi – for building APIs
uvicorn – ASGI server to run FastAPI apps
✅ Machine Learning & Data Science Libraries
scikit-learn (or sklearn) – machine learning
pandas – data manipulation and analysis
numpy – numerical computing
✅ Web Applications & Visualization
streamlit – to build data science web apps
streamlit-echarts (optional, if using ECharts integration) – for interactive charts
✅ Web Scraping
beautifulsoup4 – Beautiful Soup library for parsing HTML/XML
lxml (optional, parser dependency for Beautiful Soup)
html5lib (optional, another parser for Beautiful Soup)

### Results 


<img width="557" height="356" alt="image" src="https://github.com/user-attachments/assets/b2fe03ed-c625-4a29-bc4b-236d9895cdbe" />

<img width="614" height="353" alt="image" src="https://github.com/user-attachments/assets/d5b5f735-a027-41ea-93b4-509c7eb58120" />

<img width="583" height="333" alt="image" src="https://github.com/user-attachments/assets/1ab93fae-9667-46c6-b755-12b30c4cc92a" />

<img width="567" height="390" alt="image" src="https://github.com/user-attachments/assets/bc4fc819-7eb6-493f-8061-71980e4455a5" />

This was a Collaborative Project done along with my friends :) 



import streamlit as st

def load_home_page_content():
    return st.markdown("""
<!-- Container (Project Section) -->
<div id="project" class="container-fluid">
  <div class="row">
    <div class="col-sm-12">
      <h4>This project is initiated by the Omdena New Delhi, India Chapter to solve Real World Problems.</h4>
      <h2>Project background</h2>
      According to the latest AQI report, Delhi is the second most polluted city on this planet. The respirable suspended particulate matter (RSPM) in the New Delhi's air is touching 250 micrograms per cubic meter ((μg/m3), four times the prescribed level, while the concentration of nitrogen oxide (NOx) is 50-55 μg/m3 - way above the permissible upper limit of 40μg/m3.
As a result, the pollution level in Delhi today is as bad as it was in the pre-CNG days, exposing residents to serious health problems such as respiratory and pulmonary diseases.
High Respiratory Symptoms have been noted in 32% of children examined in Delhi compared to only 18.2% of rural Children. The Symptoms are higher during winter.
Lung function has reduced in 43.5 percent of schoolchildren, and deficit hyperactivity disorder is 4.1 times higher among schoolchildren of Delhi than in the rest of India.
The city's poor quality air damages irreversibly the lungs of 2.2 million or 50 percent of all children.

<h3> The problem </h3>
Cough is a common symptom of many respiratory diseases, including COVID-19, which has become a global pandemic. Identifying the severity of a cough can aid in diagnosing and managing respiratory illnesses. This project aims to create a website that uses machine learning models to analyze cough through audio and provide an analysis of cough severity. The website will also provide recommendations based on the severity of the cough.
According to our research, as there is no web portal available to the public for this aid as of now in India, the website can aid in early detection of respiratory illnesses, including COVID-19, which has become a global pandemic. With the website, people can easily record and upload their cough audio, and the machine learning model can provide an analysis of the severity of the cough. This can help people identify the severity of their symptoms and seek medical attention promptly, reducing the spread of the disease.
Secondly, the website can provide recommendations based on the severity of the cough. The recommendations can range from self-care measures to seeking medical attention. This can help people manage their symptoms effectively and prevent the development of complications.

<h3> Project goals </h3>
The goals of this project are: 
<ul><li>Understand the processing of audio data for machine learning.</li>
<li>Use machine learning to predict cough severity.</li>
<li>Deploy models and provide APIs that process the data and give final predictions on the website.</li></ul> 
    </div>
  </div>
</div>

<!-- Container (Team Section) -->
<div id="team" class="container-fluid text-center">
  <h2>About Team</h2>
  <table class="table table-bordered">
            <thead><tr><th scope="col">Chapter Name</th><th scope="col">Lead Name</th></tr></thead>
          <tbody><tr><td scope="row">New Delhi, India Chapter Leads</td>
          <td>Dharvi Kumra</td></tr></tbody>
          </table>
          <br>
          <table class="table table-striped">
<thead><tr><th scope="col">Task Name</th><th scope="col">Task Lead</th><th scope="col">Active Contributors</th></tr></thead>
         <tbody>
         <tr><td scope="row">Knowledge</td><td></td><td></td></tr>
          <tr><td scope="row">Data Collection</td><td></td><td></td></tr>
          <tr><td scope="row">Exploratory Data Analysis (EDA)</td><td></td><td></td></tr>
          <tr><td scope="row">Data Preprocessing</td><td></td><td></td></tr>
          <tr><td scope="row">Model Development</td><td></td><td></td></tr>
          <tr><td scope="row">Model Deployment API Creation</td><td>Arya Adesh, Vinod</td><td>-</td></tr>
          <tr><td scope="row">Web Portal Creation</td><td></td><td></td></tr>
          <tr><td scope="row">Making the Web Portal Live</td><td>Vinod</td><td>-</td></tr>
         </tbody>
         </table>
</div>

<!-- Container (Data Source Section) -->
<div id="datasource" class="container-fluid text-center bg-grey">
  <h2>Data Source</h2>
<h3>Data Source Information Section. here. Maybe in a table format or paragraph</h3>
</div>

<!-- Container (Cough Diagnosis Section) -->
<div id="coughdiagnosis" class="container-fluid bg-grey">
  <h2 class="text-center">Cough Diagnosis</h2>
</div>
"""
,unsafe_allow_html=True)

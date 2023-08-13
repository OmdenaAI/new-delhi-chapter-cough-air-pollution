import streamlit as st

def load_home_page_content():
    return st.markdown("""
<!-- Container (Project Section) -->
<div id="project" class="container-fluid">
  <div class="row">
    <div class="col-sm-12">
      <h2>This project is initiated by the Omdena New Delhi, India Chapter to solve Real World Problems.</h2>
      <h2>Project background</h2>
      <p>According to the latest AQI report, Delhi is the second most polluted city on this planet. The respirable suspended particulate matter (RSPM) in the New Delhi's air is touching 250 micrograms per cubic meter ((μg/m3), four times the prescribed level, while the concentration of nitrogen oxide (NOx) is 50-55 μg/m3 - way above the permissible upper limit of 40μg/m3.
As a result, the pollution level in Delhi today is as bad as it was in the pre-CNG days, exposing residents to serious health problems such as respiratory and pulmonary diseases.
High Respiratory Symptoms have been noted in 32% of children examined in Delhi compared to only 18.2% of rural Children. The Symptoms are higher during winter.
Lung function has reduced in 43.5 percent of schoolchildren, and deficit hyperactivity disorder is 4.1 times higher among schoolchildren of Delhi than in the rest of India.
The city's poor quality air damages irreversibly the lungs of 2.2 million or 50 percent of all children.</p>

<h3> The Project's Problem to solve and Goals to achieve</h3>
<p>Cough is a common symptom of many respiratory diseases, including COVID-19, which has become a global pandemic. Identifying the severity of a cough can aid in diagnosing and managing respiratory illnesses. This project aims to create a website that uses machine learning models to analyze cough through audio and provide an analysis of cough severity. The website will also provide recommendations based on the severity of the cough.
According to our research, as there is no web portal available to the public for this aid as of now in India, the website can aid in early detection of respiratory illnesses, including COVID-19, which has become a global pandemic. With the website, people can easily record and upload their cough audio, and the machine learning model can provide an analysis of the severity of the cough. This can help people identify the severity of their symptoms and seek medical attention promptly, reducing the spread of the disease.
Secondly, the website can provide recommendations based on the severity of the cough. The recommendations can range from self-care measures to seeking medical attention. This can help people manage their symptoms effectively and prevent the development of complications.</p>

<ul><li><p>Understand the processing of audio data for machine learning.</p></li>
<li><p>Use machine learning to predict cough severity.</p></li>
<li><p>Deploy models and provide APIs that process the data and give final predictions on the website.</p></li></ul> 
    </div>
  </div>
</div>
<hr>
<!-- Container (Team Section) -->
<div id="team" class="container-fluid">
  <h2>Team</h2>
  <table class="table table-bordered">
            <thead><tr><th scope="col">Chapter Name</th><th scope="col">Lead Name</th></tr></thead>
          <tbody><tr><td scope="row">New Delhi, India Chapter Leads</td>
          <td>Dharvi Kumra</td></tr></tbody>
          </table>
          <br>
          <table class="table">
<thead><tr><th scope="col">Task Name</th><th scope="col">Task Lead</th><th scope="col">Active Contributors</th></tr></thead>
         <tbody>
         <tr><td scope="row">Knowledge</td><td>Eishani Bhattacharya,  Anushka Singh,Param Barodia </td><td>Param Barodia, Eishani Bhattacharya, Neelakshi Joshi, Nick Kobets</td></tr>
          <tr><td scope="row">Data Collection</td><td>Debadrita Dey, Kaif Ashraf</td><td>-</td></tr>
          <tr><td scope="row">Exploratory Data Analysis (EDA)</td><td>Neelakshi Joshi, Shubham Naik</td><td>Neelakshi Joshi, Kartik Goel</td></tr>
          <tr><td scope="row">Data Preprocessing</td><td>Neelakshi Joshi, Shubham Naik, Sankalp Gilda </td><td>Neelakshi Joshi</td></tr>
          <tr><td scope="row">Model Development</td><td>Pankaj Tiwari, Zuhail, Shibendra Bhattacharjee</td><td>Shibendra Bhattacharjee, Dharvi</td></tr>
          <tr><td scope="row">Model Deployment API Creation</td><td>Arya Adesh, Vinod Cherian</td><td>Vinod Cherian, Souvik Roy</td></tr>
          <tr><td scope="row">Web Portal Creation</td><td>Harshita, Arya Adesh</td><td>Harshita, Vinod Cherian, Souvik Roy</td></tr>
          <tr><td scope="row">Making the Web Portal Live</td><td>Vinod Cherian</td><td>Vinod Cherian, Souvik Roy</td></tr>
         </tbody>
         </table>
</div>
<hr>
<!-- Container (Data Source Section) -->
<div id="datasource" class="container-fluid bg-black">
 <br/>
 <h2>Data Source</h2>
 <h3>Dataset Name: COUGHVID</h3>
  The COUGHVID dataset provides over 20,000 crowdsourced cough recordings representing a wide range of subject ages, genders, geographic locations, and COVID-19 statuses.     
 <h3>Data access</h3>
  The COUGHVID dataset can be downloaded from the following Zenodo link: https://doi.org/10.5281/zenodo.4048311
 <br/>
 <h3>Citation</h3>
  When using this resource, please cite the following publication:
   Orlandic, L., Teijeiro, T. & Atienza, D. The COUGHVID crowdsourcing dataset, a corpus for the study of large-scale cough analysis algorithms. *Sci Data* 8, 156 (2021). https://doi.org/10.1038/s41597-021-00937-4
 <br/>
 <h3>Contact</h3>
  For questions or suggestions, please contact coughvid@epfl.ch
  To donate a COVID-19 cough sound to our database, please visit https://coughvid.epfl.ch/
</div>
<hr>
<!-- Container (Cough Diagnosis Section) -->
<div id="coughdiagnosis" class="container-fluid bg-black">
  <h2 class="text-center">Cough Diagnosis</h2>
        This website helps you to identifying the severity of a cough which can aid in diagnosing and managing respiratory illnesses by seeking medical attention promptly.
Please click the button below to upload your cough audio in order to identify the severity of cough.               
</div>
"""
,unsafe_allow_html=True)

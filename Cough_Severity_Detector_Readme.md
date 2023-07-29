# Cough Severity Detection

This project aims to detect the severity of cough sounds to aid early diagnosis of respiratory illnesses.

## Background

- Air pollution in Delhi causing spike in respiratory diseases 
- Early detection through cough analysis can improve outcomes
- Lack of easily accessible cough screening solutions  

## Our Solution  

- Developed ML models to classify cough severity from audio
- Built web app allowing users to record and analyze coughs
- Models categorize cough severity as mild, moderate or severe 
- Provides results and recommendations to user

## Web Application

- Built using Streamlit for model integration and easy audio uploads
- Hosted on Streamlit Cloud for public access: https://impact-airpollution-cough-audio.streamlit.app/#coughdiagnosis

## Datasets

- [ESC-50](https://github.com/karolpiczak/ESC-50): Environmental audio for cough detection
- [Respiratory Sounds DB](https://www.kaggle.com/vbookshelf/respiratory-sound-database): Audio labeled with respiratory diseases mapped to severity 

## Models 

- Extra Trees Classifier for cough detection
- LightGBM for multi-class cough severity rating

## Results

- Cough detection accuracy: 73.33%  
- Cough severity classification accuracy: 91.30%

## Future Work 

- Expand labeled cough audio datasets
- Experiment with deep learning models 
- Add more features to web app
- Scale up deployment 

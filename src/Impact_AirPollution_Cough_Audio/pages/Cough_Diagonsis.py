import streamlit as st
#from streamlit_toggle import st_toggle_switch
#from audiorecorder import audiorecorder
import librosa, glob, os, lightgbm
import numpy as np
import pandas as pd
from project_utils.menu import load_menu_html, load_css
from project_utils.cough_analysis_helper import load_all_models, features_extractor, detect_cough_from_model, detect_cough_severity_from_model
from tempfile import TemporaryDirectory
from pathlib import Path

#model6
DETECT_COUGH_MODEL_PATH = './Model/cough_detection_model.pkl'
#model5
COUGH_SEVERITY_MODEL_PATH = './Model/respiratory_db_lightgbm_model.joblib'
TEMPORARY_FILE_NAME='cough_audio.wav'

COUGH_TYPE = {0: 'Wind', 1: 'Breathing', 2: 'Coughing', 3: 'Snoring', 4: 'Sneezing'}
SEVERITY_TYPE = ['healthy', 'mild', 'moderate', 'severe']

if 'toggleswitchkey' not in st.session_state:
  st.session_state.toggleswitchkey = ''
if 'audio_sr' not in st.session_state:
  st.session_state.audio_sr = ''
if 'audio_file' not in st.session_state:
  st.session_state.audio_file = ''

@st.cache_resource
def model_load(detect_cough_model_path, cough_severity_model_path):
   detect_cough_model, cough_severity_model = load_all_models(detect_cough_model_path, cough_severity_model_path)
   return detect_cough_model,cough_severity_model

def detect_cough(model, mfcc, mels, zcr, sc, sr):
    prediction_result = detect_cough_from_model(model, mfcc, mels, zcr, sc, sr)
    #st.write(list(prediction_result))
    return prediction_result[0]

def detect_cough_severity(model, mfcc, mels, zcr, sc, sr, audio_sr, audio_file):
    prediction_result = detect_cough_severity_from_model(model, mfcc, mels, zcr, sc, sr, audio_sr, audio_file)
    return prediction_result[0]

#def toggle_switch_ui():
#   #st.write("## Toggle Switch")
#  toggleswitch=st_toggle_switch(
#    label="Select Audio Option",
#    key="switch_1",
#    default_value=False,
#    label_after=True,
#    inactive_color="#D3D3D3",  # optional
#    active_color="#11567f",  # optional
#    track_color="#29B5E8",  # optional
#  )
#
#  st.session_state.toggleswitchkey = toggleswitch
#
#  for f in glob.glob("./*.wav"):
#    os.remove(f)
#
#  if st.session_state.toggleswitchkey:
#    audio = audiorecorder("Click to Record", "Click again to stop Recording...")
#    if len(audio) > 0:
#      # To play audio in frontend:
#      st.audio(audio.tobytes(), format='audio/wav')
#      convert_filebyte_to_audio_sample_rate(audio.tobytes())
#  else:
#    uploaded_file = st.file_uploader("Upload a Audio file in .wav format", type='wav')
#    if uploaded_file is not None:
#      #st.audio(uploaded_file.getbuffer(), format='audio/wav')
#      st.audio(uploaded_file.read(), format='audio/wav')
#      #convert_filebyte_to_audio_sample_rate(uploaded_file)
#      save_to_temp_file(uploaded_file)


def convert_filebyte_to_audio_sample_rate(uploaded_audio_file):
  with TemporaryDirectory() as temporary_directory:
    temporary_file_path = Path(temporary_directory, 'cough_audio.wav')
    temporary_file_path.write_bytes(uploaded_audio_file.read())
    audio_wave, audio_sr = librosa.load(temporary_file_path, sr=None) 
    st.session_state.audio_sr = audio_sr
    st.session_state.audio_file = audio_wave
    #st.write(st.session_state.audio_sr)
    #st.write(st.session_state.audio_file)

def save_to_temp_file(uploaded_audio_file):
  with TemporaryDirectory() as temp_dir:
    temp_file_path = Path(temp_dir, 'cough_audio.wav')
    temp_file_path.write_bytes(uploaded_audio_file.read())
    
    wave, sr = librosa.load(temp_file_path, sr=None) 
    st.session_state.audio_sr = sr
    st.session_state.audio_file = wave    

if __name__ == '__main__':
   detect_cough_model, cough_severity_model = model_load(os.path.abspath(DETECT_COUGH_MODEL_PATH), os.path.abspath(COUGH_SEVERITY_MODEL_PATH))
   #st.help(detect_cough_model)
   #st.write(cough_severity_model)
   load_css()
   load_menu_html(True)
   st.markdown('''<style>
   [data-testid="stHeader"]{ display: none;}
   [data-testid="stSidebar"]{ display: none;}
   </style>''',unsafe_allow_html=True)
    
   #toggle_switch_ui()
   #uploaded_file = st.file_uploader("Upload a Audio file in .wav format", type='wav')
   #if uploaded_file is not None:
   #   #st.audio(uploaded_file.getbuffer(), format='audio/wav')
   #   st.audio(uploaded_file.read(), format='audio/wav')
   #   #convert_filebyte_to_audio_sample_rate(uploaded_file)
   #   #save_to_temp_file(uploaded_file)
   #   with TemporaryDirectory() as temp_dir:
   #     temp_file_path = Path(temp_dir, 'cough_audio.wav')
   #     temp_file_path.write_bytes(uploaded_file.read())
   #     wave, sr = librosa.load(temp_file_path, sr=None) 
   #     st.session_state.audio_sr = sr
   #     st.session_state.audio_file = wave  

   uploaded_file = st.file_uploader("Upload a Audio file in .wav format", type='wav')
   if uploaded_file is not None:
      st.session_state.audio_sr = ''
      st.session_state.audio_file = ''
      st.write(uploaded_file.name)
      for f in glob.glob("./*.wav"):
        os.remove(f)

      save_to_temp_file(uploaded_file)
      st.write(st.session_state.audio_sr)
      st.write(st.session_state.audio_file)

   btn=st.button("Diagnose")
   if btn:
    mfcc,mels,zcr,sc,sr = features_extractor(st.session_state.audio_sr, st.session_state.audio_file)
    cough_type_index = detect_cough(detect_cough_model, mfcc, mels, zcr, sc, sr)
    if COUGH_TYPE[cough_type_index]=='Coughing':
      severity_type_index=detect_cough_severity(cough_severity_model, mfcc, mels, zcr, sc, sr, st.session_state.audio_sr, st.session_state.audio_file)
      st.success(f"The Audio sample is {SEVERITY_TYPE[severity_type_index]}", icon="✅")
      #if label_class_index==LABEL_CLASS_NAMES[1]:
      #  st.success(f"The Audio sample is {LABEL_CLASS_NAMES[label_class_index]} with confidence level {confidence_percentage}%", icon="✅")
      #elif label_class_index==LABEL_CLASS_NAMES[2]:
      #  st.warning(f"The Audio sample is {LABEL_CLASS_NAMES[label_class_index]} with confidence level {confidence_percentage}%", icon="⚠️")
      #elif label_class_index==LABEL_CLASS_NAMES[3]:
      #  st.error(f"The Audio sample is {LABEL_CLASS_NAMES[label_class_index]} with confidence level {confidence_percentage}%", icon="🚨")
      #else:
      # st.info("Please try again.", icon="ℹ️")
      #The Audio sample is Healthy with confidence level 71.58%
    else:
      st.info("Cough was not detected in the uploaded audio file. Please try again with a valid audio file.", icon="ℹ️")

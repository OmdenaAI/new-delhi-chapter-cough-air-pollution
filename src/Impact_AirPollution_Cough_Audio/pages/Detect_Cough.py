import streamlit as st
from streamlit_toggle import st_toggle_switch
from audiorecorder import audiorecorder
import librosa
import numpy as np
import pandas as pd
from menu import load_menu_html, load_css
from tensorflow.keras.models import load_model

extracted_features=[]
label_class_names=['Healthy', 'Symptomatic', 'COVID-19']
MODEL_PATH='/Model/audio_classification_v1.0.hdf5'

@st.cache_resource
def model_load(path):
   return load_model(path)

#def features_extractor(file_name):
def features_extractor(audio,sample_rate):
    #audio, sample_rate = librosa.load(file_name)
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=20)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sample_rate, n_fft=2048, hop_length=512, n_mels=20)
    mel_scaled_features = np.mean(mel_spectrogram.T,axis=0)
    return mfccs_scaled_features, mel_scaled_features #, chroma_scaled_features

#def model_predict(file_path,model):
def model_predict(audio,sample_rate):
  model=model_load(MODEL_PATH)
  #mfcc, melspec = features_extractor(file_path)
  mfcc, melspec = features_extractor(audio,sample_rate)
  extracted_features.append([mfcc,melspec])
  extracted_features_df = pd.DataFrame(extracted_features,columns=['feature1','feature2'])
  X1 = np.array(extracted_features_df['feature1'].tolist())
  X2 = np.array(extracted_features_df['feature2'].tolist())
  predictions = model.predict(np.concatenate((np.array(extracted_features_df['feature1'].tolist()), np.array(extracted_features_df['feature2'].tolist())), axis=1))
  label_class_index=(np.argmax(predictions[0])-1)
  #1
  confidence_percentage=round(max(predictions[0])*100,2)
  #71.58
  return label_class_index,confidence_percentage

# INFO: by calling the function an instance of the audio recorder is created
# INFO: once a recording is completed, audio data will be saved to wav_audio_data
  #audio_bytes = audio_recorder(
  #  text="Click to record your cough",
  #  recording_color="#e8b62c",
  #  neutral_color="#6aa36f",)
  #st.audio(audio_bytes, format="audio/wav")
  #if audio_bytes:
  #  st.audio(audio_bytes, format="audio/wav")

def toggle_switch_ui():
   #st.write("## Toggle Switch")
  toggleswitch=st_toggle_switch(
    label="Select Audio Option",
    key="switch_1",
    default_value=False,
    label_after=True,
    inactive_color="#D3D3D3",  # optional
    active_color="#11567f",  # optional
    track_color="#29B5E8",  # optional
  )
  if toggleswitch:
    audio = audiorecorder("Click to Record", "Click again to stop Recording...")
    if len(audio) > 0:
      # To play audio in frontend:
      st.audio(audio.tobytes())
      with open("cough_audio.wav", "wb") as wav_file:
        wav_file.write(audio.tobytes()) 
  else:
    uploaded_file = st.file_uploader("Upload a Audio file")
    if uploaded_file is not None:
      with open("cough_audio.wav", "wb") as wav_file:
        wav_file.write(uploaded_file.getbuffer()) 

def diagnose_cough():
  audio, sample_rate = librosa.load("cough_audio.wav")
  print("Librosa Library data : ",audio,sample_rate)
  #predicted_result= model_predict(file_path,model)
  predicted_result_label_index,predicted_result_conf= model_predict(audio,sample_rate)
  return predicted_result_label_index,predicted_result_conf
  #The Audio sample is Healthy with confidence level 71.58%

if __name__ == '__main__':
   load_css()
   load_menu_html(True)
   st.markdown('''<style>
   [data-testid="stHeader"]{ display: none;}
   [data-testid="stSidebar"]{ display: none;}
   </style>''',unsafe_allow_html=True)
    
   toggle_switch_ui()
   btn=st.button("Diagnose")
   if btn:
    label_class_index,confidence_percentage=diagnose_cough()
    if label_class_index==label_class_names[0]:
      st.success(f"The Audio sample is {label_class_names[label_class_index]} with confidence level {confidence_percentage}%", icon="✅")
    elif label_class_index==label_class_names[1]:
      st.warning(f"The Audio sample is {label_class_names[label_class_index]} with confidence level {confidence_percentage}%", icon="⚠️")
    elif label_class_index==label_class_names[2]:
      st.error(f"The Audio sample is {label_class_names[label_class_index]} with confidence level {confidence_percentage}%", icon="🚨")
    else:
     st.info("Please try again.", icon="ℹ️")
   #The Audio sample is Healthy with confidence level 71.58%

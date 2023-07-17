import numpy as np
import pandas as pd
import os, librosa, lightgbm, joblib #, pickle

def chroma_scaled_features(audio_sr, audio_file):
    stft = np.abs(librosa.stft(audio_file))
    chroma = librosa.feature.chroma_stft(S=stft, sr=audio_sr)
    chroma_scaled_features = np.mean(chroma.T,axis=0)
    return chroma_scaled_features

def features_extractor(audio_sr, audio_file):
    mfccs_features = librosa.feature.mfcc(y=audio_file, sr=audio_sr, n_mfcc=16)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    mel_spectrogram = librosa.feature.melspectrogram(y=audio_file, sr=audio_sr, n_fft=2048, hop_length=512, n_mels=10)
    mel_scaled_features = np.mean(mel_spectrogram.T,axis=0)
    zcr = librosa.feature.zero_crossing_rate(audio_file)
    zcr_scaled_features = np.mean(zcr.T,axis=0)
    spectral_centroid = librosa.feature.spectral_centroid(y=audio_file, sr=audio_sr)
    spectral_centroid_scaled_features = np.mean(spectral_centroid.T,axis=0)
    spectral_rolloff = librosa.feature.spectral_rolloff(y=audio_file, sr=audio_sr)
    spectral_rolloff_scaled_features = np.mean(spectral_rolloff.T,axis=0)
    return mfccs_scaled_features, mel_scaled_features, zcr_scaled_features, spectral_centroid_scaled_features, spectral_rolloff_scaled_features

def load_all_models(detect_cough_model_path, detect_cough_severity_model_path):
    detect_cough_model = joblib.load(detect_cough_model_path)#pickle.load(open(detect_cough_model_path, 'rb'))
    detect_cough_severity_model = joblib.load(detect_cough_severity_model_path)
    return detect_cough_model, detect_cough_severity_model 

def detect_cough_from_model(model, mfcc, mels, zcr, sc, sr):
    extracted_features=[]
    extracted_features.append([mfcc[0], mfcc[1], mfcc[2], mfcc[3], mfcc[4], mfcc[5], mfcc[6], mfcc[7], mfcc[8], mfcc[9], mfcc[10], mfcc[11], mfcc[12], mfcc[13], mfcc[14], mfcc[15], mels[0], mels[1], mels[2], mels[3], mels[4], mels[5], mels[6], mels[7], mels[8], mels[9], zcr[0], sc[0], sr[0]])
    extracted_features_df = pd.DataFrame(extracted_features, columns = ['mfcc1', 'mfcc2', 'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10', 'mfcc11', 'mfcc12', 'mfcc13', 'mfcc14', 'mfcc15', 'mfcc16', 'mels1', 'mels2', 'mels3',  'mels4', 'mels5', 'mels6', 'mels7', 'mels8', 'mels9', 'mels10', 'zcr', 'sc', 'sr'])
    prediction_result = model.predict(extracted_features_df)[0]
    #prediction_result = predict_model(model,data=extracted_features_df)
    return prediction_result

def detect_cough_severity_from_model(model, mfcc, melspec, zcr, sc, sr, audio_sr, audio_file):
    extracted_features=[]
    chroma = chroma_scaled_features(audio_sr, audio_file)
    extracted_features.append([mfcc[0], mfcc[1], mfcc[2], mfcc[3], mfcc[4], mfcc[5], mfcc[6], mfcc[7], mfcc[8], mfcc[9], mfcc[10], mfcc[11], mfcc[12], mfcc[13], mfcc[14], mfcc[15], melspec[0], melspec[1], melspec[2], melspec[3], melspec[4], melspec[5], melspec[6], melspec[7], melspec[8], melspec[9], zcr[0], sc[0], sr[0], chroma[0]])
    extracted_features_df = pd.DataFrame(extracted_features, columns = ['mfcc1', 'mfcc2', 'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10', 'mfcc11', 'mfcc12', 'mfcc13', 'mfcc14', 'mfcc15', 'mfcc16', 'melspec1', 'melspec2', 'melspec3', 'melspec4', 'melspec5', 'melspec6', 'melspec7', 'melspec8', 'melspec9', 'melspec10', 'zcr', 'sc', 'sr', 'chroma'])
    prediction_result = model.predict(extracted_features_df)[0]
    return prediction_result

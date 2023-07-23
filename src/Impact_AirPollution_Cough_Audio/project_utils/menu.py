import streamlit as st
def load_css():
    return st.markdown("""
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
  <style>
   [data-testid="stHeader"]{
        display: none;
	    }
   [data-testid="stSidebar"]{
   display: none;
   }   
    [data-testid="collapsedControl"]{
   display: none;
   }   
  body {
    font: 400 15px Lato, sans-serif;
    line-height: 1.8;
    color: #818181;
  }
  h2 {
    font-size: 24px;
    text-transform: uppercase;
    color: white;
    font-weight: 600;
    margin-bottom: 30px;
  }
  h4 {
    font-size: 19px;
    color: #303030;
    margin-bottom: 30px;
  }  
  p {
    font-size: medium;
  }
  th{
    text-align: center;
  }
  .jumbotron {
    background-color: #f4511e;
    color: #fff;
    padding: 100px 25px;
    font-family: Montserrat, sans-serif;
  }
  .container-fluid {
    padding: 60px 50px;
  }
  .bg-grey {
    background-color: #f6f6f6;
  }
  .item h4 {
    font-size: 19px;
    line-height: 1.375em;
    font-weight: 400;
    font-style: italic;
    margin: 70px 0;
  }
  .navbar {
    background-color: #f4511e;
    z-index: 9999;
    border: 0;
    font-size: 12px !important;
    line-height: 1.42857143 !important;
    letter-spacing: 4px;
    font-family: Montserrat, sans-serif;
    font-weight: 600;
  }
  .navbar li a, .navbar .navbar-brand {
    color: #fff !important;
    font-size:medium;
  }
  .navbar-nav li a:hover, .navbar-nav li.active a {
    color: #f4511e !important;
    background-color: #fff !important;
  }
  .navbar-default .navbar-toggle {
    border-color: transparent;
    color: #fff !important;
  }
  .slide {
    animation-name: slide;
    -webkit-animation-name: slide;
    animation-duration: 1s;
    -webkit-animation-duration: 1s;
    visibility: visible;
  }
  @keyframes slide {
    0% {
      opacity: 0;
      transform: translateY(70%);
    } 
    100% {
      opacity: 1;
      transform: translateY(0%);
    }
  }
  @-webkit-keyframes slide {
    0% {
      opacity: 0;
      -webkit-transform: translateY(70%);
    } 
    100% {
      opacity: 1;
      -webkit-transform: translateY(0%);
    }
  }
  @media screen and (max-width: 768px) {
    .col-sm-4 {
      text-align: center;
      margin: 25px 0;
    }
    .btn-lg {
      width: 100%;
      margin-bottom: 35px;
    }
  }
  </style>
  """
,unsafe_allow_html=True)


def load_menu_html(is_app_page):
    if is_app_page:
        st.markdown(f"""   <base href=".."/>
    <link rel="redirect" id="project" href="#project"/>
    <link rel="redirect" id="team" href="#team"/>
    <link rel="redirect" id="datasource" href="#datasource"/>
    <link rel="redirect" id="coughdiagnosis" href="#coughdiagnosis"/>
    <nav class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="#myPage">Logo</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-right font-weight-bold">
        <li><a href="#project">Project</a></li>
        <li><a href="#team">About Team</a></li>
        <li><a href="#datasource">Data Source</a></li>
        <li><a href="#coughdiagnosis">Cough Diagnosis</a></li>
      </ul>
    </div>
  </div>
</nav>
<div class="jumbotron text-center">
  <h1>Identifying the Severity of Cough Due to Air Pollution in New Delhi using Audio Analysis and Machine Learning</h1> 
</div>
"""
,unsafe_allow_html=True)
    else:
        return st.markdown(f"""                         
<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="#myPage"></a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#project">Project</a></li>
        <li><a href="#team">About Team</a></li>
        <li><a href="#datasource">Data Source</a></li>
        <li><a href="#coughdiagnosis">Cough Diagnosis</a></li>
      </ul>
    </div>
  </div>
</nav>
<div class="jumbotron text-center">
  <h1>Identifying the Severity of Cough Due to Air Pollution in New Delhi using Audio Analysis and Machine Learning</h1> 
</div>
"""
,unsafe_allow_html=True)

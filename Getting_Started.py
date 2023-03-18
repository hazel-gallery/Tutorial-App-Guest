import streamlit as st
from PIL import Image

st.title('Getting Started')
st.markdown('''
    Congratulations! You have successfully built the Tutorial app
    in our guest server. You can also build this app in your own
    server by following the tutorial. \n

    Developing a web application and configuring the necessary 
    cloud resources can be a time-consuming process involving 
    multiple elements, including a host machine, operating 
    system, databases, and security measures. As the complexity 
    of the application grows, so does the level of intricacy 
    in the workflows. To simplify this process and save you 
    time, we have designed a standard procedure that 
    streamlines the workflows. \n

    We are excited to introduce our App Gallery, which
    provides a hassle-free way for you to build 
    applications on your preferred server. By browsing through 
    our selection of apps, you can easily view a list of the 
    minimum required specifications for cloud resources. You can 
    then customize these specifications to meet your unique 
    requirements by increasing the specs to your preference.

''')
img_sys = Image.open('images/sys_min.jpg')
st.image(img_sys)

st.markdown('''
    Once the request is finalized, Hazel proceeds to send it to the cloud 
    provider, which then pulls the required resources and prepares them 
    for application development. The server environment is set up 
    by downloading and installing all the necessary dependencies. 
    Once everything is in place, the server exposes an IP 
    address, and the application is instantly accessible as 
    a web service.

''')

img_workflow = Image.open('images/workflow.png')
st.image(img_workflow)

st.markdown('''
    Our goal is to simplify the web application development 
    process and make it accessible to everyone. With our App 
    Gallery and streamlined procedures, you can focus on 
    creating your application without the worry of complicated 
    workflows or resource management.
''')


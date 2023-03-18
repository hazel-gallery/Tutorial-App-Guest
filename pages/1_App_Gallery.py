import streamlit as st
from PIL import Image

st.title('App Gallery')

st.subheader('''
    Everything is open-sourced! :100: 
''')

st.markdown('''

    We are constanly expanding the volume, bring you more 
    useful applications. You can check out any app’s source 
    code in its Github, or building the application 
    in your local computer by pulling the Docker image. There
    is no limitation to how you use the codes, be creative.

''')

img_source = Image.open('images/source_code.jpg')
st.image(img_source)

st.text('')
st.text('')

st.subheader('''
    Building an App :hammer_and_wrench:
''')

st.markdown('''
    Building an app with Hazel is quite simple.
    For every app, it is given a mininum required specs
    to start with. A system  include the cloud provider,
    server  (CPU and memory), and the storage size.
''')
img_sys_min = Image.open('images/sys_min.jpg')
st.image(img_sys_min)

st.markdown('''
    You are also given options to increase the spec level
''')
img_sys_option = Image.open('images/sys_option.jpg')
st.image(img_sys_option)          

st.markdown('''
    Once finalized, click the :blue[**Build**] button 
''')

st.text('')
st.text('')

st.subheader('''
    Mangaging Apps :pager:
''')

st.markdown('''
    The console page provides an interface to  display 
    and manage your apps, including their 
    links, specs, and the option to terminate. Note that 
    terminating an app will also 
    terminate its host server. We recommend always 
    terminate unused apps to save cost.
''')
img_console = Image.open('images/console.jpg')
st.image(img_console)   



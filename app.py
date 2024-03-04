import streamlit as st
import cv2
import drowsiness_detection as detection

def camera():
    st.session_state.clicked = not st.session_state.clicked

def main():
    st.title('Drowsiness Detection', False)
    camera = cv2.VideoCapture(0)
    with st.sidebar:
        # Settings
        st.title('Menu')
        app_mode = st.selectbox('Choose the App mode', ['Drowsiness Detection', 'About'])
    if app_mode == 'Drowsiness Detection':
        with st.sidebar:
            st.markdown('---')
            # change camera state
            run = st.checkbox('Camera On')
        
        FRAME_WINDOW = st.image([])
        while run:
            _, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = detection.check_drowsy(frame)
            FRAME_WINDOW.image(output)
        else:
            st.write('Camera OFF')
            
    elif app_mode == 'About':
        st.header('About App',False)
        st.markdown('This is Drowsiness Detection Application, when user turn on camera then camera start to detect drowsiness of driver')
        st.markdown('''I am Sumit Pal Singh, a Machine Learning Enthuiast. you can follow me.  
                    Linkedin : https://www.linkedin.com/in/sumit-pal-singh-233639217/
                    ''')

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass


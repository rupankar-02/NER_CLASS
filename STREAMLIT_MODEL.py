import streamlit as st
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from newspaper import Article

nlp = en_core_web_sm.load()
from pprint import pprint

st.title("Named Entity Recognizer")

st.info("Put URL or copy any paragraph in this page")

status = st.radio("Select any: ", ('URL', 'Paragraph'))
 
if (status == 'URL'):
    st.success("Enter the URL below")
    url = st.text_input("Enter the URL")
   
    if(st.button("Analyze")):
        article=Article(url)
        article.download()
        article.parse()
        doc = nlp(article.text)
        displacy.render(doc, style='ent')
        st.markdown(displacy.render(doc, style='ent'), unsafe_allow_html=True)
           
else:
    st.success("Type Your Paragraph Below")
    paragraph=st.text_area("Enter the Paragraph")
    
    if(st.button("Analyze")):
        doc=nlp(paragraph)
        ent_html = displacy.render(doc, style="ent")
        # Display the entity visualization in the browser:
        st.markdown(ent_html, unsafe_allow_html=True)

        
level = st.slider("Rate the website out of 10", 1, 10)
st.text('You have rated this website: {} out of 10'.format(level))
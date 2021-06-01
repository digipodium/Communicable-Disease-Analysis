import streamlit as st
import pandas as pd

from analyze import Analyse

st.title('Communicable disease Analysis')
st.image('2.jpg')


def overview():
    st.header('Project Overview')


def viewDataset(path):
    st.write('Dataset Used in Project')
    analysis = Analyse(path)
    dataframe = analysis.getDataframe()

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")


sidebar = st.sidebar
sidebar.header('Choose Your Option')
options = ('View Dataset', 'Analysis of Malaria',
           'Analysis of Tuberculosis', 'Analyze By Hepatitus', 'About')
choice = sidebar.selectbox(options=options, label="Choose Action")

if choice == 'View Dataset':
    with st.spinner("Loading Data..."):
        st.header('Raw datasets')
        st.header('Hepatitus Dataset')
        viewDataset(path='datasets/hepatitusBsurfaceAntigen.csv')
        st.header('Malaria Dataset')
        viewDataset(path='datasets/incedenceOfMalaria.csv')
        st.header('Tuberculosis Dataset')
        viewDataset(path='datasets/incedenceOfTuberculosis.csv')
        st.header('NTDs Dataset')
        viewDataset(path='datasets/interventionAgianstNTDs.csv')
        st.header('HIV Dataset')
        viewDataset(path='datasets/newHivInfections.csv')
elif choice == 'Analysis of Malaria':
    with st.spinner("Loading Analysis..."):
        st.subheader(
            'Number of malaria cases per 1000 population at risk per year.')
        st.write(
            'Cases of Malaria in thousand population in these countries, India, Nepal, Bhutan, Malaysia')
        st.image('images/malaria1.png')
        st.subheader('Top 20 countries with highest Malaria Incidence')
        st.write('Randawa having the highest Malaria Cases')
        st.image('images/malaria2.png')
        st.subheader(
            'Number of malaria cases per 1000 population at risk per year.')
        st.write(
            'Cases of Malaria from 2000 to 2018 per thousand population at theses countries')
        st.image('images/malaria3.png')
        st.subheader('Best progress in malaria incidence over year')
        st.write('Positive progess in countries over a period of 18 years ie.. 2000 to 2018, per thousand population at theses countries')
        st.image('images/malaria4.png')
        st.write('''Countries with highest Progess :- Timor-Leste
Lets look at these countries progress
        ''')
        st.subheader(
            'Number of malaria cases per 1000 population at risk per year.')
        st.write(
            'Comparision of top 5 progressing countries over a period of 2000 to 2018 in Malaria Incidence')
        st.image('images/malaria5.png')
        st.subheader('Progress of different countries')
        st.write('Progess in countries over a period of 18 years ie.. 2000 to 2018, per thousand population at theses countries')
        st.image('images/malaria6.png')
        st.subheader(
            'Number of malaria cases per 1000 population at risk per year.')
        st.write(
            'Comparison of 2 best and 2 worst preforming countries over a period of 18 years ie... 2000 to 2018')
        st.image('images/malaria7.png')
elif choice == 'Analysis of Tuberculosis':
    with st.spinner("Loading Analysis..."):
        st.subheader(
            'Number of Tuberculosis cases per 100,000 population at risk per year')
        st.write(
            'Cases of tuberculosis over a period of 2000 to 2018 in India, China, Germany and USA.')
        st.image('images/tb1.png')
        st.subheader(
            'Top and bottom 20 countries with lowest Tuberculosis incidence')
        st.write(
            'bottom and top 20 countries with lowest and highest Tuberculosis incidence in 2019 respectively')
        st.image('images/tb2.png')
        st.subheader(
            'Where different countries stand in 2019(Tuberculosis Incidence)')
        st.write('Tuberculosis incidence and where these countries stand in 2019')
        st.image('images/tb3.png')
        st.header('Lets Look at the progress of TOP 5 and BOTTOM 5 countries')
        st.subheader(
            'Number of Tuberculosis cases per 100,000 population at risk per year')
        st.write(
            'Cases of tuberculosis over a period of 2000 to 2018 in 100,000 population')
        st.write('Plot For TOP 5 Countries')
        st.image('images/tb4.png')
        st.subheader(
            'Number of Tuberculosis cases per 100,000 population at risk per year')
        st.write(
            'Cases of tuberculosis over a period of 2000 to 2018 in 100,000 population')
        st.write('Plot For BOTTOM 5 Countries')
        st.image('images/tb5.png')

        st.subheader('Countries having peak')
        st.image('images/tb6.png')
        st.write('''We can see that most of countries achieve their peak in 2000
But some countries are at their peak at 2019 also, lets have a look at those countries progress
        ''')
        st.subheader(
            'Number of Tuberculosis cases per 100,000 population at risk per year')
        st.write(
            'Countries at peak in 2019, their population at risk per 100,000 population at risk per year')
        st.image('images/tb7.png')
        st.subheader(
            'Progress of Different Countries in Tuberculosis incedence')
        st.write('Lets Look at the progress')
        st.image('images/tb8.png')
        st.subheader('Where different countries stand in progress')
        st.write(
            'Tuberculosis incidence progress and where these countries stand in 2019')
        st.image('images/tb9.png')
        st.subheader(
            'Number of Tuberculosis cases per 100,000 population at risk per year')
        st.write('Comparsion of Tuberculosis cases per 100,000 population at risk per year in Botswana, Eswatini, Nauru and Marshall Islands')
        st.image('images/tb10.png')
elif choice == 'Analyze By Hepatitus':
    with st.spinner("Loading Analysis..."):
        st.subheader('Top and bottom 20 countries in Hepatitus Incidence')
        st.write('bottom and top 20 countries with lowest and highest Hepatitus incidence among children under 5 years in 2019 respectively')
        st.image('images/h1.png')
        st.subheader('Where Different countries stand in progress')
        st.write(
            'Hepatitus incidence among children under 5 years and where these countries stand in 2019')
        st.image('images/h2.png')
elif choice == 'About':
    with st.spinner("Loading Analysis..."):
        st.write('''A communicable disease is one that is spread from one person to another through a variety of ways that include: contact with blood and bodily fluids; breathing in an airborne virus; or by being bitten by an insect.

Reporting of cases of communicable disease is important in the planning and evaluation of disease prevention and control programs, in the assurance of appropriate medical therapy, and in the detection of common-source outbreaks. California law mandates healthcare providers and laboratories to report over 80 diseases or conditions to their local health department. Some examples of the reportable communicable diseases include Hepatitis A, B & C, influenza, measles, and salmonella and other food borne illnesses.
        ''')

        st.write('''<b>How do these communicable diseases spread?<b>

How these diseases spread depends on the specific disease or infectious agent. Some ways in which communicable diseases spread are by:

physical contact with an infected person, such as through touch (staphylococcus), sexual intercourse (gonorrhea, HIV), fecal/oral transmission (hepatitis A), or droplets (influenza, TB)
contact with a contaminated surface or object (Norwalk virus), food (salmonella, E. coli), blood (HIV, hepatitis B), or water (cholera);
bites from insects or animals capable of transmitting the disease (mosquito: malaria and yellow fever; flea: plague); and
travel through the air, such as tuberculosis or measles.

        ''', unsafe_allow_html=True)

        st.write('Here, in this project we can draw insights like which country has made how much progress in years, we can see status of Malaria, Tuberculosis and hepatitus in countries. we can view the dataset used in the project(Raw Data). This project is basically analysis of some communicable disease like Malaria, Tuberculosis and Hepatitus')

        st.markdown('# This is Heading')

import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Recommend Apartments")

st.title("Apartment Recommendation System")

# Load data
location_df = pickle.load(open('datasets/location_distance.pkl', 'rb'))
cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))

# Recommendation function based on a weighted combination of similarity matrices
def recommend_properties_with_scores(property_name, top_n=5):
    # Weighted combination of cosine similarity matrices
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

    # Get similarity scores for the selected property
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties by similarity score in descending order
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get indices and similarity scores of the top_n properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Get names of the top properties
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with recommendations
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df

# Step 1: Location-based filtering
st.header('Select Location and Radius')
st.write('after filtering')

# Allow the user to select a location and input a radius
selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in Kms', min_value=1.0, max_value=100.0, step=1.0)

# Use session state to preserve the filtered apartments after searching
if 'filtered_apartments' not in st.session_state:
    st.session_state['filtered_apartments'] = None

if st.button('Search'):
    # Filter apartments within the given radius (convert radius to meters)
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values().to_dict()

    if result_ser:
        # Convert the result to a DataFrame and store it in session state
        filtered_apartments = pd.DataFrame(list(result_ser.items()), columns=['Apartment', 'Distance (kms)'])
        filtered_apartments['Distance (kms)'] = filtered_apartments['Distance (kms)'] / 1000  # Convert meters to kms
        st.session_state['filtered_apartments'] = filtered_apartments
        st.write(f"**Filtered Apartments within {radius} km of {selected_location}:**")
        st.dataframe(filtered_apartments)
    else:
        st.write("No apartments found within the selected radius.")

# Step 2: Apartment recommendation based on filtered results
if st.session_state['filtered_apartments'] is not None:
    st.header('Recommend Similar Apartments')

    # Allow the user to select an apartment from the filtered list
    selected_apartment = st.selectbox('Select an apartment', st.session_state['filtered_apartments']['Apartment'].tolist())

    if st.button('Recommend'):
        # Get recommended properties based on the selected apartment
        recommendation_df = recommend_properties_with_scores(selected_apartment)
        st.dataframe(recommendation_df)

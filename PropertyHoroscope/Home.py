import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="",
)

st.sidebar.success("Select a demo above.")



# Load an image for the home page (optional)
# You can add an image related to properties in Gurgaon or a logo for Propertyhoroscope
image = Image.open('property_image.jpg')  # Replace with your own image

st.image(image, use_column_width=True)

# Title and descriptionst.title("Welcome to PropertyHoroscope 🏡✨")
st.subheader("Unlock Insights for Your Dream Property in Gurgaon")

st.write("""
At **PropertyHoroscope**, we’ve combined data, analysis, and smart technology to help you make informed property decisions in Gurgaon. Whether you're looking to predict property prices, explore detailed analytics, or find apartments that match your preferences—this is your one-stop solution. Let's take a tour of what you can do on our platform:
""")

# Feature 1: Price Prediction Module
st.markdown("### 🔮 **Price Prediction Module**")
st.write("""
Just input details like property type, number of bedrooms, location, and more, and we’ll provide you with an accurate price prediction. Whether it's a house or a flat, we've got you covered! Discover the value of properties before you make any big decisions.
""")

# Feature 2: Analytics Module
st.markdown("### 📊 **Analytics Module**")
st.write("""
Dive deep into Gurgaon’s real estate data with our **Analytics Module**:
- **Sector Price per Sqft Geomap**: Understand property prices visually across sectors.
- **Features Wordcloud**: See what amenities are common in specific sectors.
- **Area vs Price**: Analyze how property size influences price.
- **BHK Pie Charts**: Explore the distribution of BHKs in different sectors.
- **Price Comparisons**: Compare BHKs side by side using Box Plots and Dist Plots for different property types.
Let data guide your decisions!
""")

# Feature 3: Apartment Recommendation System
st.markdown("### 🏢 **Apartment Recommendation System**")
st.write("""
Looking for a new apartment? Our **Recommendation System** suggests apartments based on your chosen location, radius, and preferences. We filter the best matches using your inputs and recommend the most similar options, powered by our advanced model.
""")

# Call to Action
st.markdown("### 🌟 **Ready to Explore?**")
st.write("Start by selecting an option from the menu on the left and make smarter property decisions today!")

# Additional Links or Contact
st.write("If you have any questions or need support, feel free to contact us at **support@propertyhoroscope.com**.")


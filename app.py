import streamlit as st

# Streamlit App Title
st.title("🔄 Unit Converter")

# Categories of Unit Conversion
categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Weight/Mass": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Area": ["square meter", "square kilometer", "square foot", "square yard", "acre", "hectare"],
    "Volume": ["liter", "milliliter", "gallon", "cup", "pint"],
    "Speed": ["meter per second", "kilometer per hour", "mile per hour", "knot"],
    "Time": ["second", "minute", "hour", "day"],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt-hour", "kilowatt-hour"],
    "Pressure": ["pascal", "bar", "atmosphere", "torr", "psi"],
}

# Session State for Recent Conversions
if "history" not in st.session_state:
    st.session_state.history = []

# Select Conversion Category
category = st.selectbox("Select Category", list(categories.keys()))
units = categories[category]

# Input Fields
amount = st.number_input("Enter Value", min_value=0.0, step=0.01, format="%.2f")
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

# Conversion Logic
conversion_factors = {
    "Length": {"meter": 1, "kilometer": 1000, "centimeter": 0.01, "millimeter": 0.001, "mile": 1609.34, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254},
    "Weight/Mass": {"gram": 1, "kilogram": 1000, "pound": 453.592, "ounce": 28.3495, "ton": 1000000},
    "Temperature": {"celsius": lambda x: x, "fahrenheit": lambda x: (x * 9/5) + 32, "kelvin": lambda x: x + 273.15},
    "Area": {"square meter": 1, "square kilometer": 1e6, "square foot": 0.092903, "square yard": 0.836127, "acre": 4046.86, "hectare": 10000},
    "Volume": {"liter": 1, "milliliter": 0.001, "gallon": 3.78541, "cup": 0.24, "pint": 0.473176},
    "Speed": {"meter per second": 1, "kilometer per hour": 0.277778, "mile per hour": 0.44704, "knot": 0.514444},
    "Time": {"second": 1, "minute": 60, "hour": 3600, "day": 86400},
    "Frequency": {"hertz": 1, "kilohertz": 1000, "megahertz": 1e6, "gigahertz": 1e9},
    "Energy": {"joule": 1, "kilojoule": 1000, "calorie": 4.184, "kilocalorie": 4184, "watt-hour": 3600, "kilowatt-hour": 3.6e6},
    "Pressure": {"pascal": 1, "bar": 1e5, "atmosphere": 101325, "torr": 133.322, "psi": 6894.76},
}

if st.button("Convert"):
    try:
        if category == "Temperature":
            result = conversion_factors[category][to_unit](amount)
        else:
            result = amount * conversion_factors[category][from_unit] / conversion_factors[category][to_unit]
        st.success(f"{amount} {from_unit} = {result:.2f} {to_unit}")
        
        # Save to history
        st.session_state.history.insert(0, f"{amount} {from_unit} → {result:.2f} {to_unit}")
        if len(st.session_state.history) > 5:
            st.session_state.history.pop()
    except Exception as e:
        st.error(f"Conversion Error: {str(e)}")

# Display Conversion History
if st.session_state.history:
    st.subheader("📜 Recent Conversions")
    for item in st.session_state.history:
        st.write(item)

import streamlit as st

# Page configuration
st.set_page_config(page_title="Power Calculator", page_icon="🧮", layout="centered")

# Title and description
st.title("🧮 Power Calculator")
st.markdown("""
Enter a number below to instantly see its square, cube, and fifth power.
Perfect for quick math checks or exploring how numbers grow with higher exponents!
""")

# Sidebar for additional options
with st.sidebar:
    st.header("Options")
    show_formula = st.checkbox("Show mathematical formulas", value=True)
    dark_mode_hint = st.info("Streamlit automatically adapts to your system theme 🎨")

# Main input
st.subheader("Enter a number")
col1, col2 = st.columns([3, 1])

with col1:
    n = st.number_input(
        "Number",
        value=2.0,
        step=1.0,
        format="%.2f",
        help="You can enter integers or decimal numbers"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)  # Vertical alignment
    example = st.selectbox(
        "Quick examples",
        options=[None, 2, 5, 10, -3, 1.5, 100],
        format_func=lambda x: "Select..." if x is None else str(x)
    )
    if example is not None:
        n = float(example)

# Calculate powers
if n == 0:
    square = 0
    cube = 0
    fifth = 0
else:
    square = n ** 2
    cube = n ** 3
    fifth = n ** 5

# Display results in nice cards
st.markdown("---")
st.subheader("Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Square" + (" (n²)" if show_formula else ""),
        value=f"{square:,.4f}".rstrip("0").rstrip(".")
    )

with col2:
    st.metric(
        label="Cube" + (" (n³)" if show_formula else ""),
        value=f"{cube:,.4f}".rstrip("0").rstrip(".")
    )

with col3:
    st.metric(
        label="Fifth Power" + (" (n⁵)" if show_formula else ""),
        value=f"{fifth:,.4f}".rstrip("0").rstrip(".")
    )

# Optional: Show calculation details
if show_formula:
    st.markdown("---")
    st.subheader("Formulas Used")
    st.latex(f"n^2 = {n} \\times {n} = {square:,.4f}")
    st.latex(f"n^3 = {n} \\times {n} \\times {n} = {cube:,.4f}")
    st.latex(f"n^5 = {n} \\times {n} \\times {n} \\times {n} \\times {n} = {fifth:,.4f}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
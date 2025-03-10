import streamlit as st 

#app to tittle 
st.title("unit converter")

#unit conversion 
conversion_types = [ "length","Weight","Temperature",]
# user se conversion choose karwana
conversion_choice = st.selectbox("Choose Conversion Type:",conversion_types)

#length conversion

if conversion_choice == "length":
    length_units = [ "meters","Kiloeters","Feet","Inches","Centimeters"]
    input_value = st.number_input("Enter Length Value:",min_value=0.0, format =  "%.2f")
    from_unit = st.selectbox("from unit :", length_units)
    to_unit = st.selectbox("to unit :",length_units)

    #conversion dictionaries
    length_conversion = {
        "Meters": 1,
        "Kilometer":1000,
        "Feet":0.3048,
        "Inches":0.0254,
        "Centimeter":0.01
    }

    #conversion logic
    if st.button("convert"):
        result = input_value* (length_conversion[from_unit] / length_units[to_unit])
        st.success(f"{input_value}{from_unit} is equal to {result}{to_unit}")


    # weight conversion 
    elif conversion_choice == "Weight":
         weight_units = ["Kilograms","Grams","Pounds","Ounces"]   
         input_value = st.number_input("Enter Weight Value:",min_value=0.0, format =  "%.2f")
         from_unit = st.selectbox("from unit :", weight_units)
         to_unit = st.selectbox("to unit :",weight_units)


         #conversion dictionaries
         weight_conversion = {
            "Kilograms":1,
            "Grams":0.001,
            "Pounds":0.453592,
            "Ounches":0.0283495
         }

         # conversion logic 
         if st.button("convert"):
          result = input_value*( weight_conversion[from_unit] / weight_units[to_unit])
          st.success(f"{input_value}{from_unit} is equal to {result:.2f}{to_unit}")
         
         # tempreture conversion 
    elif conversion_choice == "Tempreture":
        temperature_unit= ["Celsius","Fahrenhetit","Kelvin"]
        input_value = st.number_input("Enter Temperature Value:",min_value=0.0, format =  "%.2f")
        from_unit = st.selectbox("from unit :","temperature_unit")
        to_unit = st.selectbox("to unit :","temperature_units") 
 
        def convert_temperature (value,from_unit, to_unit):
            if from_unit == "celsius":
                if to_unit == "Fahrenhit":
                    return (value * 9/5) + 32
                elif to_unit == "kelvin":
                    return value + 273.15
                elif from_unit == "Fahrenhit":
                    if to_unit == "Celsius":
                        return (value - 32) * 5/9
                elif to_unit =="Kelvin":
                    return (value-32)* 5/9 + 273.15
                elif from_unit == "Kelvin":
                    if to_unit == "Celsius":
                        return value - 273.15
                elif to_unit == "Fahrenhit":
                    return (value- 273.15)* 9/5 +32
                return value
                if st.button("Convert") :
                   result = convert_temperature(input_value,from_unit,to_unit)
            st.success(f"{input_value}{from_unit} is equal to {result:.2f}{to_unit}")
import streamlit as st
from utils.functions import get_trainingplan
import random
import os
from datetime import datetime, timedelta
from utils.functions import language_options, EN_ui_title, EN_ui_get_race_info, EN_ui_warnings, EN_get_race_info, EN_ui_get_goal_info, EN_ui_get_current_ability, get_race_info, get_goal_info, calculate_race_goalpace, ui_get_current_ability, ui_title, ui_warnings, ui_get_race_info, ui_get_goal_info



def english_version():
    EN_ui_title()
    race_day, race_distance_input = EN_ui_get_race_info()
    race_days_until_int, race_days_until, race_distance_float, race_distance = EN_get_race_info(race_distance_input, race_day)
    EN_ui_warnings(race_days_until_int)
    race_goaltime_input = EN_ui_get_goal_info(race_distance_input)
    race_goaltime_minutes, race_goaltime = get_goal_info(race_goaltime_input)
    race_goalpace = calculate_race_goalpace(race_goaltime_minutes, race_distance_float)
    current_pb, current_mileage, current_frequency, current_othernotes = EN_ui_get_current_ability(race_distance_input)
    return race_day, race_days_until, race_distance, race_goaltime, race_goalpace, current_pb, current_mileage, current_frequency, current_othernotes


def japanese_version():
    ui_title()
    race_day, race_distance_input = ui_get_race_info()
    race_days_until_int, race_days_until, race_distance_float, race_distance = get_race_info(race_distance_input, race_day)
    ui_warnings(race_days_until_int)
    race_goaltime_input = ui_get_goal_info(race_distance_input)
    race_goaltime_minutes, race_goaltime = get_goal_info(race_goaltime_input)
    race_goalpace = calculate_race_goalpace(race_goaltime_minutes, race_distance_float)
    current_pb, current_mileage, current_frequency, current_othernotes = ui_get_current_ability(race_distance_input)
    return race_day, race_days_until, race_distance, race_goaltime, race_goalpace, current_pb, current_mileage, current_frequency, current_othernotes



def main():

    language = language_options()


    if language == "English":
        race_day, race_days_until, race_distance, race_goaltime, race_goalpace, current_pb, current_mileage, current_frequency, current_othernotes = english_version()

    if language == "日本語":
        race_day, race_days_until, race_distance, race_goaltime, race_goalpace, current_pb, current_mileage, current_frequency, current_othernotes = japanese_version()

    # Submit button
    if st.sidebar.button("Submit"):
        # Process the inputs
        st.session_state.race_days_until = race_days_until
        st.session_state.race_distance = race_distance
        st.session_state.race_goaltime = race_goaltime
        st.session_state.race_goalpace = race_goalpace
        st.session_state.current_pb = current_pb
        st.session_state.current_mileage = current_mileage
        st.session_state.current_frequency = current_frequency
        st.session_state.current_othernotes = current_othernotes


        output = get_trainingplan(language, race_day, race_days_until, race_distance, race_goaltime, race_goalpace, current_pb, current_mileage, current_frequency, current_othernotes)

        process_inputs(output)



def process_inputs(input1):
    # Function to display the final output
    # Process the inputs here
    st.write(input1)



if __name__ == "__main__":
    main()

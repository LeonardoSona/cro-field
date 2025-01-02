import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def load_sample_data():
    current_tasks = pd.DataFrame({
        'site': ['Boston Clinical Center', 'Chicago Research Lab'],
        'type': ['Site Inspection', 'Staff Training'],
        'due': ['2025-01-03', '2025-01-02'],
        'status': ['In Progress', 'Started'],
        'priority': ['High', 'Medium']
    })
    
    upcoming_tasks = pd.DataFrame({
        'site': ['NYC Medical', 'LA Research'],
        'type': ['Protocol Review', 'Deviation Assessment'],
        'due': ['2025-01-05', '2025-01-07'],
        'status': ['Pending', 'Not Started'],
        'priority': ['Medium', 'Low']
    })
    
    past_tasks = pd.DataFrame({
        'site': ['Miami Clinical', 'Seattle Center'],
        'type': ['Staff Training', 'Site Inspection'],
        'completed': ['2024-12-30', '2024-12-29'],
        'status': ['Completed', 'Completed'],
        'outcome': ['Passed', 'Issues Found']
    })
    
    return current_tasks, upcoming_tasks, past_tasks

def main():
    st.set_page_config(page_title="CRO Field Agent Dashboard", layout="wide")
    
    # Header
    st.title("Field Agent Dashboard")
    st.write(f"Current Date: {datetime.now().strftime('%Y-%m-%d')}")
    
    # Load data
    current_tasks, upcoming_tasks, past_tasks = load_sample_data()
    
    # Tab navigation
    tab1, tab2, tab3 = st.tabs(["Current Tasks", "Upcoming Tasks", "Past Tasks"])
    
    with tab1:
        st.subheader("Current Tasks")
        for _, task in current_tasks.iterrows():
            with st.expander(f"{task['site']} - {task['type']}"):
                cols = st.columns(3)
                cols[0].metric("Due Date", task['due'])
                cols[1].metric("Status", task['status'])
                cols[2].metric("Priority", task['priority'])
                
                if st.checkbox("Mark as Complete", key=f"complete_{task['site']}"):
                    st.success("Task marked as complete!")

    with tab2:
        st.subheader("Upcoming Tasks")
        for _, task in upcoming_tasks.iterrows():
            with st.expander(f"{task['site']} - {task['type']}"):
                cols = st.columns(3)
                cols[0].metric("Due Date", task['due'])
                cols[1].metric("Status", task['status'])
                cols[2].metric("Priority", task['priority'])

    with tab3:
        st.subheader("Past Tasks")
        for _, task in past_tasks.iterrows():
            with st.expander(f"{task['site']} - {task['type']}"):
                cols = st.columns(3)
                cols[0].metric("Completion Date", task['completed'])
                cols[1].metric("Status", task['status'])
                cols[2].metric("Outcome", task['outcome'])

    # Urgent Notifications
    st.sidebar.title("Urgent Notifications")
    st.sidebar.error("Protocol deviation reported at Boston Clinical Center")
    st.sidebar.warning("Staff certification expires in 5 days at Chicago Research Lab")

if __name__ == "__main__":
    main()

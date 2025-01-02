import streamlit as st
import pandas as pd
from datetime import datetime

def load_sample_data():
    # Dashboard data
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

    # Task manager data
    inspection_items = {
        'Physical Site Inspections': [
            'Temperature logs reviewed',
            'Storage conditions verified',
            'Equipment calibration checked',
            'Emergency protocols posted'
        ],
        'Staff Training': [
            'Protocol review completed',
            'GCP training verified',
            'Documentation procedures demonstrated',
            'Q&A session completed'
        ],
        'Protocol Deviations': [
            'Deviation type categorized',
            'Root cause analysis',
            'CAPA plan documented',
            'Regulatory reporting needed'
        ],
        'Site Relationships': [
            'Key staff contacts updated',
            'Communication preferences noted',
            'Upcoming milestones reviewed',
            'Site feedback collected'
        ],
        'Trial Procedures': [
            'Subject screening process',
            'Sample collection observed',
            'Data entry verified',
            'Protocol compliance confirmed'
        ],
        'Staff Competency': [
            'Role-specific assessments',
            'Required certifications verified',
            'Performance metrics reviewed',
            'Training needs identified'
        ]
    }
    
    return current_tasks, upcoming_tasks, past_tasks, inspection_items

def show_dashboard():
    st.title("Field Agent Dashboard")
    st.write(f"Current Date: {datetime.now().strftime('%Y-%m-%d')}")
    
    current_tasks, upcoming_tasks, past_tasks, _ = load_sample_data()
    
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

def show_tasks():
    st.title("Task Manager")
    
    _, _, _, inspection_items = load_sample_data()
    
    selected_category = st.selectbox(
        "Select Task Category",
        list(inspection_items.keys())
    )
    
    st.subheader(selected_category)
    
    for item in inspection_items[selected_category]:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            done = st.checkbox(item, key=f"task_{item}")
        with col2:
            if st.button("📷 Photo", key=f"photo_{item}"):
                st.info("Photo capture triggered")
        with col3:
            if st.button("📝 Note", key=f"note_{item}"):
                st.text_input("Add note:", key=f"note_input_{item}")

def main():
    st.set_page_config(page_title="CRO Field Agent App", layout="wide")
    
    # Navigation
    page = st.sidebar.radio("Navigation", ["Dashboard", "Tasks"])
    
    if page == "Dashboard":
        show_dashboard()
    else:
        show_tasks()
        
    # Urgent Notifications always visible
    st.sidebar.title("Urgent Notifications")
    st.sidebar.error("Protocol deviation reported at Boston Clinical Center")
    st.sidebar.warning("Staff certification expires in 5 days at Chicago Research Lab")

if __name__ == "__main__":
    main()

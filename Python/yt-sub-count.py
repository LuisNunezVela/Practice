from googleapiclient.discovery import build
import tkinter as tk
import time
import threading

# insert your own API key and channel ID
API_KEY = ''
CHANNEL_ID = ''

def get_subscriber_count():
    """Fetch subscriber count using YouTube Data API."""
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.channels().list(
        part="statistics",
        id=CHANNEL_ID
    )
    response = request.execute()
    return response['items'][0]['statistics']['subscriberCount']

def update_subscriber_count(label):
    """Continuously update the subscriber count in the label."""
    while True:
        try:
            subscriber_count = get_subscriber_count()
            label.config(text=f"Subscribers: {subscriber_count}")
        except Exception as e:
            label.config(text=f"Error: {e}")
        time.sleep(60)  # Update every 60 seconds

def show_window():
    """Display the subscriber count in a GUI window."""
    # Create the GUI window
    window = tk.Tk()
    window.title("Channel: teteiras")
    window.geometry("300x150")
    
    # Initial subscriber count
    label = tk.Label(window, text="Loading...", font=("Arial", 18))
    label.pack(pady=30)
    
    # Start a background thread to update the subscriber count
    threading.Thread(target=update_subscriber_count, args=(label,), daemon=True).start()
    
    # Run the GUI event loop
    window.mainloop()

if __name__ == "__main__":
    show_window()

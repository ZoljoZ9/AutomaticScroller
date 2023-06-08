import pyautogui
import time

# Set the duration and scroll amount
scroll_duration = 10  # Duration in seconds
scroll_amount = -100  # Scroll amount in pixels (negative for scrolling down)

# Wait for a few seconds before starting the scroll
time.sleep(5)

# Calculate the number of scroll steps based on the duration and scroll amount
num_steps = int(scroll_duration * 1000 / pyautogui.PAUSE)

# Perform the scrolling
for _ in range(num_steps):
    pyautogui.scroll(scroll_amount)
    time.sleep(0.001)  # Add a short delay between each scroll step

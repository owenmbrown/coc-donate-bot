import pygetwindow

window = pygetwindow.getWindowsWithTitle("Clash of Clans")[0]
print("Top:", window.topleft[1] + 40)
print("Left:", window.topleft[0] + 40)
print("Right:", window.bottomright[0] + 40)
print("Bottom:", window.bottomright[1])

print()


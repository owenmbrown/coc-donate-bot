### Progress Tracker

| Feature                                           | Status | Description                                 |
| ------------------------------------------------- | ------ | ------------------------------------------- |
| Open up COC from system                           | 🟥     |                                             |
| Opens Chat                                        | ✅     | Cdb_ClickChat.py                            |
| Finds & Clicks Donation Button                    | 🟥     |                                             |
| Donates what it can and remembers what to retrain | 🟥     |                                             |
| Finds & Clicks Barracks                           | ✅     | Cdb_OpenBarracks.py                         |
| Retrains/trains in barracks                       | 🟥     |                                             |
| Closes COC                                        | 🟥     | Leaves it in state where it can be reopened |
| Frontend w/ Electron                              | 🟥     |                                             |

**Status Legend:**

- ✅ - Done and Working
- 🟨 - Done but Needs Work (Bugs or Incomplete)
- 🟥 - Not Started / Not Functional

### Notes

- We should also maybe look into changing the OpenBarracks to be abstracted so we just input 2 images and it clicks the first one based off of the second one
- I think we should code tests for all of the functions

### Helper Files

See `\helpers` and `mousecurrentpixel.py` for helpers and add them there

- also realized we can resize the CoC window with pygetwindow so that might make things ezier if we choose to hard code certain things if its faster

### Future Features

- Maybe we could add where someone on a Discord channel requests something and it trains it and donates it
  - built in training timers for when it reopens and such

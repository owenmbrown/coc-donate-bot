### Progress Tracker

| Feature                                           | Status | Description                                                |
| ------------------------------------------------- | ------ | ---------------------------------------------------------- |
| Open up COC from system                           | 🟥     | Checks for update too                                      |
| Opens Chat                                        | ✅     | Cdb_ClickChat.py                                           |
| Finds & Clicks Donation Button                    | 🟥     |                                                            |
| Donates what it can and remembers what to retrain | 🟥     |                                                            |
| Finds & Clicks Barracks                           | ✅     | Cdb_OpenBarracks.py                                        |
| Retrains/trains in barracks                       | ✅     | Cdb_TrainTroop.py                                          |
| Closes COC                                        | 🟥     | Leaves it in state where it can be reopened                |
| Frontend w/ Electron                              | 🟥     |                                                            |
| Add Random px numbers to all clicks               | 🟥     | Will help stay undetected if we think this'll be a problem |
| Add all troop pngs                                | 🟨     | See Troop_Barbarian.png for reference                      |
| Pause all processes button on frontend            | 🟥     |                                                            |

**Status Legend:**

- ✅ - Done and Working
- 🟨 - Started
- 🟥 - Not Started

### Notes

- We should also maybe look into changing the OpenBarracks to be abstracted so we just input 2 images and it clicks the first one based off of the second one
- I think we should code tests for all of the functions

### Helper Files

const.currentArmy[troop]
See `\helpers` and `mousecurrentpixel.py` for helpers and add them there

- also realized we can resize the CoC window with pygetwindow so that might make things ezier if we choose to hard code certain things if its faster

### Future Features

- Maybe we could add where someone on a Discord channel requests something and it trains it and donates it
  - built in training timers for when it reopens and such
- Maybe add always-on-top functionality so we don't have to worry about something covering it while the process is going on

### BUGS

<span style="color:red;">\*</span> Occasionally in `Cdb_OpenBarracks.py` it glitches and cant find `trainTroops2.png`

<span style="color:red;">\*</span> On large resolutions `Cdb_TrainTroop.py` isn't working with the current barb image

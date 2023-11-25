# Installation guide for Android (using Termux)
Android installation can be done in two ways, the recommended one is using the
Termux app, the other way is to use PyDroid3. Using PyDroid3 is more straight
forward but it have some issues rendering the Frequency Distribution Table.

1. Install [Termux](https://termux.dev/en/) from
[F-Droid](https://f-droid.org/en/packages/com.termux) or from their
[GitHub Repo](https://github.com/termux/termux-app#github).
2. Open the Termux app and paste the following commands line-by-line to it and
then press to enter.
```sh
pkg update && pkg upgrade
pkg install python3 git nano
git clone https://github.com/M-MAD-Official/Descriptive_Statistics_Mobile.git
cd Descriptive_Statistics_Mobile
pip3 install -U prettytable
```
3. Now you should be able to run the program using the following command:
```sh
python3 main.py
```

Note 1: You can use `nano` inside Termux in order to enter your custom data to
the program, like this:
```sh
nano main.py
```
Then use Control+O to save the file and Control+X to exit nano (the Control
button is on the little bar above your Android keyboard).

Note 2: For next times trying to run the program after you exited the session
in the Termux, first run the `cd` command then run the command in step 3 to
run the program, like this:
```sh
cd Descriptive_Statistics_Mobile
python3 main.py
```

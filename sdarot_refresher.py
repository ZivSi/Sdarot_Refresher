import pyautogui
import time

MAX_TRIES = 100


def main():
    play_button = "" # Image of how the button looks like
    refresh_button = "" # Image of the refresh button
    tries = 0

    # Sleep for 5 sec to come to the chrome
    for i in range(5):
        time.sleep(1)
        print("Starting in " + str(5 - i))

    while tries < MAX_TRIES:
        coordinates_play = pyautogui.locateOnScreen(play_button, grayscale=True)

        print("Play coordinates:", coordinates_play)

        # Episode worked?
        if coordinates_play is not None:
            print("Episode loaded!")

            # Play it
            # pyautogui.click(coordinates_play) - if you want to start the episode automatically
            time.sleep(1.5)

            # TODO: Fix big screen
            pyautogui.doubleClick()

            exit()
        else:
            print("Failed. Refreshing...")
            # Didn't load - refresh page
            coordinates_of_refresh = pyautogui.locateOnScreen(refresh_button)
            pyautogui.click(coordinates_of_refresh)

            time.sleep(2)
            coordinates_of_reset = pyautogui.locateOnScreen(reset)
            pyautogui.click(coordinates_of_reset)

        tries += 1

        time.sleep(32)


if __name__ == '__main__':
    main()

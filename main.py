from game import Game

DEBUG = True


def run():
    """
    Main entry point. Runs the program depending on the given variables for different use cases.
    """
    if DEBUG:
        Game().start()

        while True:
            pass
        # pass  # Run Game regularly

    else:

        # Loop Forever
        while True:
            try:
                pass  # Run Game regularly

            except:
                pass  # If error happens, Log it


if __name__ == '__main__':

    run()

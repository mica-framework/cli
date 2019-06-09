import questions


def show():
    # initial initialization
    module, answer = questions.list('manager_menu', clear_console=True)
    endless_loop_counter = 10

    while True:
        if module == 'exit':
            print("Shutting down...")
            break

        endless_loop_counter -= 1
        if endless_loop_counter <= 0:
            print("Seems that we are in a endless loop..")
            module = 'exit'

from win10toast import ToastNotifier
import time
import threading


def doSomething(secs, message, icon):
    time.sleep(secs)
    try:
        # print('Counting: ' + message)
        while True:
            toaster = ToastNotifier()
            toaster.show_toast("Lembrete",
                               message,
                               icon_path=icon,
                               duration=10,
                               threaded=True)

            time.sleep(secs)
    except KeyboardInterrupt:
        print('Exiting ...')


if __name__ == '__main__':
    try:
        # Para iniciar sem problemas com o Windows
        time.sleep(60)

        threads = []

        threads.append(threading.Thread(target=doSomething, args=(60*20, "Dê uma olhada ao redor!", "eye.ico")))
        threads.append(threading.Thread(target=doSomething, args=(60*30, "Hora de se esticar um pouco!", "water.ico")))

        for t in threads:
            t.start()
            # Coloco um timer para que elas não ocorram muito próximas pois é lançado uma exceção
            time.sleep(20)

    except KeyboardInterrupt:
        print('Exiting ...')

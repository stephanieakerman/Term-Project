import sys
import multiprocessing
import subprocess

PYTHON_EXECUTABLE = sys.executable

def run_app():
    print("Running the website")
    subprocess.call([PYTHON_EXECUTABLE, 'app.py'])

def run_bot():
    print("Running the bot")
    subprocess.call([PYTHON_EXECUTABLE, 'bot.py'])

if __name__ == "__main__":
    app_process = multiprocessing.Process(target=run_app)
    bot_process = multiprocessing.Process(target=run_bot)

    app_process.start()
    bot_process.start()

    app_process.join()
    bot_process.join()

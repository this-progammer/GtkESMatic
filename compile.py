#-*compile.py*-

config_mkproj = 'gcc main.cpp -o GtkMatic.exe $(pkg-config --cflags --libs gtk+-3.0)'

def run_config():
  config_mkproj


run_config()

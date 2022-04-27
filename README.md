# PRE-REQUISITES: 

Both the GUI and the Web-app needs Python, and needs to be connected to a localhost server. Below are the steps to get your localhost server running for each OS: 
  - Windows
      - Make sure Python is installed on your machine: https://www.python.org/downloads/
      - Download XAMPP from: https://www.apachefriends.org/index.html
      - Open the XAMPP Application and run Apache and MySQL
      - Open your browser and type "localhost" in your address search bar
      - Click on "phpMyAdmin" in the top right corner of the page 
      - Import `hfyql1ju_csv_db_7.sql` and `hfyql1ju_segp.sql` into your server using the export button
  - macOS
      - Make sure Python is installed on your machine: https://www.python.org/downloads/macos/
      - Install phpMyAdmin for macOS: https://www.javatpoint.com/how-to-install-phpmyadmin-on-mac
      - Click on "phpMyAdmin" in the top right corner of the page 
      - Import `hfyql1ju_csv_db_7.sql` and `hfyql1ju_segp.sql` into your server using the export button
  - Linux:
      - Make sure Python is installed on your machine: https://opensource.com/article/20/4/install-python-linux
      - Install phpMyAdmin for Linux: https://www.linuxtechi.com/install-phpmyadmin-linux/
      - Click on "phpMyAdmin" in the top right corner of the page 
      - Import `hfyql1ju_csv_db_7.sql` and `hfyql1ju_segp.sql` into your server using the export button

# TO RUN THE SOFTWARE: 

  - Navigate to `__main__.py`
  - Run localhost server
  - Make sure database is set-up with the database files imported
  - Run `__main__.py`: 
     - Open any IDE of your choice 
     - Or Open your command prompt to the project directory and type `python __main__.py` and click enter
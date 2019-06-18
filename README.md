# robo-advisor

## SETUP
### repo setup
    1. Create new repository called robo-advisor (include gitignore file)
    2. Download repository to desktop
    3. After downloading the repo, navigate there from the command-line:

        ```sh
        cd ~/Desktop/robo-advisor
        ```

    4. Create new sub directory called app and add robo_advisor.py file to it
    5. Add the following contents to the file
        ```py
        # app/robo_advisor.py

        print("-------------------------")
        print("SELECTED SYMBOL: XYZ")
        print("-------------------------")
        print("REQUESTING STOCK MARKET DATA...")
        print("REQUEST AT: 2018-02-20 02:00pm")
        print("-------------------------")
        print("LATEST DAY: 2018-02-20")
        print("LATEST CLOSE: $100,000.00")
        print("RECENT HIGH: $101,000.00")
        print("RECENT LOW: $99,000.00")
        print("-------------------------")
        print("RECOMMENDATION: BUY!")
        print("RECOMMENDATION REASON: TODO")
        print("-------------------------")
        print("HAPPY INVESTING!")
        print("-------------------------")
        ```
    6. Create a requirements.txt file in the repo and add the following to it
        ```
        requests
        python-dotenv
        ```
### environment setup
    1. Create and activate a new Anaconda virtual environment:
        ```sh
        conda create -n stocks-env python=3.7 # (first time only)
        conda activate stocks-env
        ```
    2. From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:
        ```sh
        pip install -r requirements.txt
        pip install pytest # (only if you'll be writing tests)
        ```
    3. From within the virtual environment, demonstrate your ability to run the Python script from the command-line:
        ```sh
        python robo_advisor.py
        ```
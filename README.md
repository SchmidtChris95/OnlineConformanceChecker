# OnlineConformanceChecker
A prototype for an online conformance checker tool for industrial processes with manual steps.

## Main Requirements
- Python 3.9.5
- Flask 2.0.1
- Flask SocketIO 5.1.0
- Paho-mqtt 1.5.1
- For more requirements see [requirements.txt](https://github.com/SchmidtChris95/OnlineConformanceChecker/blob/master/requirements.txt)

## Installation
1. Install Python at least in version 3.9.5
2. Download the [source code](https://github.com/SchmidtChris95/OnlineConformanceChecker.git) of this prototype
3. Install pip via terminal to manage dependencies for Python. Run the following commands:
   ```bash
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python3 get-pip.py
   ```
4. Create and activate an isolated virtual Python environment within the downloaded source code folder:
   ```bash
   sudo pip install virtualenv
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Install all needed dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. To run the prototype, execute:
   ```bash
   flask run
   ```
## Usage
Open the webapp (running on localhost), start all modules and run the data producer to execute the prototype.

To switch the example business process, change the variables *active_process_set* and *active_process_lowLevelActivityTrace* at the end of the file [process.py](https://github.com/SchmidtChris95/OnlineConformanceChecker/blob/master/app/process.py) and restart the app.

```python
#######################################################
# Alle möglichen HLA aus dem aktiven Geschäftsprozess #
#######################################################

# active_process_set = BP_0_right["highlevelActivities"] 
# active_process_set = BP_0_left["highlevelActivities"] 
# active_process_set = BP_1["highlevelActivities"] 
active_process_set = BP_2_right["highlevelActivities"] 
# active_process_set = BP_2_left["highlevelActivities"] 

###########################################
# LowLevelActitity Trace für Dataproducer #
###########################################

# active_process_lowLevelActivityTrace = BP_0_right_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_0_left_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_0_right_alternative_wrong1_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_0_right_alternative_wrong2_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_0_right_alternative_wrong3_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_1_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_1_alternative_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_2_right_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_2_left_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_2_right_alternative_lowLevelActivityTrace 
# active_process_lowLevelActivityTrace = BP_2_right_alternative2_lowLevelActivityTrace 
# active_process_lowLevelActivityTrace = BP_2_right_alternative_wrong1_lowLevelActivityTrace
active_process_lowLevelActivityTrace = BP_2_right_alternative_wrong2_lowLevelActivityTrace 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

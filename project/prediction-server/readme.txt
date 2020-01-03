1. Download elmo model from: https://tfhub.dev/google/elmo/3
2. extract it to prediction-server/embed/

to run the server:
    1. open the directory 'prediction-server' - you need to BE INSIDE THE DIRECTORY in order for server to run correctly
    2. 'python3 prediction-service.py'

to test prediction:
    1. Open your brwoser
    2. enter the following url: http://127.0.0.1:5000/get_prediction/I%20want%20to%20die (assuming the server is running on localhost and port 500)

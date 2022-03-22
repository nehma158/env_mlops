# Start by importing the base image
FROM ubuntu:20.04

# Install python to container
RUN apt-get update && \ 
    apt-get install python3 -y && \
    apt install python3-pip -y

# Copy dataset, notebook & requirements.txt
COPY iris-analysis.ipynb requirements.txt ./

COPY data/iris.csv ./data/

# Install from requirements.txt
RUN python3 -m pip install -r requirements.txt

# On launch: run the notebook
#CMD ["jupyter", "nbconvert", "--to", "notebook", "--execute", "iris-analysis.ipynb"]
CMD ["jupyter", "notebook",  "--no-browser", "--ip", "0.0.0.0", "--port", "8888", "--allow-root"]


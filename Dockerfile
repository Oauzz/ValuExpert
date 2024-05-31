# Use the Miniconda base image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the environment.yml file into the container
COPY environment.yml /app/environment.yml

# Create the Conda environment and install the necessary packages
RUN conda env create -f /app/environment.yml

# Ensure the environment is activated and run the script
CMD ["/bin/bash", "-c", "source activate valuexp"]

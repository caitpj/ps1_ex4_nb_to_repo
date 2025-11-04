FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml && \
    conda clean -a -y

EXPOSE 8888

# Improved CMD with no token requirement for local development
CMD ["conda", "run", "-n", "ps1_ex4", "jupyter", "lab", \
     "--ip=0.0.0.0", "--port=8888", "--no-browser", \
     "--allow-root", "--NotebookApp.token=''", \
     "--NotebookApp.password=''"]




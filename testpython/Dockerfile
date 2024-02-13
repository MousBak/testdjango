#FROM python:3

#ENV PYTHONBUFFERD 1

#ENV PYTHONDONTWRTEBYTECODE 1

#RUN mkdir /app

#WORKDIR / app

#COPY Books /app/

#RUN python -m venv /env

#ENV PATH="/env/bin/:&PATH"

#COPY entrypoint.sh /app/entrypoint.sh

#RUN python -m pip install --upgrade pip

#COPY requirements.txt /app/

#RUN pip install -r requirements.txt




FROM python:3.8

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier entrypoint.sh et les autres fichiers nécessaires dans l'image
COPY entrypoint.sh /app/
COPY . /app/

# Donner les permissions d'exécution au script
RUN chmod +x /app/entrypoint.sh

# (Optionnel) Installer les dépendances si nécessaire
# RUN pip install -r requirements.txt

# Définir le script entrypoint.sh comme point d'entrée
ENTRYPOINT ["/app/entrypoint.sh"]
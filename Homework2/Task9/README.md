## Build a Python-Based Chatbot Application Backed by an LLM

There are two implementations: **DMR** and **Ollama (direct)**.

---

### DMR
This implementation creates a ChatGPT-like chatbot using **Streamlit** as the web UI and **smollm2** via **Docker Model Runner (DMR)** backed by Ollama.

In the `sample-app-dmr` directory, you’ll find the project files:

- [Dockerfile](./sample-app-dmr/Dockerfile)  
  Based on the [official Streamlit Docker tutorial](https://docs.streamlit.io/deploy/tutorials/docker), simplified for ease of use.  
  Most importantly, `pip install` commands are placed as early as possible in the Dockerfile to avoid unnecessary rebuild delays.

- [app.py](./sample-app-dmr/app.py)  
  The main chatbot application, largely adapted from the [official Streamlit conversational apps tutorial](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps).

- [docker-compose-dmr.yaml](./sample-app-dmr/docker-compose-dmr.yaml)  
  Used to run both the app and the smollm2 model.  
  Note: I couldn’t find a way to make the app explicitly depend on the model runner, so it’s left as-is.

#### How to Build & Run
Assuming DMR is enabled, run the following commands from the `sample-app-dmr` directory:

```shell
docker build -f Dockerfile -t streamlit-app:dmr .
```

Then start the containers:

```shell
docker compose -f docker-compose-dmr.yaml up
```

On success, you should see the app running at:  
[http://0.0.0.0:8501/](http://0.0.0.0:8501/)

---

### Ollama
This implementation creates a ChatGPT-like chatbot using **Streamlit** as the web UI and **smollm2** via **Ollama directly** (without DMR).

In the `sample-app-ollama` directory, you’ll find the project files:

- [Dockerfile](./sample-app-ollama/Dockerfile)  
  Same as the DMR version.

- [app.py](./sample-app-ollama/app.py)  
  Similar to the DMR version, with minor changes to the API calls.

- [docker-compose-ollama.yaml](./sample-app-ollama/docker-compose-ollama.yaml)  
  Defines three containers:
    - **ollama** – LLM backend
    - **pull-smollm2** – pulls the model
    - **streamlit-app-ollama** – the chatbot application

  A volume is also included to cache the model in the Ollama container between restarts.

#### How to Build & Run
Assuming Ollama is enabled, run the following commands from the `sample-app-ollama` directory:

```shell
docker build -f Dockerfile -t streamlit-app:ollama .
```

Then start the containers:

```shell
docker compose -f docker-compose-ollama.yaml up
```

On success, you should see the app running at:  
[http://0.0.0.0:8501/](http://0.0.0.0:8501/)
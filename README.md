# Neuro text to speech (TTS)

- create account on <https://platform.openai.com>
  - top up account with a few dollars
  - generate API key
- save API key to `.env` file in this folder
  - `OPENAI_API_KEY=...`
- install conda/mamba via <https://github.com/conda-forge/miniforge>
- run `mamba env create -f environment.yml`
- run `mamba activate openai`
- change mp3 file path in main.py if needed
- run `python main.py`
# auto-content-gen

This starter repo automates short-form content generation for RightBiz AI (TikTok + Instagram) from a JSON content plan.


## What you get
- `google-sheets-template.csv` — import to Google Sheets as the Content Engine
- `apps-script.js` — Google Apps Script to auto-generate one polished script daily
- `colab-notebook.py` — Colab-ready Python script to turn the generated script into a TikTok-ready MP4 (gTTS + Pexels + Whisper)
- `zapier-make-config.json` — template for the Zapier/Make workflow


## Quick setup
1. Import `google-sheets-template.csv` to Google Sheets and name the sheet **Content Engine**.
2. Open Extensions → Apps Script in the sheet and paste `apps-script.js`. Add a time trigger to run daily.
3. Open the `colab-notebook.py` in Google Colab, add your API keys (Pexels, OpenAI), and follow the notebook to connect Google Drive.
4. Configure a Zap (or Make scenario) to trigger the Colab script when a new “Generated” row appears in the sheet, save MP4 to Drive, and write back the video URL.
5. Use Meta Business Suite or Buffer to schedule posts using the generated MP4s and the `caption` / `hashtags` in the sheet.


## Notes
- This repo uses free-first tools: gTTS, Pexels free stock API, Whisper/OpenAI for transcription. Replace any API with your preferred provider.
- Keep API keys private. Use Google Secret Manager or environment variables when possible.

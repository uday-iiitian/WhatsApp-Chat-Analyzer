# WhatsApp Chat Analyzer

A small Streamlit app to analyze exported WhatsApp chats. It parses an exported chat file, preprocesses messages, and visualizes chat statistics such as message counts, timelines, activity maps, wordclouds, most common words and emojis.

## Features
- Parse WhatsApp exported chat text using timestamps like `[dd/mm/yy, h:mm:ss AM/PM]`.
- Compute basic statistics: total messages, total words, media shared, links shared.
- Monthly and daily timelines.
- Activity maps (most busy day/month and weekly heatmap).
- Most busy users (group-level analysis).
- Word cloud and most-common-words (uses a Hinglish stopword list in `stop_hinglish.txt`).
- Emoji frequency analysis.

## Requirements
The project lists the Python dependencies in `requirements.txt`. Key packages:

- streamlit
- pandas
- matplotlib
- seaborn
- urlextract
- wordcloud
- emoji

Install requirements with:

```bash
pip install -r requirements.txt
```

## Quickstart / Usage
1. Export a WhatsApp chat (text) from your phone and save it locally. The exporter should produce messages with timestamps like:

```
[24/10/25, 08:15:30 AM] Alice: Hello!
[24/10/25, 08:16:10 AM] Bob: Hi Alice
```

2. Run the Streamlit app from the repository root:

```bash
streamlit run app.py
```

3. In the app UI, upload the exported chat text file using the sidebar file uploader.
4. Select a user or `Overall` and click "Show Analysis" to view visualizations and tables.

## File overview
- `app.py` — Streamlit front-end. Handles file upload, UI controls, and plotting using functions from `helper.py` and `preprocessor.py`.
- `preprocessor.py` — Parses the raw exported chat text into a pandas DataFrame. Adds columns: `date`, `only_date`, `year`, `month_num`, `month`, `day`, `day_name`, `hour`, `minute`, and `period` for analysis.
- `helper.py` — Analysis helpers: `fetch_stats`, `most_busy_users`, `create_wordcloud`, `most_common_words`, `emoji_helper`, `monthly_timeline`, `daily_timeline`, `week_activity_map`, `month_activity_map`, `activity_heatmap`.
- `stop_hinglish.txt` — List of stopwords (English + Hinglish) used when creating the word cloud and common-words analysis.
- `requirements.txt` — Python dependencies.

## Input format details / assumptions
- The preprocessor expects timestamps in square brackets in the format `%d/%m/%y, %I:%M:%S %p` (12-hour format including seconds and AM/PM). Example: `[24/10/25, 08:15:30 AM]`.
- Messages that don't have a `User: ` prefix are treated as `group_notification`.
- Media placeholders are expected to appear as `<Media omitted>` or similar; the code filters messages that equal `'<Media omitted>\n'` in some places — if your export uses a different placeholder, you may need to adapt `helper.py`.

## Notes & potential improvements
- The regex in `preprocessor.py` currently looks for timestamps with seconds and AM/PM. If your export uses a slightly different timestamp format (e.g., no seconds or 24-hour clock), update the regex and datetime parsing accordingly.
- Wordcloud and stopword removal use `stop_hinglish.txt`. You can extend this list for better filtering.
- Some messages may include system notifications or forwarded tags; further cleaning could improve accuracy.

## Where this project is useful
This small tool is useful in several practical scenarios:

- Personal chat exploration: Quickly visualize who writes the most, busiest times, and commonly used words in your personal or family group chats.
- Community moderation / summary: For moderate-sized groups, identify the most active participants, common links shared, and emoji usage to help moderators summarize conversations.
- Research & analysis (non-sensitive): Academics or hobbyists can use the parser to analyze conversational patterns (temporal activity, frequently used words) from exported chats — ensure you have consent and remove personal identifiers before publishing any analysis.
- Quick reporting: Create simple visual snapshots for events (e.g., planning groups) to see participation levels and activity spikes.

Use it responsibly: WhatsApp chats often contain private information. Only analyze chats when you have permission and sanitize data before sharing results.

## Added example & tests
- `sample_chat.txt` — a small exported-chat example included for quick testing and demos.
- `tests/test_preprocessor.py` — a simple unit test that runs `preprocessor.preprocess` on the sample file and asserts expected columns and message counts.

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Contributors

- [UDAY DHAKAR](https://github.com/uday-iiitian)

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
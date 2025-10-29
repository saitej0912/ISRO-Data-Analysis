def save_summary_report(summary_text, filepath):
    with open(filepath, 'w') as f:
        f.write(summary_text)

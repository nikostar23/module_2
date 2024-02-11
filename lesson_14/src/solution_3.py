def report_generator(*pages):
    return (f"Page {i + 1}: {page}" for i, page in enumerate(pages))

report_pages = report_generator("Стр 1", "Стр 2")

print(report_pages)
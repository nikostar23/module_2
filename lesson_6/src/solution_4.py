def get_workers(name_workers: list) -> None:
    return f"Всего сотрудников: {len(name_workers)}"
    
    
print(get_workers(["Алекс", "Боб", "Сьюзи"]))

print(get_workers(["Сара", "Майкл",]))


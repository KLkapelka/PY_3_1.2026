ticket_ids = [101, 102, 103, 104]
statuses = ["open", "closed", "open", "open"]
priorities = ["low", "high", "high", "medium"]

# создание словаря, распаковка, zip (номер, "статус")
ticket_dict = {t_id: status for t_id, status in zip(ticket_ids, statuses)}
print(f"словарь заявок: {ticket_dict}")

# постоение списока номеров открытых заявок высокого приоритета
# new номер заявки. open, high
high_priority_open = [t_id for t_id, status, priority in zip(ticket_ids, statuses, priorities)
                      if status == "open" and priority == "high"]

print(f"ожидаемый список: {high_priority_open}")
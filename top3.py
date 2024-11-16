import shelve

with shelve.open('workers_hours') as db:
    workers = db['workers']

N=8
top_workers = []
for name, hours in workers.items():
    if hours > N:
        top_workers.append((name, hours))

top_workers = sorted(top_workers, key = lambda hour: hour[1], reverse = True)
top_3 = top_workers[:3]

print("Працівики з максимальною кількістю робочих годин: ")
for worker in top_3:
    print(worker[0], ":", worker[1], "годин")

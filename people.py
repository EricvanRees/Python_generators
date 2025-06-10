import memory_profiler
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Major', 'Engineering', 'CompSci', 'Arts', 'Business']

print(f'Memory (Before): {memory_profiler.memory_usage()}')


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


"""
Memory (Before): [51.671875]
Memory (After) : [275.75390625] - memory usage explodes
Took 0.892071100010071 seconds.
"""

t1 = time.perf_counter()
people = people_list(1000000)
t2 = time.perf_counter()

"""
Memory (Before): [51.48828125]
Memory (After) : [51.49609375] - almost no difference with "before", Python waits for user to yield the first value
Took 4.9000082071870565e-06 seconds.
"""


""" t1 = time.perf_counter()

people = people_generator(1000000)
# people = list(people_generator(1000000)) # lose performance boost
t2 = time.perf_counter() """

print(f'Memory (After) : {memory_profiler.memory_usage()}')
print(f"Took {t2-t1} seconds.")

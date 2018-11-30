#!/usr/bin/env python3

# with open('berlim.jpg', 'rb') as rf:  # binary mode
#     with open('berlim_copy.jpg', 'wb') as wf:  # binary mode
#         for line in rf:
#             wf.write(line)
#
# print('Done!')

# or

with open('berlim.jpg', 'rb') as rf:
    with open('berlim_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size) # para que o loop nao seja infinito,
            # precisamos ler novmanete o chunck_size

print('Done!')


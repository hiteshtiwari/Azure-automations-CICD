# mention the chunk of size. Below I have taken 68000
chunk_size = 68000

def write_chunk(part, lines):
    with open('<file path and name to save chunked data>'+ str(part) +'.csv', 'w') as f_out:
      # eg C:\\project\\mydirectory\\files_chunk_
        f_out.write(header)
        f_out.writelines(lines)

with open(<'Source file with path(absolute or relative)'>, "r") as f:
  #eg: C:\\project\\mydirectory\\source_files\\src_file_process.csv
    count = 0
    header = f.readline()
    lines = []
    for line in f:
        count += 1
        lines.append(line)
        if count % chunk_size == 0:
            write_chunk(count // chunk_size, lines)
            lines = []
    # write remainder
    if len(lines) > 0:
        write_chunk((count // chunk_size) + 1, lines)

import re


regexp = re.compile(r"^__version__\W*=\W*'([\d.abrd]+)'")
with open(
    r"E:\gaodakui\git\aiohttp-demos\demos\polls\aiohttpdemo_polls\__init__.py"
) as f:
    for line in f:
        match = regexp.match(line)
        if match is not None:
            print(match.group(1))
    # msg = "Cannot find version in aiohttpdemo_polls/__init__.py"
    # raise RuntimeError(msg)

import aiofiles


async def sanitize_tsv_file(file_path: str) -> None:
    async with aiofiles.open(file_path, "r") as tsv, aiofiles.open(
        "%s.clean" % (file_path), "w"
    ) as out:
        # Reader header
        await out.write(await tsv.readline())

        last_line = ""
        async for line in tsv.readlines():
            separated = line.split("\t")

            if separated[0].isdecimal():
                await out.write(last_line)
                last_line = line
            else:
                last_line = last_line.rstrip() + " " + line

        await out.write(last_line)

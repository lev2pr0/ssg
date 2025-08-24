


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    results = []
    for block in blocks:
        block = block.strip("\n")
        results.append(block)
    return results

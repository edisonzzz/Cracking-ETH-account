import requests

# 获取特定高度区块的 hash
def get_block_hash(block_number):
    url = "https://mainnet.infura.io/v3/xxx"  # 替换成你的 Infura 项目 ID
    headers = {"Content-Type": "application/json"}
    data = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [hex(block_number), False],
        "id": 1
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        if "result" in result and result["result"]:
            return result["result"]["hash"]
    return None

# 将区块 hash 写入到 txt 文件中
def write_hashes_to_txt(blocks_range):
    start_block, end_block = blocks_range
    with open(f"blocks_{start_block}_to_{end_block}_hashes.txt", "w") as file:
        for block_number in range(start_block, end_block + 1):
            block_hash = get_block_hash(block_number)
            if block_hash:
                file.write(f"{block_hash}\n")
            else:
                file.write(f"Failed to get hash for block {block_number}\n")
    print(f"区块 {start_block} 到 {end_block} 的 hash 已写入到文件中。")

# 主函数
def main():
    start_block = 100000  # 区块范围的起始高度
    end_block = 111111    # 区块范围的结束高度
    blocks_range = (start_block, end_block)
    write_hashes_to_txt(blocks_range)

if __name__ == "__main__":
    main()

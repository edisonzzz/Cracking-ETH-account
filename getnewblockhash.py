import requests

# 获取最新的10个区块的 hash
def get_latest_block_hashes():
    url = "https://mainnet.infura.io/v3/xxx"  # 替换成你的 Infura 项目 ID
    headers = {"Content-Type": "application/json"}
    data = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["latest", False],
        "id": 1
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        if "result" in result and result["result"]:
            latest_block_number = int(result["result"]["number"], 16)
            latest_block_hashes = []

            # 获取最新的10个区块的 hash
            for i in range(latest_block_number, latest_block_number - 100, -1):
                data["params"] = [hex(i), False]
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    block_result = response.json()
                    if "result" in block_result and block_result["result"]:
                        latest_block_hashes.append(block_result["result"]["hash"])
            return latest_block_hashes
    return None

# 将区块 hash 写入到 txt 文件中
def write_hashes_to_txt(hashes):
    if hashes:
        with open("latest_block_hashes.txt", "w") as file:
            for hash_value in hashes:
                file.write(hash_value + "\n")
        print("区块 hash 已写入到 latest_block_hashes.txt 文件中。")
    else:
        print("获取区块信息失败。")

# 主函数
def main():
    latest_block_hashes = get_latest_block_hashes()
    write_hashes_to_txt(latest_block_hashes)

if __name__ == "__main__":
    main()

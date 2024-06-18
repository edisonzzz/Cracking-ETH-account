import argparse
import hashlib
import ecdsa
import binascii

def generate_eth_address(private_key):
    # 使用哈希值生成私钥
    private_key_bytes = hashlib.sha256(private_key.encode()).digest()
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    
    # 生成公钥
    public_key = sk.get_verifying_key()
    public_key_bytes = public_key.to_string()
    public_key_hex = binascii.hexlify(public_key_bytes)
    
    # 计算地址
    sha3_256_hash = hashlib.sha3_256(public_key_bytes).hexdigest()
    eth_address = '0x' + sha3_256_hash[-40:]
    
    return eth_address

def main(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line.startswith('0x'):  # 如果行已经是哈希值，则直接使用
                private_key = line
            else:  # 否则，将其作为私钥生成哈希值
                private_key = hashlib.sha256(line.encode()).hexdigest()
            
            # 生成对应的以太坊地址
            eth_address = generate_eth_address(private_key)
            outfile.write(f"{eth_address}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Ethereum addresses from private keys.")
    parser.add_argument('-f', '--file', type=str, required=True, help="Path to the input file containing private keys.")
    args = parser.parse_args()
    
    input_file = args.file
    output_file = 'eth_addresses.txt'
    
    main(input_file, output_file)
    print(f"ETH addresses have been written to {output_file}")

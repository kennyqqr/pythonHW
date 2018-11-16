import json

jsonstr = '{"id": "0","jsonrpc": "2.0","result": {"address": "7BG5jr9QS5sGMdpbBrZEwVLZjSKJGJBsXdZLt8wiXyhhLjy7x2LZxsrAnHTgD8oG46ZtLjUGic2pWc96GFkGNPQQDA3Dt7Q","address_index": 5}}'
resultObj = json.loads(jsonstr)

# print(resultObj["result"]["address"])

tojsonstr = {
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "address": "7BG5jr9QS5sGMdpbBrZEwVLZjSKJGJBsXdZLt8wiXyhhLjy7x2LZxsrAnHTgD8oG46ZtLjUGic2pWc96GFkGNPQQDA3Dt7Q",
    "address_index": 5
  }
}

# toResult = json.dumps(tojsonstr)
# format output
toResult = json.dumps(tojsonstr, indent=2, separators=(" ", ":"))

print(toResult)
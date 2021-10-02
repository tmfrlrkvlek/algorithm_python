let n: Int = (Int(readLine() ?? "1") ?? 1) - 1
var b: [Character] = Array(String(n, radix: 2))
b.removeAll(where: { $0 == "0"})
print(b.count % 2)
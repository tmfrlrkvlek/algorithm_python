import Foundation

let input = (readLine() ?? "0 0 100").components(separatedBy: " ")
let n = Int(input[0])!, l = Int(input[2])!
var m = Int(input[1])!
var loc: [Int] = [l], d: [Int] = [Int](), c: [Int] = Array(repeating: 0, count: n + 1)

(readLine() ?? "0").components(separatedBy: " ").forEach{ loc.append(Int($0)!) }
loc.sort()

for (index, dest) in loc.enumerated() {
    guard index > 0 else { 
        d.append(dest) 
        continue
    }
    d.append(dest - loc[index - 1])
}

var cd = d.map{ $0 }
for _ in (0..<m) {
    let index = cd.firstIndex(of: cd.max()!)!
    c[index] += 1
    cd[index] = Int(ceil(Double(d[index]) / Double(c[index] + 1)))
}
print(cd.max()!)
import Foundation

let n = Int(readLine()!)!
var t = [Int]()
var p = [Int]()
var r = Array(repeating: 0, count: n)
for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map(){ Int(String($0))!}
    t.append(input[0]); p.append(input[1])
}
func dp(_ cr: Int) {
    guard n - cr >= t[cr] else { return }
    r[cr] = (r[(cr+t[cr])..<n] + [0]).max()!+p[cr]
}
(0..<n).reversed().forEach{ dp($0) }
print(r.max()!)
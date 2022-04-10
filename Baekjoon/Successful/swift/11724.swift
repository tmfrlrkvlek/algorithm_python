// 11724
import Foundation
var input = readLine()!.split(separator: " ").map(){Int(String($0))!}
let N = input[0], M = input[1]
var edges: [Int: [Int]] = [:]
for _ in 0..<M {
    input = readLine()!.split(separator: " ").map(){Int(String($0))!}
    let s = input[0], e = input[1]
    edges.updateValue((edges[s] ?? [])+[e], forKey: s)
    edges.updateValue((edges[e] ?? [])+[s], forKey: e)
}

var visited = Array<Bool>(repeating: false, count: N+1)
func DFS(_ s: Int) {
    var queue = [s]
    while !queue.isEmpty {
        let c = queue.removeLast()
        if visited[c] { continue }
        else { visited[c] = true }
        for e in edges[c] ?? [] where !visited[e] { queue.append(e) }   
    }
}

var count = 0
for s in 1...N where !visited[s] {
    count += 1
    DFS(s)
}
print(count)
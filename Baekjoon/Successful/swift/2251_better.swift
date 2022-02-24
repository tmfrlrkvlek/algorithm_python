// 2251
import Foundation

let input = readLine()!.split(separator: " ").map(){Int(String($0))!}

func bfs(_ A: Int, _ B: Int, _ C: Int) -> [Int] {
    var visit = Array<[Bool]>(repeating: Array<Bool>(repeating: false, count: B+1), count: A+1)
    var queue = [(0, 0)]
    while !queue.isEmpty {
        let node = queue.removeFirst()
        let a = node.0; let b = node.1; let c = C-node.0-node.1
        if visit[a][b] { continue }
        visit[a][b] = true
        if a > 0 {
            if a >= B-b { queue.append((a-B+b, B)) }
            else { queue.append((0, b+a))}
            if a >= C-c { queue.append((a-C+c, b)) }
            else { queue.append((0, b))}
        }
        if b > 0 {
            if b >= A-a { queue.append((A, b-A+a)) }
            else { queue.append((a+b, 0))}
            if b >= C-c { queue.append((a, b-C+c)) }
            else { queue.append((a, 0))}
        }
        if c > 0 {
            if c >= B-b { queue.append((a, B)) }
            else { queue.append((a, b+c))}
            if c >= A-a { queue.append((A, b)) }
            else { queue.append((a+c, b))}
        }
    }
    var result = Set<Int>()
    for b in 0..<B+1 where visit[0][b] { result.insert(C-b) }
    return Array(result).sorted()
}

bfs(input[0], input[1], input[2]).forEach() {print($0, terminator: " ")}
// 16236
import Foundation

let n = Int(readLine()!)!
var space = Array<[Int]>()
var sharkPos = (x: -1, y: -1)
var sharkSize = 2
for x in 0..<n {
    space.append(readLine()!.split(separator: " ").map(){Int(String($0))!})
    for (y, num) in space.last!.enumerated() where num == 9 {
        space[x][y] = 0
        sharkPos = (x: x, y: y)
    }
}

func bfs(x: Int, y: Int, n: Int, sharkSize: Int, space: [[Int]]) -> (pos: (x: Int, y: Int), time: Int) {
    var queue = [[x, y, 0]]
    var visited = Array<[Bool]>(repeating: Array(repeating: true, count: n), count: n)
    var fish = [[-1, -1, n*n+1]]
    while !queue.isEmpty {
        let a = queue.removeFirst()
        if fish.count > 1 && fish.last![2] < a[2] { break } 
        else if 1..<sharkSize ~= space[a[0]][a[1]] { fish.append(a); continue }
        else if !visited[a[0]][a[1]] || space[a[0]][a[1]] > sharkSize { continue }
        else { visited[a[0]][a[1]] = false }
        if a[0] != 0 { queue.append([a[0]-1, a[1], a[2]+1]) }
        if a[1] != 0 { queue.append([a[0], a[1]-1, a[2]+1]) }
        if a[1] != n-1 { queue.append([a[0], a[1]+1, a[2]+1]) }
        if a[0] != n-1 { queue.append([a[0]+1, a[1], a[2]+1]) }
    }
    fish.sort(){ (l, r) -> Bool in
        if l[2] < r[2] { return true }
        else if l[2] == r[2] {
            if l[0] < r[0] { return true }
            else if l[0] == r[0] {
                return l[1] < r[1]
            }
            else { return false }
        }
        else { return false }
    }
    return ((fish[0][0], fish[0][1]), fish[0][2])
}

var time = 0
var fishCount = 0
while true {
    let result = bfs(x: sharkPos.x, y: sharkPos.y, n: n, sharkSize: sharkSize, space: space)
    if result.pos.x < 0 { break }
    time += result.time
    sharkPos = result.pos
    fishCount += 1
    if fishCount == sharkSize {
        sharkSize += 1
        fishCount = 0
    }
    space[sharkPos.x][sharkPos.y] = 0
}
print(time)
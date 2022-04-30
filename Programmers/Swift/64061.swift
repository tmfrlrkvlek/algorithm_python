import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var stack: [Int] = []
    var result = 0
    var currentLocation = [board.count] + Array(repeating: board.count, count: board.count)
    for row in 0..<board.count {
        for col in 0..<board.count where currentLocation[col+1] == board.count && board[row][col] != 0 {
            currentLocation[col+1] = row
        }
    }
    for move in moves where currentLocation[move] < board.count {
        let doll = board[currentLocation[move]][move-1]
        switch (stack.last ?? 0) == doll {
        case true : 
            result += 2
            stack.removeLast()
        case false :
            stack.append(doll)
        }
        currentLocation[move] += 1
    }
    return result
}
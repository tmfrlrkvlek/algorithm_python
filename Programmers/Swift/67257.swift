import Foundation

func solution(_ expression:String) -> Int64 {
    let priorities: [[Operand]] = [[.plus, .minus, .multiple], [.plus, .multiple, .minus], [.minus, .plus, .multiple], [.minus, .multiple, .plus], [.multiple, .plus, .minus], [.multiple, .minus, .plus]]
    let nums: [Int64], operands: [Operand]
    (nums, operands) = split(expression)
    return priorities.reduce(Int64(0)) { before, priority in
        return [abs(calculate(priority: priority, nums: nums, operands: operands)), before].max() ?? 0
    }
}

func calculate(priority: [Operand], nums: [Int64], operands: [Operand]) -> Int64 {
    guard !priority.isEmpty else { return nums[0] }
    guard operands.contains(priority[0]) else { 
        var priority = priority; priority.removeFirst()
        return calculate(priority: priority, nums: nums, operands: operands)
    }
    var operands = operands, nums = nums
    for idx in 0..<operands.count where priority[0] == operands[idx] {
        let num1 = nums[idx], num2 = nums[idx+1]
        nums.remove(at: idx)
        operands.remove(at: idx)
        switch priority[0] {
        case .minus : nums[idx] = num1-num2
        case .plus : nums[idx] = num1+num2
        case .multiple : nums[idx] = num1*num2
        }
        return calculate(priority: priority, nums: nums, operands: operands)
    }
    return 0
}

enum Operand: Character, Equatable {
    case plus = "+", minus = "-", multiple = "*"
}

func split(_ expression: String) -> ([Int64], [Operand]) {
    var num: [Character] = []
    var nums: [Int64] = []
    var operands: [Operand] = []
    for c in Array(expression) {
        switch c {
        case "0"..."9" : num.append(c)
        default : 
            operands.append(Operand(rawValue: c) ?? Operand.plus)
            if !num.isEmpty {
                nums.append(Int64(num.reduce("") { "\($0)\($1)" })!)
                num = []
            }
        }
    }
    nums.append(Int64(num.reduce("") { "\($0)\($1)" })!)
    return (nums, operands)
}
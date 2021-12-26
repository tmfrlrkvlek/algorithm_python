import Foundation

func combination(_ nums:[Int], _ target: Int) -> [[Int]] {
    guard target > 0 else { return [[]] }
    @inline(__always)
    func combination(_ index: Int,_ current:[Int]) {
        guard current.count < target else { return result.append(current) }
        Array((index+1)..<(nums.count-target+current.count+1)).forEach() {combination($0, current + [nums[$0]])}
    }
    var result = [[Int]]()
    for i in 0...nums.count-target { combination(i, [nums[i]]) }
    return result
}
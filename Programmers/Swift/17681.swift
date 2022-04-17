func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    return zip(arr1, arr2).map() { num1, num2 in
        zip(String(num1, radix: 2).formatting(n), String(num2, radix: 2).formatting(n)).map() { c1, c2 in
            return c1 == "0" && c2 == "0" ? " " : "#"
        }.reduce("") { "\($0)\($1)" }
    }
}

extension String {
    func formatting(_ n: Int) -> [Character] {
        guard self.count < n else { return Array(self) }
        return Array(0..<n-self.count).map() { _ in "0"} + Array(self)
    }
}
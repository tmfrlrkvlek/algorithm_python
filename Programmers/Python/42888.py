def solution(record):
    record = [re.split() for re in record]
    idInfo = {line[1] : line[2] for line in record if len(line) > 2}
    return [idInfo[line[1]]+"님이 "+("들어왔습니다." if line[0] == "Enter" else "나갔습니다.") for line in record if line[0] != "Change"]
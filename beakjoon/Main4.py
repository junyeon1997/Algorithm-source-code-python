while True:
    str = input()
    stack = []
    checklst = ["(", ")", "[", "]"]
    for s in str:
        if s in checklst:
            if stack == []:
                stack.append(s)
            elif stack[-1] == checklst[0] and s == checklst[1]:
                stack.pop()
            elif stack[-1] == checklst[2] and s == checklst[3]:
                stack.pop()
            else:
                stack.append(s)
    if str == ".":
        break
    if stack == []:
        print("yes")
    else:
        print("no")

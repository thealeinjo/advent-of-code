# input = """
# px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}
#
# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}
# """

with open("input.txt") as f:
    input = f.read()

def parse_to_dict(input_str):
    # Removing the braces and splitting the string by commas
    pairs = input_str.strip('{}').split(',')
    # Splitting each pair by '=' and converting to a dictionary
    return {k: int(v) for k, v in (pair.split('=') for pair in pairs)}


def isPartInWorkflowParts(round, workflowparts):
    for currentWorkflowPart in workflowparts:
        if ":" in currentWorkflowPart:
            check = currentWorkflowPart.split(":")
            if '<' in check[0]:
                vergleich = check[0].split('<')
                if round.get(vergleich[0]) < int(vergleich[1]):
                    return check[1]
            if '>' in check[0]:
                vergleich = check[0].split('>')
                if round.get(vergleich[0]) > int(vergleich[1]):
                    return check[1]
        else:
            return currentWorkflowPart

def addAll(round):
    return round.get('x') + round.get('m') + round.get('a') + round.get('s');

def schleife(round, workflows):
    nextStep = 'in'
    index = 0
    while True:
        workflow = workflows[index]
        if nextStep == workflow.split("{")[0]:
            workflow = (workflow.split("{"))[1][:-1]
            workflowParts = workflow.split(',')
            nextStep = isPartInWorkflowParts(round, workflowParts)
            #print(nextStep)
            if nextStep == 'A':
                return addAll(round)
            if nextStep == 'R':
                return 0
        if index == len(workflows)-1:
            index = 0
        else:
            index += 1

# Splitting the string into lines
parts = input.split('\n\n')
rounds = parts[1].split('\n')
rounds = list(filter(None, rounds))
workflows = parts[0].split('\n')

count = 0
for round in rounds:
    round = parse_to_dict(round)
    count += schleife(round, workflows)

print("Solution is: " + str(count))


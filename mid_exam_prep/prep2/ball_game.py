from collections import deque

required_strength = [int(x) for x in input().split()]
needed_accuracy = deque(int(x) for x in input().split())

scored_goals = 0

while required_strength and needed_accuracy:
    current_strength = required_strength[-1]
    current_accuracy = needed_accuracy[0]
    total = current_strength + current_accuracy
    if total== 100:
        required_strength.pop()
        needed_accuracy.popleft()
        scored_goals += 1
    elif total < 100:
        if current_strength < current_accuracy:
            required_strength.pop()
        elif current_strength > current_accuracy:
            needed_accuracy.popleft()
        else:
            required_strength[-1] += current_accuracy
            needed_accuracy.popleft()
    else:
        required_strength[-1] -= 10
        needed_accuracy.rotate(-1)


if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals == 0:
    print("Paul failed to score a single goal.")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < scored_goals < 3:
    print("Paul failed to make a hat-trick.")

if scored_goals > 0:
    print(f"Goals scored: {scored_goals}")

if required_strength:
    print(f"Strength values left: {', '.join(map(str, required_strength))}")

if needed_accuracy:
    print(f"Accuracy values left: {', '.join(map(str, needed_accuracy))}")

# Lab 4 – VibeCoding: Fishing Game

## 1. Project Overview

This project is part of **Lab 4: VibeCoding**. The task was to use a Vibe Coding tool to inspect, fix, and extend a Python/Pygame fishing game.

The original game contained a deliberate catch-detection bug and required three additional features to be implemented.

**Repository:** `ankitasks-png/03_fishing`

---

## 2. Tasks Completed

### Task 1 – Fix Fish Catch Detection Bug

**Problem:**  
The original catch detection checked only whether the hook and fish were at approximately the same vertical/depth position. This could cause a fish to be caught even when the hook was not horizontally overlapping it.

**Fix:**  
Catch detection was changed to use Pygame rectangle collision detection.

```python
hook_rect = hook.get_rect()

for fish in fish_list:
    if hook_rect.colliderect(fish.get_rect()):
        return fish
```

This makes a catch possible only when the hook and fish actually overlap.

---

### Task 2 – Add Multiple Fish Types

Two different fish types were added with different:

- Movement speeds
- Sizes
- Colors
- Point values

Example:

```python
class SlowFish(Fish):
    def __init__(self, x, y):
        super().__init__(
            x, y,
            speed=1.5,
            width=32,
            height=16,
            point_value=10,
            color=(50, 150, 255)
        )


class FastFish(Fish):
    def __init__(self, x, y):
        super().__init__(
            x, y,
            speed=-4,
            width=44,
            height=22,
            point_value=25,
            color=(255, 165, 50)
        )
```

Different fish now award different scores when caught.

**Commit:** `792949c`

---

### Task 3 – Implement Player-Controlled Casting

**Feature:**  
The hook was changed from automatically casting to being controlled by the player.

- Press **Spacebar** to start a cast.
- The cast starts only when the hook is idle.
- The hook travels downward.
- It returns when it reaches maximum depth or catches a fish.
- Pressing Spacebar during an active cast does not interrupt it.

Example:

```python
def start_cast(self):
    if self.hook.state == IDLE:
        self.hook.start_cast()
```

---

### Task 4 – Implement 30-Second Round Timer

A 30-second countdown timer was added.

The final implementation includes:

- 30-second countdown
- Remaining time displayed on screen
- No catches after the timer reaches zero
- Round-over state
- Final score display
- New-round functionality
- Score reset when starting a new round
- Timer reset when starting a new round
- Fish and hook reset for a new round

The timer is based on:

```python
ROUND_DURATION = 30
```

A new round can be started using the **R** key after the round ends.

**Commit:** `6974aa8`

---

## 3. Additional Fix During Task 4

While implementing Task 4, an issue was observed where fish became invisible while the hook was casting.

The fish visibility and movement behavior was corrected so that:

- Fish remain visible while the hook is casting.
- Fish continue moving normally.
- The existing hook behavior was preserved.
- The Task 1 catch-detection logic was preserved.

This was completed as part of the final Task 4 implementation.

---

## 4. Controls

| Key | Action |
|---|---|
| **Spacebar** | Start casting the hook |
| **R** | Start a new round after the round ends |
| **Close Window** | Exit the game |

---

## 5. Before vs After Videos

### Before Video

The **Before** video is a 10-second recording of the original game before making any code changes.

It provides evidence of the starting state and the original behavior/bug.

**Before Video:**  
[Paste Before Video Link Here]

### After Video

The **After** video is a 10-second recording of the completed game after implementing Tasks 1–4.

It demonstrates the final functionality, including:

- Correct fish catching
- Multiple fish types
- Player-controlled casting
- Timer
- Score
- Round-over behavior

**After Video:**  
[Paste After Video Link Here]

---

## 6. Vibe Coding Prompts Used

### Prompt 1 – Fix Fish Catch Detection Bug

> Fix the catch detection bug in Task 1 from the README. The hook should only catch a fish when they actually overlap, not just when they are at the same depth. Keep the rest of the game unchanged.

### Prompt 2 – Add Multiple Fish Types

> Now implement Task 2 from the README.
>
> Add at least 2 different fish types with different movement speeds and point values. Make them visually different using color and/or size, and make sure the correct points are awarded when each type is caught.
>
> Keep the Task 1 fix working, and don't implement Tasks 3 or 4 yet.

### Prompt 3 – Implement Player-Controlled Casting

> Now implement Task 3 from the README.
>
> Make casting player-controlled: pressing a key should start the cast when the hook is idle. The hook should travel down and return when it reaches maximum depth or catches a fish. A new cast must not interrupt an active cast.
>
> Keep Tasks 1 and 2 working, and don't implement Task 4 yet.

### Prompt 4 – Fix Fish Visibility and Implement 30-Second Round Timer

> The fish are visible when the hook is at the surface, but when the hook casts down, the fish disappear from the screen. Because of this, the hook cannot catch them.
>
> Inspect the existing code and fix ONLY this problem: fish must remain visible and keep moving while the hook is casting. Send me the entire code files for the same.
>
> Do not change Tasks 1, 2, 3 or logic.
>
> Do not change the hook or catch detection.
>
> Give me the exact complete file(s) to replace.
>
> And implement Task 4:
>
> Add a 30-second countdown for the round. Display the remaining time on screen. Once it reaches zero, no further catches should be possible, the round should end, and the final score should be shown clearly. Provide a way to start a new round with the score and timer both reset.

---

## 7. Git Commit History

The project was implemented using separate commits for the tasks.

```text
6974aa8  Complete Task 4: add round timer and final game fixes
[Task 3 commit]  Implement Task 3: player-controlled casting
792949c  Implement Task 2: multiple fish types
[Task 1 commit]
```

> The Task 1 and Task 3 commit hashes can be obtained directly from the GitHub repository history.

---

## 8. Chat History Evidence

The Vibe Coding prompts were entered in a separate ChatGPT conversation.

**Chat History / ChatGPT Link:**  
[Paste ChatGPT Conversation Link Here]

The chat history provides evidence of the prompts used to implement the tasks.

---

## 9. Project Setup

### Requirements

- Python 3.10+
- Pygame

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Game

From the project folder:

```bash
python main.py
```

---

## 10. Submission Checklist

- [x] Forked repository
- [x] Original game tested
- [x] 10-second Before video recorded
- [x] Task 1 completed
- [x] Task 2 completed
- [x] Task 3 completed
- [x] Task 4 completed
- [x] 10-second After video recorded
- [x] Separate task commits made
- [x] Changes pushed to personal GitHub repository
- [x] No Pull Request raised to the main `SETAPESU26` repository
- [ ] Before video link added
- [ ] After video link added
- [ ] Chat history link added
- [ ] Final PDF evidence prepared

---

## 11. Conclusion

The Fishing Game was successfully updated using Vibe Coding. The original catch-detection bug was fixed, multiple fish types were added, casting was made player-controlled, and a 30-second round system was implemented while preserving the required functionality from the earlier tasks.

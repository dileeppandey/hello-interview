# Group Anagrams — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Given a list of words, put all anagrams into the same group.

**Inputs**: List of strings.
**Output**: List of lists, where each inner list contains strings that are anagrams of each other.
**Constraints**: `1 <= strs.length <= 10^4`, `0 <= strs[i].length <= 100`, lowercase English letters only.

**What makes two strings anagrams?** They contain exactly the same characters with the same frequencies, just in different order. "eat" and "tea" both have {a:1, e:1, t:1}.

## 2. Building Intuition

**What category?** This is a **grouping/classification** problem. We need a way to identify which group each string belongs to.

**Key question**: How do I create a unique identifier (a "canonical form") for each anagram group?

**Two approaches**:
1. **Sort the characters**: "eat" → "aet", "tea" → "aet" — same key!
2. **Character frequency count**: "eat" → (1,0,0,0,1,0,...,1,0,...) — same count tuple!

Both work. Sorting is simpler to implement; frequency count is slightly faster for long strings.

## 3. Brute Force First

**Naive approach**: Compare every pair of strings to check if they're anagrams (by sorting both and comparing). Then use union-find or similar to group them.

**Complexity**: O(n² · k log k) where k is max string length. Comparing all pairs is O(n²), sorting each string is O(k log k).

**Why insufficient?** Quadratic in the number of strings.

## 4. Identifying the Optimization

**Key insight**: Instead of comparing pairs, compute a **canonical key** for each string. Strings with the same key are anagrams. Use a hash map to collect strings by key.

**Why this works**: The canonical form (sorted string) is a *deterministic function* of the character set. All anagrams map to the same key. Non-anagrams map to different keys.

**From O(n²) to O(n)**: We process each string exactly once, doing O(k log k) work per string for sorting.

## 5. Building the Solution Step-by-Step

```
groups = defaultdict(list)

For each word in strs:
    key = sorted(word)        ← canonical form
    groups[key].append(word)  ← add to its group

return list(groups.values())
```

**Dry-run**: `["eat", "tea", "tan", "ate", "nat", "bat"]`
```
"eat" → key="aet" → groups={"aet": ["eat"]}
"tea" → key="aet" → groups={"aet": ["eat","tea"]}
"tan" → key="ant" → groups={"aet": ["eat","tea"], "ant": ["tan"]}
"ate" → key="aet" → groups={"aet": ["eat","tea","ate"], "ant": ["tan"]}
"nat" → key="ant" → groups={"aet": ["eat","tea","ate"], "ant": ["tan","nat"]}
"bat" → key="abt" → groups={"aet": [..], "ant": [..], "abt": ["bat"]}
```

**Edge cases**:
- Empty strings: `["", ""]` → both have sorted key `""` → grouped together
- Single character: `["a"]` → one group
- No anagrams: each word is unique → each in its own group

## 6. Complexity Analysis

**Time**: O(n · k log k) — n strings, each sorted in O(k log k) where k = max string length.
**Space**: O(n · k) — storing all strings in the hash map.

**Alternative**: Use character count tuple as key for O(n · k) time (avoiding sorting), but in practice sorting is fast enough for `k ≤ 100`.

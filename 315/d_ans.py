#!/usr/bin/env python3
h, w = map(int, input().split())
cookies = [[char for char in input()] for _ in range(h)]
checked = [[False] * w for _ in range(h)]


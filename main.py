def juft_sonlar_roxati(sana):
    juft_sonlar = [son for son in sana if son % 2 == 0]
    return juft_sonlar

sana = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(juft_sonlar_roxati(sana))
```

```python
def juft_sonlar_roxati(sana):
    return [son for son in sana if son % 2 == 0]

sana = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(juft_sonlar_roxati(sana))

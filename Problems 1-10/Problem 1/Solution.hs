-- Sum all x when x ranges from 1 to 999 (incrementing by +1) only when x is divisible by 3 or 5.
sum [x | x <- [1..999], x `mod` 3 == 0 || x `mod` 5 == 0]
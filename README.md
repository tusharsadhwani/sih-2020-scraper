# sih-2020-scraper
A Python script that scrapes all of SIH 2020 problem statements and lets you search through them easily.

# How to use

```
git clone https://github.com/tusharsadhwani/sih-2020-scraper
cd sih-2020-scraper
```

To load the SIH 2020 problem statements, you'll have to run the `store_problems()` function, for eg.

1. comment out the `if __name__ == '__main__'` block from `__main__.py`
2. run the following:

  ```
  python -i __main__.py
  >>> store_problems()
  >>>
  ```

  It will take a minute to complete.

3. Verify that a new file named `problems.pickle` is created.
4. Uncomment the previously commented block.
5. To run:

```
cd ..
python sih-2020-scraper
```

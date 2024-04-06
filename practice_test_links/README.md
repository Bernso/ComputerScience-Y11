# How this was done

The entire document was pasted into a text file.

Grep was used with PCRE, then a simple bash loop outputs links:

```bash
# just get the links and output to links file
grep -Po "isaaccs.org\S+" gcse_comp  > links
# prepend each line of the links file with https://
for item in $(cat links) ; do echo https://${item} ; done
```

This was pasted into the [q_and_a.md](https://github.com/Bernso/ComputerScience-Y11/blob/main/practice_test_links/q_and_a.md) file.

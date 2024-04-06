# How this was done

The entire document was pasted into a text file.

You can learn more about regular expressions "regex" at [Regex101 Website](https://regex101.com/) - everyone uses this.  Excellent site.

Grep was used with PCRE, then a simple bash loop outputs links:

```bash
# just get the links and output to links file
grep -Po "isaaccs.org\S+" gcse_comp  > links
# prepend each line of the links file with https://
for item in $(cat links) ; do echo https://${item} ; done
```

This was pasted into the [q_and_a.md](https://github.com/Bernso/ComputerScience-Y11/blob/main/practice_test_links/q_and_a.md) file.

## Practice Testing

Output the links to clickables file:

```bash
for item in $(cat links) ; do echo https://${item} >> clickables ; done
```


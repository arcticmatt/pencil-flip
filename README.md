# pencil-flip
my blog  
[blog.pencilflip.com](http://blog.pencilflip.com/)


## instructions for myself

I always forget how to update this thing. I have this alias in my `.zshrc`. 

```
alias activate_pelican='cd ~/virtualenvs/pelican && source bin/activate && cd -'
```

1. Run `activate_pelican`
2. Make some changes. Remember to change the date in the headers.
3. Commit and push changes.

https://docs.getpelican.com/en/3.3.0/tips.html has some info about `.git/hooks/post-commit`.

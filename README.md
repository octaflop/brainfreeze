# BrainFreeze

*BrainFreeze* is just another quick-and-dirty blogging application that utilizes flask for templating and freezes to static pages with the possibility of future dynamic hosting — in particular, the expectation is to create an author view with in-page editing using jsonp or CORS.

## Installation
To keep JS and bootstrap CSS out of the repo, we use bower (you will need npm installed). You will also need to enable `git subtree` for bootstrap-glyphicons installation.

```bash
$ cd assets
$ npm install -g bower
$ bower install bootstrap
$ sudo chmod +x /usr/share/doc/git/contrib/subtree/git-subtree.sh
$ sudo ln -s /usr/share/doc/git/contrib/subtree/git-subtree.sh /usr/lib/git-core/git-subtree
$ git subtree
```

The symlinks should take care of the rest.


---
title: Hello, world
description: A first post for the new blog, and a quick tour of what a post can look like.
image: /images/photos/Z72_1609.jpg
---

This is the first post on the new blog. It lives right alongside my work and photos, and every post is just a Markdown file in the site's repo. Writing one should be as easy as opening an editor.

<!--more-->

This post is a sample. It shows off the formatting the blog supports, so swap it out for something real whenever you're ready.

## Text and lists

Paragraphs, **bold**, *italics* and [links](https://github.com/phillfarrugia) all work the way you'd expect. Lists too:

- Bullet points for quick thoughts
- Numbered lists for steps
- Inline `code` for short snippets

> Pull quotes are set in the same serif as the site name, for the lines worth slowing down on.

## Code

Fenced code blocks get syntax highlighting:

```swift
struct Post: Identifiable {
    let id = UUID()
    let title: String
    let publishedAt: Date

    var isRecent: Bool {
        publishedAt > .now.addingTimeInterval(-7 * 24 * 60 * 60)
    }
}
```

## Photos

![A photo from my portfolio](/images/photos/Z72_1609.jpg)
*Captions go on the line right after the image, in italics.*

---

That's everything. Thanks for reading.

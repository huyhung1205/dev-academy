# CLAUDE.md

## Role

You are assisting with the `dev-academy` project.

You must act as a careful frontend developer and course content generator.

## Project Summary

`dev-academy` is a static GitHub Pages website for learning programming and computer science.

It supports multiple courses.

Each course contains lessons with:

1. Video mô phỏng
2. Tài liệu lý thuyết
3. Ví dụ minh họa
4. Trắc nghiệm bằng JavaScript
5. Câu hỏi tự luận tự ôn tập
6. Đáp án tham khảo

## Mandatory Behavior

When the user says:

```txt
Tạo khóa học "Course Name".

Nội dung lý thuyết gồm:
[content]
```

you must automatically create the complete course.

Do not ask the user where to place files unless absolutely necessary.

Do not only generate text.

You must create or modify the actual project files.

## Files To Read First

Before implementing course generation, read:

```txt
AGENTS.md
CLAUDE.md
.spec
.rules
.workflows
```

Then follow them strictly.

## Automatic Course Generation Requirements

For every new course, create:

```txt
courses/<course-slug>/
├── index.html
└── lessons/
    ├── lesson-01.html
    ├── lesson-02.html
    ├── lesson-03.html
    ├── lesson-04.html
    └── lesson-05.html
```

If the provided theory content should be split into more lessons, create more lesson pages.

If fewer lessons are appropriate, fewer pages are allowed only when the user content clearly requires it.

## Course Overview Page

The course overview page must include:

- Course title
- Course description
- Learning objectives
- Lesson list
- Start learning button
- Link back to homepage
- Link back to courses page if it exists

## Lesson Page Requirements

Every lesson page must include:

- Global navbar
- Course sidebar or table of contents
- Lesson title
- Short introduction
- Video mô phỏng section
- Theory section
- Example section
- Quiz section
- Essay self-study section
- Suggested answer section
- Previous and next lesson links
- Footer

## Homepage Update Requirement

When creating a new course, update:

```txt
index.html
```

Add the new course to the homepage course list as a card, sidebar item, or menu item.

If the homepage already has a course section, follow the existing style.

If the homepage does not have a course section, create one.

## Courses Page Update Requirement

If this file exists:

```txt
courses.html
```

update it and add the new course.

If it does not exist, do not create it unless it is useful for the current structure.

## Responsive Design Requirement

All generated pages must work on:

- Mobile
- Tablet
- Laptop
- Desktop

Use Bootstrap grid:

```html
<div class="container">
  <div class="row">
    <aside class="col-12 col-lg-3"></aside>
    <article class="col-12 col-lg-9"></article>
  </div>
</div>
```

## JavaScript Requirements

Quiz:

- Must run in the browser.
- Must calculate score.
- Must display result.
- Must not require backend.

Essay:

- Must not be graded.
- Must include a textarea.
- Must include a button to show suggested answer.

## Style Requirements

- Clean educational interface.
- Consistent cards and buttons.
- Readable spacing.
- Good mobile experience.
- Use Bootstrap where appropriate.
- Avoid complex animations.

## Path Requirements

Use relative paths.

Examples from a lesson page:

```html
<link rel="stylesheet" href="../../../assets/css/style.css">
<a href="../index.html">Tổng quan khóa học</a>
<a href="../../../index.html">Trang chủ</a>
```

## Final Report

After making changes, report:

```txt
Created files:
- ...

Modified files:
- ...

What was added:
- Course folder
- Lesson pages
- Sidebar
- Quiz
- Essay section
- Homepage course card
```

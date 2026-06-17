# .spec

## Product Name

dev-academy

## Product Type

Static educational website hosted on GitHub Pages.

## Product Goal

Create a simple and expandable learning platform for programming, computer science, software engineering, and AI Agent Engineering.

## Target Users

- Beginners learning programming
- Students learning Data Structures and Algorithms
- Learners studying software engineering
- Learners studying AI Agent Engineering
- Learners who want theory, video, quiz, and self-study exercises

## Core Technologies

Use:

- HTML
- CSS
- JavaScript
- Bootstrap
- GitHub Pages

Avoid:

- Backend
- Database
- Login system
- Online compiler
- AI grading
- Build tools

unless explicitly requested.

## Initial Courses

The project may include these initial courses:

```txt
courses/
├── programming-fundamentals/
├── data-structures/
├── algorithms/
└── agent-engineering/
```

## Standard Course Requirements

Every course must include:

- Course overview page
- Lesson pages
- Sidebar or table of contents
- Responsive layout
- Homepage course card
- Internal navigation links

## Standard Course Folder Structure

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

## Course Overview Page Specification

Each course overview page must include:

```txt
1. Course title
2. Course description
3. Target learners
4. Learning objectives
5. Lesson list
6. Start learning button
7. Back to homepage link
8. Back to courses page link if available
```

## Lesson Page Specification

Each lesson page must include:

```txt
1. Global navbar
2. Course sidebar / table of contents
3. Lesson title
4. Short introduction
5. Video mô phỏng
6. Tài liệu lý thuyết
7. Ví dụ minh họa
8. Trắc nghiệm bằng JavaScript
9. Câu hỏi tự luận tự ôn tập
10. Đáp án tham khảo
11. Previous / Next lesson navigation
12. Footer
```

## Video Section Specification

The video section must:

- Appear near the beginning of the lesson.
- Support embedded YouTube videos.
- Use a placeholder if no video is provided.

Placeholder text:

```txt
Video mô phỏng sẽ được cập nhật sau.
```

## Theory Section Specification

The theory section must:

- Be written in Vietnamese.
- Be beginner-friendly.
- Use headings and short paragraphs.
- Include examples when possible.
- Include code blocks when relevant.

## Quiz Specification

Each lesson should include 3 to 5 multiple-choice questions.

Quiz must:

- Use JavaScript
- Run in the browser
- Show score immediately
- Not require backend
- Not require login

## Essay Self-Study Specification

Each lesson should include 1 to 3 essay/self-study questions.

Essay section must:

- Provide a textarea
- Provide a suggested answer
- Hide suggested answer by default
- Show suggested answer when the learner clicks a button
- Not calculate score
- Not auto-grade

## Homepage Integration Specification

When a new course is created, the AI must update:

```txt
index.html
```

The homepage must display the new course as one of:

- Course card
- Sidebar item
- Menu item
- Course list item

Preferred format:

```html
<div class="col-md-6 col-lg-4">
  <div class="card h-100">
    <div class="card-body">
      <h3 class="card-title">Course Name</h3>
      <p class="card-text">Short course description.</p>
      <a href="courses/course-slug/index.html" class="btn btn-primary">Bắt đầu học</a>
    </div>
  </div>
</div>
```

If the existing homepage already has a different design, follow the existing design.

## Responsive Specification

The layout must work on:

- Mobile
- Tablet
- Laptop
- Desktop

Use this general pattern for lesson pages:

```html
<main class="container my-4">
  <div class="row">
    <aside class="col-12 col-lg-3 mb-4">
      Sidebar
    </aside>

    <article class="col-12 col-lg-9">
      Lesson content
    </article>
  </div>
</main>
```

## Out of Scope

Do not implement these unless the user explicitly requests them:

- User account
- Login/register
- Database
- Backend server
- Online judge
- Automatic code grading
- AI essay grading
- Payment
- Admin dashboard
- Complex frontend framework

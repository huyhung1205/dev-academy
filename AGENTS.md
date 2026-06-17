# AGENTS.md

## Project Name

dev-academy

## Project Type

Static educational website hosted on GitHub Pages.

## Main Goal

`dev-academy` is a learning platform for programming, computer science, software engineering, and AI Agent Engineering.

The website must be simple, expandable, responsive, and easy to maintain.

## Tech Stack

Use only:

- HTML
- CSS
- JavaScript
- Bootstrap
- GitHub Pages
- LocalStorage if needed

Do not use:

- Backend server
- Database
- React
- Vue
- Angular
- Node.js build system
- Supabase
- Firebase
- Login/register
- AI auto-grading
- Online compiler

unless the user explicitly requests it.

## Most Important Automation Rule

When the user gives a prompt like:

```txt
Tạo khóa học "Course Name".

Nội dung lý thuyết gồm:
[content]
```

the AI must automatically:

1. Read and follow:
   - `AGENTS.md`
   - `CLAUDE.md`
   - `.spec`
   - `.rules`
   - `.workflows`

2. Create a new course folder:

```txt
courses/<course-slug>/
```

3. Create a course overview page:

```txt
courses/<course-slug>/index.html
```

4. Automatically split the provided theory content into suitable lessons.

5. Create lesson pages:

```txt
courses/<course-slug>/lessons/lesson-01.html
courses/<course-slug>/lessons/lesson-02.html
courses/<course-slug>/lessons/lesson-03.html
courses/<course-slug>/lessons/lesson-04.html
courses/<course-slug>/lessons/lesson-05.html
```

If the content naturally needs more or fewer lessons, adjust the number of lessons.

If the user only provides a course name and no lesson count, create at least 5 lessons.

6. Each lesson page must include:
   - Video mô phỏng
   - Tài liệu lý thuyết
   - Ví dụ minh họa
   - Trắc nghiệm bằng JavaScript
   - Câu hỏi tự luận tự ôn tập
   - Đáp án tham khảo

7. Create sidebar or table of contents for the course.

8. Add previous/next navigation between lessons.

9. Update the main website homepage:

```txt
index.html
```

The homepage must include a new course card/sidebar/menu item for the generated course.

10. Update the courses list page if it exists:

```txt
courses.html
```

11. Ensure all pages are responsive for:
   - Mobile
   - Tablet
   - Laptop
   - Desktop

12. Use relative paths so everything works on GitHub Pages.

13. Summarize all created and modified files.

## Default Course Folder Structure

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

## Default Lesson Structure

Every lesson must follow this order:

```txt
1. Lesson title
2. Short introduction
3. Video mô phỏng
4. Tài liệu lý thuyết
5. Ví dụ minh họa
6. Trắc nghiệm
7. Câu hỏi tự luận tự ôn tập
8. Đáp án tham khảo
9. Previous / Next lesson navigation
```

## Layout Rules

Every lesson page should use this layout:

```html
<header>
  Global navbar
</header>

<main class="container my-4">
  <div class="row">
    <aside class="col-12 col-lg-3 mb-4">
      Course sidebar / table of contents
    </aside>

    <article class="col-12 col-lg-9">
      Lesson content
    </article>
  </div>
</main>

<footer>
  Footer
</footer>
```

## Course Sidebar Rules

The sidebar must include:

- Course overview link
- All lesson links
- Active lesson highlight if possible

On laptop and desktop:

- Sidebar appears on the left.

On mobile:

- Sidebar appears above the lesson content or collapses.

## Homepage Update Rule

When creating a new course, always update `index.html`.

The homepage should include a course card like:

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

If the homepage already has a different course card style, follow the existing style.

## Quiz Rules

- Quiz must be implemented using JavaScript.
- Do not use backend.
- Do not require login.
- Show score immediately after submit.
- Highlight correct and wrong answers if possible.
- A lesson should normally include 3 to 5 multiple-choice questions.

## Essay Rules

- Essay questions are self-study only.
- Do not automatically grade essay answers.
- Provide suggested answers.
- The learner may compare their own answer with the suggested answer.
- Optional draft saving can use LocalStorage.

## Content Language Rules

- Use Vietnamese for user-facing course content.
- Use English for file names and folder names.
- Use clear and beginner-friendly explanations.
- Use examples whenever possible.

## File Naming Rules

Use lowercase and hyphenated names.

Good:

```txt
agent-engineering
programming-fundamentals
data-structures
binary-search.html
what-is-ai-agent.html
```

Bad:

```txt
Agent Engineering
Bai 1.html
Lesson01Final.html
```

## Final Response Rule

After completing any course generation, the AI must summarize:

```txt
Created:
- file 1
- file 2

Modified:
- index.html
- courses.html

Notes:
- Course added to homepage
- Sidebar created
- Quiz JavaScript included
```

# AGENTS.md

########################################################
# PROJECT INFORMATION
########################################################

Project Name:

dev-academy

Project Type:

Static educational website hosted on GitHub Pages.

Main Goal:

Build a high-quality learning platform for:

- Programming
- Computer Science
- Data Structures
- Algorithms
- Software Engineering
- Git
- AI Agent Engineering

The primary goal is:

Teaching quality first.

HTML generation is secondary.

A course is successful only when a beginner can learn the topic successfully.

########################################################
# TECHNOLOGY STACK
########################################################

Use only:

- HTML
- CSS
- JavaScript
- Bootstrap
- GitHub Pages
- LocalStorage (optional)

Do not use:

- Backend server
- Database
- Authentication
- React
- Vue
- Angular
- Firebase
- Supabase
- Node.js build tools
- Online compiler
- AI grading

unless explicitly requested.

########################################################
# CORE AGENT BEHAVIOR
########################################################

Whenever a user asks:

"Tạo khóa học"

or

"Refactor khóa học"

or

"Mở rộng khóa học"

the AI must first read:

- AGENTS.md
- CLAUDE.md
- .spec
- .rules
- .workflows

These files are mandatory.

########################################################
# EDUCATION FIRST RULE
########################################################

The objective is NOT:

- Creating HTML files
- Creating folders
- Creating pages

The objective IS:

Teaching learners effectively.

When there is a conflict between:

- Better content
and
- Faster page generation

always choose better content.

########################################################
# COURSE GENERATION RULE
########################################################

When generating a course:

The AI must:

1. Create course structure
2. Create lesson structure
3. Generate educational content
4. Generate examples
5. Generate exercises
6. Generate quizzes
7. Generate essay questions
8. Generate suggested answers
9. Update navigation
10. Update homepage

Never stop after generating folder structures.

########################################################
# BEGINNER-FIRST RULE
########################################################

Assume the learner knows nothing.

Every lesson must be understandable by:

- First-year university students
- Self-taught beginners
- Learners with no prior experience

Never assume background knowledge.

Always explain:

- What
- Why
- How
- When

########################################################
# THEORY QUALITY RULE
########################################################

Every important concept must contain:

1. Definition
2. Why it exists
3. Why it is important
4. Real-world usage
5. Syntax (if applicable)
6. How it works
7. Common mistakes
8. Summary

Avoid:

- Generic explanations
- One-paragraph lessons
- Syntax-only explanations

Bad:

Variable stores data.

Good:

Explain:

- memory
- storage
- naming
- usage
- examples

########################################################
# PROGRAMMING COURSE RULE
########################################################

For programming courses:

Examples:

- C++
- Python
- Java
- Data Structures
- Algorithms

Every lesson must contain:

Example 1:
Basic example

Example 2:
Practical example

Every example must:

- Compile
- Be runnable
- Include required libraries
- Include main()
- Include Vietnamese comments

########################################################
# CODE COMMENT RULE
########################################################

Code examples must teach.

Every logical block must contain comments.

Example:

// Khai báo biến lưu tuổi
int age = 20;

// Hiển thị tuổi ra màn hình
cout << age;

Never generate unexplained code.

########################################################
# CODE EXPLANATION RULE
########################################################

After every code example create:

Giải thích chương trình

Explain:

- Purpose
- Input
- Output
- Variables
- Flow
- Expected result

Do not stop at code.

########################################################
# PRACTICE RULE
########################################################

Every lesson must contain:

Easy:
- 3 exercises

Medium:
- 2 exercises

Hard:
- Optional

Programming exercises should require coding.

########################################################
# QUIZ RULE
########################################################

Every lesson must contain:

Minimum:
5 questions

Question types:

- Concept
- Syntax
- Output prediction
- Error detection
- Practical usage

########################################################
# ESSAY RULE
########################################################

Every lesson must contain:

Minimum:
2 essay questions

Generate:

- Suggested answers

Do not grade essays.

########################################################
# GIT COURSE RULE
########################################################

Git lessons must include:

- Commands
- Explanation
- Expected output
- Common mistakes
- Real workflows

Example:

git status

Explain:

- What it does
- When to use it
- Expected result
- Common errors

Git courses must teach real development workflows.

########################################################
# AGENT ENGINEERING COURSE RULE
########################################################

Agent Engineering courses must include:

- Prompt Engineering
- Context Engineering
- AGENTS.md
- CLAUDE.md
- Rules
- Specs
- Workflows
- Tool Calling
- MCP
- Multi-Agent Systems

Use practical examples whenever possible.

########################################################
# HOMEPAGE UPDATE RULE
########################################################

When creating a course:

Update:

index.html

If available:

courses.html

Insert course cards between:

AGENT_COURSE_CARDS_START
AGENT_COURSE_CARDS_END

when those markers exist.

########################################################
# SIDEBAR RULE
########################################################

Every lesson page must contain:

- Course overview
- Lesson list
- Active lesson indication if possible

Desktop:

Sidebar on left

Mobile:

Sidebar on top or collapsible

########################################################
# RESPONSIVE RULE
########################################################

All pages must work on:

- Mobile
- Tablet
- Laptop
- Desktop

Avoid:

- Horizontal scrolling
- Tiny buttons
- Overflowing code blocks

########################################################
# REFACTOR COURSE RULE
########################################################

When improving an existing course:

Preserve:

- URLs
- Folder structure
- Navigation
- Existing quizzes
- Existing essay sections

Improve:

- Theory
- Examples
- Exercises
- Comments
- Explanations

Never reduce quality.

########################################################
# QUALITY ACCEPTANCE RULE
########################################################

A lesson is incomplete if:

✗ Theory is shallow

✗ Examples are missing

✗ Examples lack comments

✗ Code explanations are missing

✗ Exercises are missing

✗ Quiz is missing

✗ Essay questions are missing

✗ Suggested answers are missing

✗ Navigation is missing

Only lessons that satisfy all requirements are considered complete.

########################################################
# FINAL REPORT RULE
########################################################

After every task report:

Created:
- ...

Modified:
- ...

Improved:
- ...

Notes:
- ...
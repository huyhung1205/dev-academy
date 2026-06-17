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

## Standard Course Requirements

Every course must include:

- Course overview page
- Lesson pages
- Sidebar or table of contents
- Responsive layout
- Homepage course card
- Internal navigation links

## Standard Course Folder Structure

courses/<course-slug>/
├── index.html
└── lessons/
    ├── lesson-01.html
    ├── lesson-02.html
    ├── lesson-03.html
    ├── lesson-04.html
    └── lesson-05.html

## Course Overview Page Specification

Each course overview page must include:

1. Course title
2. Course description
3. Target learners
4. Learning objectives
5. Lesson list
6. Start learning button
7. Back to homepage link
8. Back to courses page link if available

## Lesson Page Specification

Each lesson page must contain:

1. Introduction
2. Learning Objectives
3. Video Section
4. Theory Section
5. Syntax Section (if applicable)
6. How It Works
7. Common Mistakes
8. Example 1
9. Example 2
10. Practice Exercises
11. Quiz
12. Essay Questions
13. Suggested Answers
14. Summary
15. Previous / Next Navigation
16. Footer

------------------------------------------------

## THEORY SPECIFICATION

Theory quality is the highest priority.

Theory must be written for absolute beginners.

The AI must assume the learner has never studied the topic before.

Every important concept must contain:

1. Definition
2. Why it is needed
3. Real-world usage
4. Syntax (if applicable)
5. Step-by-step explanation
6. Visual explanation if useful
7. Common mistakes
8. Summary

Theory must NOT be:

- Generic
- Too short
- Only bullet points
- Only syntax descriptions

Bad:

Variable is used to store data.

Good:

Explain:

- what a variable is
- why memory is needed
- how variables are stored
- how variables are used
- practical examples

Minimum recommended length:

500+ words per lesson

Complex topics may require:

1000+ words

Examples:

- Pointers
- Arrays
- Strings
- Structs
- Files
- Trees
- Graphs
- Algorithms

------------------------------------------------

## PROGRAMMING EXAMPLE SPECIFICATION

Every programming lesson must contain:

Minimum:

- 2 complete runnable programs

Example 1:

- Basic example

Example 2:

- Practical example

Every example must include:

- Complete code
- Required libraries
- main()
- Input/output when applicable
- Vietnamese comments

Forbidden:

int add(int a, int b)
{
    return a + b;
}

unless accompanied by a complete runnable program.

------------------------------------------------

## CODE COMMENT SPECIFICATION

Every code example must contain comments.

Minimum:

- 1 comment per logical block

Example:

// Khai báo biến lưu tuổi
int age = 20;

// Hiển thị tuổi ra màn hình
cout << age;

The learner must be able to understand the code without reading external material.

------------------------------------------------

## CODE EXPLANATION SPECIFICATION

After every code example create a section:

Giải thích chương trình

Must explain:

1. Program purpose
2. Input
3. Output
4. Variables
5. Execution flow
6. Important lines
7. Expected result

Do not stop at showing code.

------------------------------------------------

## PRACTICE EXERCISE SPECIFICATION

Every lesson must include:

Easy:

- 3 exercises

Medium:

- 2 exercises

Hard:

- Optional

Programming exercises should require writing code.

Avoid exercises that only ask for definitions.

------------------------------------------------

## QUIZ SPECIFICATION

Every lesson must include:

Minimum:

5 questions

Question types should include:

- Concept
- Syntax
- Output prediction
- Error detection
- Practical usage

Avoid generating only definition questions.

Quiz must:

- Run in browser
- Use JavaScript
- Show score immediately
- Work without backend

------------------------------------------------

## ESSAY SPECIFICATION

Every lesson must include:

Minimum:

2 essay questions

Essay questions should encourage:

- Explanation
- Comparison
- Reasoning
- Reflection

Avoid yes/no questions.

Good:

Compare pass-by-value and pass-by-reference.

Bad:

Is pass-by-reference useful?

------------------------------------------------

## VIDEO SPECIFICATION

Video section must appear near the beginning of the lesson.

If no video is provided:

Display:

Video mô phỏng sẽ được cập nhật sau.

Support:

- YouTube embed
- Local video

------------------------------------------------

## PROGRAMMING COURSE SPECIFICATION

For programming courses:

Examples must be practical.

Theory must explain:

- What
- Why
- How
- When

Important topics must be explained in extra detail:

- Functions
- Pointers
- Arrays
- Strings
- Structs
- Files
- Recursion
- Data Structures
- Algorithms

These topics are foundations for later courses.

------------------------------------------------

## GIT COURSE SPECIFICATION

Every Git lesson must contain:

- Commands
- Explanations
- Expected output
- Common mistakes
- Real workflows

Example:

git status
git add .
git commit -m "Initial commit"

After each command block explain:

- What it does
- When to use it
- Expected result
- Common errors

------------------------------------------------

## HOMEPAGE INTEGRATION SPECIFICATION

When a new course is created:

The AI must update:

index.html

The homepage must display the new course as:

- Course card
- Sidebar item
- Menu item
- Course list item

Preferred card:

- Course title
- Short description
- Start button
- Link to course overview page

------------------------------------------------

## RESPONSIVE SPECIFICATION

The layout must work on:

- Mobile
- Tablet
- Laptop
- Desktop

Recommended lesson layout:

Sidebar:
- Left on desktop
- Top on mobile

Content:
- Main lesson area

Avoid horizontal scrolling.

------------------------------------------------

## QUALITY ACCEPTANCE CRITERIA

A lesson is considered complete only if:

✓ Theory is detailed

✓ Beginner-friendly explanation exists

✓ Minimum 2 runnable examples exist

✓ Code comments exist

✓ Code explanation exists

✓ Practice exercises exist

✓ Quiz exists

✓ Essay questions exist

✓ Suggested answers exist

✓ Navigation exists

A lesson failing any of the above requirements is incomplete.

------------------------------------------------

## Out Of Scope

Do not implement unless explicitly requested:

- User accounts
- Login/Register
- Database
- Backend server
- Online judge
- Automatic code grading
- AI essay grading
- Payment
- Admin dashboard
- Complex frontend frameworks
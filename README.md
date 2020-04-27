# UofTHacks2020 - STEMNotes
**The** note taking tool for scientists and engineers.

*Uzair Ahmed, Arjun Dureja, Farhan Mohammed, Martin Chak*

**[https://devpost.com/software/stem-notes-c5i7ho](https://devpost.com/software/stem-notes-c5i7ho)**

![logo](https://raw.githubusercontent.com/uzairmahmed/UofTHacks2020/master/images/splash.png)

## Inspiration

As we were discussing ideas, our group began ranting about the inconsistency of our professors' notes. The team only of STEM students, and we found that one consistent complaint was the difficulty of reading written code. This idea of cleaning hand-written notes motivated us to search for even better solutions for professors and students to develop more uniform notes and encourage learning. Also, one of us is a computer science student at U of T, he says that many of the proof-related courses require latex-only submissions and that being able create LaTeX documents hand written is a god-send

## What it does

At first the application looks like a simple note-taking app. But what differentiates it from a normal app is that it allows the user to create handwritten notes, while simultaneously transcribing them into digital notes.

## How we built it

The application is split into three main components.

The first is the mobile note-taking application. As the user writes their notes, they have segments of their notes categorized for processing. Due to the time constraints, the app is only supported on IOS, however the overall architecture allows for any mobile platform to be used as a source. 

The second major component is our data server set up on Google Cloud Platform. The platform is responsible for processing the notes. The server also manages the transfer of data between each component of the system.

The final component is our web application that takes the processed data and then generates a uniform document for live presentation. The nature of the application grants ease of access for users and their peers to view and download the notes.

Overall the components work together and create a service for students and professors alike.

## Challenges we ran into

The biggest challenge was connecting the components together with the Google Cloud Services. We used a large variety of tools to create the project, each one had different requirements that each team member had to individually solve.

The IOS application we created relied on a very new library, as a consequence there was less an ideal amount of support for the library. Specifically that the features were not very modular, meaning there was little room to add the features we deemed ideal for the project.

## Accomplishments that we're proud of

The skillsets of our team member were very diverse, we wanted to pick a project that could emphasize each one of our skills. In the end, we created an application that allowed us to strengthen our proficiency of our preferred tools, while motivating us to step out of our comfort zone.

## What we learned

Number one is that we can get a lot done with two hours of sleep.

Individually each member learned a lot about their side of the project and through our diverse skill sets, we were able to learn a whole lot about other fields.

## What's next for STEM Notes

The first step would be to enhance what we currently have, we want to improve simple things such as UI/UX and support for other platforms. After that, there is an entire rabbit hole of math and STEM based tools or utilities that could vastly improve the versatility of such an app. For example, Wolfram Alpha's API could be incorporated with LaTeX to solve written equations in real-time. We could also implement code completion technologies similar to Intellisense.

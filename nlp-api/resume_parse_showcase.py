from resumeParse import *
from nlp import *

resumepath = 'nlp-api/resume2.pdf'

# parse resume, and output the skills 
skills = generate_skills(resumepath, 'pdf')
print(skills)

# show the similarity in the desc and users skills
desc = """
Ticket Title: Enhance User Profile Management Module

Description:

Objective:
Improve the existing User Profile Management module to provide a more intuitive and personalized experience for our users.

Details:

Technical Enhancements:

User Profile Page:

Implement dynamic rendering of user profiles with HTML, CSS, and JavaScript to enhance the visual presentation.
Integrate responsive design principles for a seamless user experience across devices.
Utilize AJAX for asynchronous data loading to improve page load times.
Skills Display:

Enhance the skills section to dynamically showcase a user's proficiency in coding languages such as Python, JavaScript, and Java.
Implement a tag-based system for easy categorization and display of technical skills.
Integration with External APIs:

Explore and integrate relevant external APIs (e.g., GitHub API) to automatically fetch and display a user's latest coding projects and contributions.
Ensure secure handling of API keys and data privacy.
Soft Skills Integration:

Communication:

Implement a user-friendly interface to allow users to input and showcase their soft skills such as communication, teamwork, and leadership.
Provide a rating system or descriptive input for users to self-assess their soft skills.
User Feedback Mechanism:

Introduce a user feedback mechanism to collect testimonials or endorsements from colleagues, mentors, or project collaborators.
Display aggregated feedback on the user profile in a visually appealing format.
Acceptance Criteria:

User profiles are visually enhanced with HTML, CSS, and JavaScript.
Coding languages and technical skills are dynamically displayed and categorized.
External APIs fetch and display relevant coding projects on the user profile.
Soft skills are incorporated into the user profile, allowing self-assessment and display.
User feedback mechanism is implemented and testimonials are displayed on the user profile.
Code is well-documented, modular, and adheres to coding standards.
Notes:

Collaborate with the UX/UI team for design considerations.
Ensure compatibility with various browsers and devices.
Conduct thorough testing to validate the functionality and performance improvements.
"""

similairity = cosine_sim(resumepath, desc)
print(similairity)
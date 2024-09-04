from django.shortcuts import render

# Create your views here.

CourseList = [
    {
        'course_poster':'https://t4.ftcdn.net/jpg/02/14/56/75/360_F_214567514_hGbTMUq06pJIGKiXA248l43E3hU9Q08x.jpg',
        'course_name': 'Python Programming',
        'instructor': 'John Doe',
        'course_description': 'Learn Python programming from scratch.',
        'duration': '6 months',
        'price': '$1000',
    },
    {
        'course_poster':'https://t4.ftcdn.net/jpg/02/14/56/75/360_F_214567514_hGbTMUq06pJIGKiXA248l43E3hU9Q08x.jpg',
        'course_name': 'Web Development with JavaScript',
        'instructor': 'Jane Smith',
        'course_description': 'Master web development using JavaScript, HTML, and CSS.',
        'duration': '5 months',
        'price': '$900',
    },
    {
        'course_poster':'https://t4.ftcdn.net/jpg/02/14/56/75/360_F_214567514_hGbTMUq06pJIGKiXA248l43E3hU9Q08x.jpg',
        'course_name': 'Data Science with R',
        'instructor': 'Alice Johnson',
        'course_description': 'Explore data science concepts using the R programming language.',
        'duration': '7 months',
        'price': '$1100',
    },
    {
        'course_poster':'https://t4.ftcdn.net/jpg/02/14/56/75/360_F_214567514_hGbTMUq06pJIGKiXA248l43E3hU9Q08x.jpg',
        'course_name': 'Machine Learning A-Z',
        'instructor': 'Michael Brown',
        'course_description': 'Learn machine learning from basics to advanced topics.',
        'duration': '8 months',
        'price': '$1200',
    },
    {
        'course_poster':'https://t4.ftcdn.net/jpg/02/14/56/75/360_F_214567514_hGbTMUq06pJIGKiXA248l43E3hU9Q08x.jpg',
        'course_name': 'Full Stack Web Development',
        'instructor': 'Chris Green',
        'course_description': 'Become a full stack web developer with hands-on projects.',
        'duration': '9 months',
        'price': '$1500',
    },
    {
        'course_poster':'https://t4.ftcdn.net/jpg/02/14/56/75/360_F_214567514_hGbTMUq06pJIGKiXA248l43E3hU9Q08x.jpg',
        'course_name': 'DevOps Essentials',
        'instructor': 'Nancy White',
        'course_description': 'Learn the essentials of DevOps and automate your workflow.',
        'duration': '4 months',
        'price': '$800',
    },
    {
        'course_poster':'https://t4.ftcdn.net/jpg/02/14/56/75/360_F_214567514_hGbTMUq06pJIGKiXA248l43E3hU9Q08x.jpg',
        'course_name': 'Cloud Computing with AWS',
        'instructor': 'David Black',
        'course_description': 'Get started with cloud computing using Amazon Web Services.',
        'duration': '6 months',
        'price': '$1000',
    },
    {
        'course_poster':'https://t4.ftcdn.net/jpg/02/14/56/75/360_F_214567514_hGbTMUq06pJIGKiXA248l43E3hU9Q08x.jpg',
        'course_name': 'Cyber Security Fundamentals',
        'instructor': 'Rachel Blue',
        'course_description': 'Understand the basics of cybersecurity and how to protect systems.',
        'duration': '6 months',
        'price': '$1000',
    },
]



def Courses(request):
    return render(request, 'Course.html',{"CourseList":CourseList})
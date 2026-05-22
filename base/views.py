from django.shortcuts import render

# Create your views here.


home_page = [

    {
        'id': 1,
        'title': 'India’s Technology Sector Continues Rapid Growth in 2026',
        'desc': 'India’s technology industry is experiencing remarkable growth in 2026 with major cities such as Bengaluru, Hyderabad, Chennai, and Pune becoming important technology hubs. Large multinational companies and startups are increasing their investments in artificial intelligence, cloud computing, cybersecurity, and data analytics. Thousands of fresh graduates are being recruited for software development and digital transformation projects. Government initiatives supporting digital India programs are also encouraging innovation among young entrepreneurs. Experts believe India is becoming one of the world’s leading destinations for technology services and IT exports. Several new startup incubators and innovation centers are being launched across universities and private institutions. Companies are also providing remote work opportunities, helping employees work flexibly from different locations. The increasing demand for skilled professionals has encouraged many students to join technical and programming courses. Industry analysts predict that India’s technology market will continue expanding rapidly over the next decade. The sector is expected to create millions of new employment opportunities for young professionals.',
        'image': '/static/images/trade.jpg'
    },

    {
        'id': 2,
        'title': 'Tourism Industry Sees Huge Rise During Summer Vacation',
        'desc': 'India’s tourism sector is witnessing a major increase in travelers during the summer vacation season as families and students plan trips to famous destinations. Tourist locations such as Ooty, Goa, Kashmir, Munnar, Shimla, and Manali are receiving large numbers of visitors every day. Hotels, resorts, restaurants, and local transport services are benefiting from the growing tourism activity. Travel agencies have reported a sharp increase in online bookings compared to previous years. Many state governments are also promoting tourism through cultural festivals and tourism campaigns. Adventure tourism activities such as trekking, river rafting, and camping are attracting young travelers from different parts of the country. International tourists are also showing interest in India’s historical monuments, beaches, and wildlife sanctuaries. Tourism experts believe the industry is contributing significantly to local businesses and employment generation. Improved transportation systems and online travel services have made vacation planning easier for travelers. Analysts expect the tourism industry to continue growing strongly in the coming years.',
        'image': '/static/images/trade2.jpg'
    },

    {
        'id': 3,
        'title': 'Electric Vehicles Becoming More Popular Among Young Buyers',
        'desc': 'Electric vehicles are rapidly becoming popular across India as consumers shift toward environmentally friendly transportation options. Major automobile companies are launching affordable electric cars, scooters, and bikes with improved battery technology and faster charging systems. Rising fuel prices and environmental awareness are encouraging people to choose electric mobility solutions. Government subsidies and tax benefits are also supporting the growth of the electric vehicle market. Charging stations are being installed in major cities, highways, shopping malls, and office areas to improve convenience for users. Young professionals and students are increasingly purchasing electric scooters for daily travel because of their lower maintenance costs. Automobile manufacturers are investing heavily in research and development to improve battery performance and driving range. Experts believe electric vehicles will play a major role in reducing air pollution in urban areas. Several startups are also entering the electric mobility sector with innovative transportation solutions. Industry analysts predict that electric vehicles will dominate the future transportation market in India.',
        'image': '/static/images/trade3.jpg'
    },

    {
        'id': 4,
        'title': 'Online Learning Platforms Expanding Across India',
        'desc': 'Online education platforms are becoming increasingly popular among students and working professionals who want to improve their technical and professional skills. Courses related to software development, artificial intelligence, digital marketing, cloud computing, and data analytics are receiving huge enrollments. Students from both urban and rural areas are benefiting from affordable online learning opportunities. Educational companies are introducing interactive video classes, live mentorship sessions, and certification programs for learners. Many universities and colleges are also collaborating with online learning platforms to provide industry-focused education. Working professionals are joining part-time online courses to improve their career opportunities and technical knowledge. Experts believe digital education is helping bridge the gap between academic learning and industry requirements. Online learning platforms are also supporting multiple languages to reach a wider audience across the country. Mobile applications and internet accessibility have made online learning more convenient for students. Analysts expect the online education industry to grow significantly over the next few years.',
        'image': '/static/images/trade4.jpg'
    },

    {
        'id': 5,
        'title': 'India’s Fitness Industry Growing at a Rapid Pace',
        'desc': 'India’s fitness and wellness industry is growing rapidly as people become more aware of healthy lifestyles and physical well-being. Fitness centers, yoga studios, sports clubs, and wellness programs are expanding across metropolitan cities and smaller towns. Young professionals are actively participating in gym memberships, fitness challenges, and outdoor activities to maintain their health. Social media influencers and fitness trainers are also encouraging healthy living habits among the public. Many companies are introducing wellness programs for employees to improve workplace productivity and mental health. The demand for healthy food products, protein supplements, and fitness equipment has also increased significantly. Experts believe the fitness industry is creating new business opportunities and employment in healthcare and wellness sectors. Online fitness applications and virtual workout sessions have become highly popular among users. Doctors and health experts are advising people to follow regular exercise routines to prevent lifestyle diseases. Industry reports suggest the fitness market in India will continue growing strongly in the coming years.',
        'image': '/static/images/trade5.jpg'
    }

]


event_page = [

    {
        'id': 1,
        'title': 'Chennai Food Festival 2026 Attracts Thousands of Visitors',
        'desc': 'The Chennai Food Festival 2026 became one of the biggest cultural events of the year as food lovers from across the country gathered to experience traditional and modern cuisines. The festival featured hundreds of food stalls offering South Indian dishes, street foods, desserts, and international recipes. Celebrity chefs conducted live cooking sessions and shared unique recipes with visitors during the event. Music performances, dance shows, and cultural programs entertained the audience throughout the evening. Local restaurant owners and small food businesses received huge support from visitors attending the festival. Families, tourists, and students actively participated in food competitions and tasting events organized by the management team. The event also promoted Tamil Nadu’s traditional cuisine and local culinary heritage to international tourists. Organizers stated that visitor participation was much higher compared to previous years. Security teams and volunteers ensured smooth crowd management and visitor safety during the festival. The successful event highlighted Chennai’s growing reputation as an important destination for food and cultural tourism.',
        'image': '/static/images/event1.jpg'
    },

    {
        'id': 2,
        'title': 'National Startup Summit Held in Bengaluru',
        'desc': 'Entrepreneurs, investors, and technology experts participated in the National Startup Summit organized in Bengaluru this week. The event focused on innovation in artificial intelligence, fintech, healthcare technology, and sustainable business solutions. Startup founders presented their ideas and business models to investors and industry leaders during live pitching sessions. Several workshops were conducted to help young entrepreneurs understand funding opportunities and market strategies. Industry experts discussed the future of India’s startup ecosystem and the importance of digital transformation in businesses. Students and fresh graduates attended the summit to learn about entrepreneurship and emerging technology trends. Government representatives also announced support programs and funding initiatives for startup companies. Networking sessions allowed business owners and investors to connect and discuss future collaborations. Organizers said the summit successfully encouraged innovation and startup culture among young professionals. The event highlighted Bengaluru’s position as one of India’s leading startup and technology cities.',
        'image': '/static/images/event2.jpg'
    },

    {
        'id': 3,
        'title': 'International Music Concert Creates Excitement in Mumbai',
        'desc': 'Thousands of music fans attended the international music concert held at Mumbai’s largest sports stadium this weekend. Famous singers, DJs, and music bands delivered energetic live performances that kept the audience entertained throughout the night. Advanced lighting systems, stage effects, and fireworks created an exciting atmosphere for visitors attending the concert. Fans from different states traveled to Mumbai to experience the large-scale entertainment event. Organizers arranged food stalls, security teams, medical support, and transportation facilities to manage the crowd effectively. Social media platforms were filled with videos and photos from the concert as fans shared their experiences online. Celebrity guests and influencers also attended the event, attracting additional public attention. Music lovers praised the event management team for maintaining smooth operations and visitor safety. Event organizers stated that ticket sales exceeded expectations due to high public demand. The concert became one of the most talked-about entertainment events of the year in India.',
        'image': '/static/images/event3.jpg'
    },

    {
        'id': 4,
        'title': 'Book Fair 2026 Encourages Young Readers',
        'desc': 'The annual national book fair organized in Delhi attracted thousands of students, teachers, authors, and book lovers from different states. Publishers displayed books covering fiction, science, technology, business, history, and competitive examination topics. Visitors explored newly released novels and educational materials from both Indian and international publishers. Famous authors conducted live interaction sessions and discussed their writing experiences with readers during the event. Schools and colleges arranged educational visits for students to encourage reading habits among young learners. Organizers also conducted workshops related to creative writing, public speaking, and digital publishing. Many visitors purchased books at discounted prices offered during the exhibition. Educational institutions praised the event for promoting literacy and knowledge-sharing among students. Volunteers and event coordinators ensured smooth crowd management and visitor assistance throughout the fair. The successful event highlighted the growing interest in books and learning among India’s younger generation.',
        'image': '/static/images/event4.jpg'
    },

    {
        'id': 5,
        'title': 'Sports Marathon Conducted for Health Awareness',
        'desc': 'A large-scale city marathon was conducted to promote fitness, healthy living, and public awareness about physical wellness. Participants from different age groups including students, professionals, athletes, and senior citizens joined the marathon event. Medical teams, fitness trainers, and volunteers were present throughout the route to ensure participant safety and provide assistance when required. The marathon included multiple categories such as 5-kilometer, 10-kilometer, and half-marathon races for different participants. Sponsors and local organizations supported the event by providing refreshments, health checkups, and fitness guidance. Several schools and colleges encouraged students to participate and understand the importance of regular exercise. Public health experts addressed the audience about maintaining healthy lifestyles and reducing stress through physical activity. The event also promoted environmental awareness by encouraging eco-friendly practices during the marathon. Organizers appreciated the public response and active participation from people across the city. The successful event encouraged citizens to adopt healthier habits and active daily routines.',
        'image': '/static/images/event5.jpg'
    }

]




news_page = [

 {
    'id': 1,

    'title': 'Thalapathy Vijay Begins New Political Journey in Tamil Nadu',

    'desc': 'Actor Vijay, popularly known as Thalapathy Vijay, has officially strengthened his political journey in Tamil Nadu with the launch of new public welfare initiatives and political campaigns across the state. Thousands of supporters gathered during recent public meetings where Vijay spoke about education, employment opportunities, youth development, and social welfare programs. His speeches focused on creating better opportunities for students and improving the living standards of common people in both urban and rural areas. Political analysts believe Vijay’s growing popularity among young voters could create a major impact in future Tamil Nadu elections. Fans and supporters have actively participated in rallies, social service activities, and awareness programs organized by his political team. Vijay also emphasized transparency, equality, and development as important goals for the future of the state. Social media platforms have been filled with discussions and trending hashtags related to his political movement. Several youth groups and public organizations have shown support for his vision and leadership style. Experts believe his strong fan base and public influence may play an important role in shaping Tamil Nadu politics in the coming years. Public meetings and campaign activities are expected to continue across multiple districts in the state.',

    'image':'/static/images/vijay.jpg '
},

    {
        'id': 2,
        'title': 'Indian Space Research Achieves Another Major Milestone',
        'desc': 'Indian scientists successfully completed another important satellite mission aimed at improving communication and weather monitoring systems. The satellite launch was conducted from the Satish Dhawan Space Centre using advanced launch vehicle technology developed by Indian engineers. Scientists stated that the mission will support communication services, disaster monitoring, and scientific research activities. The successful launch was appreciated by researchers, government officials, and international space organizations. Experts believe the achievement strengthens India’s growing reputation in global space exploration and innovation. Engineers and scientists worked for several years to develop and test the satellite systems before launch. Students and educational institutions across the country celebrated the mission as an inspiration for future scientific development. Space research organizations are also planning additional missions related to lunar exploration and advanced satellite technologies. The mission demonstrated India’s capability in designing cost-effective and reliable space programs. Analysts believe the success will encourage further investments in science, research, and technological innovation.',
        'image': '/static/images/news2.jpg'
    },

    {
        'id': 3,
        'title': 'New Education Policies Focus on Digital Learning',
        'desc': 'Educational institutions across India are increasingly adopting digital learning methods as part of the latest education reforms introduced this year. Schools and colleges are introducing smart classrooms, online assessments, and skill-based training programs for students. Teachers are receiving technical training to improve classroom teaching through modern digital tools and interactive learning methods. Educational experts believe digital learning can improve accessibility and provide better learning opportunities for students in rural regions. Online educational platforms are also collaborating with institutions to offer industry-focused certification programs. Students are using mobile applications and e-learning resources to strengthen technical and communication skills. Government authorities are investing in internet infrastructure and digital education systems across public institutions. Universities are introducing new courses related to artificial intelligence, cybersecurity, cloud computing, and data science. Parents and educators believe technology-based education can improve student engagement and career readiness. Analysts predict digital education will continue transforming India’s academic environment over the coming years.',
        'image': '/static/images/news3.jpg'
    },

    {
        'id': 4,
        'title': 'Railway Department Announces New High-Speed Routes',
        'desc': 'The Indian Railway Department has announced plans to introduce additional high-speed train routes connecting major metropolitan cities across the country. Officials stated that the project aims to reduce travel time and improve transportation facilities for passengers. Modern railway stations with advanced safety systems and digital ticketing services are also being developed as part of the expansion plan. Engineers are conducting surveys and infrastructure assessments before starting construction work on new routes. Government representatives believe the project will strengthen economic growth and improve connectivity between important business cities. Passengers are expected to benefit from improved comfort, faster travel, and better railway services. Environmental experts also stated that railway transportation can help reduce road traffic congestion and fuel consumption. The railway department plans to introduce modern trains with improved technology and passenger facilities. Several employment opportunities are expected to be created during the construction and operational phases of the project. Officials confirmed that the development work will begin in multiple phases over the next few years.',
        'image': '/static/images/news4.jpg'
    },

    {
        'id': 5,
        'title': 'Healthcare Sector Expands Services in Rural Areas',
        'desc': 'Healthcare organizations and government authorities are expanding medical services in rural areas through new hospitals, mobile clinics, and telemedicine support systems. The initiative aims to improve access to healthcare facilities for people living in remote villages and underserved communities. Doctors and healthcare workers are conducting awareness programs related to nutrition, hygiene, and disease prevention. Mobile medical units are visiting rural locations regularly to provide free checkups and essential medicines. Government officials stated that additional funding is being allocated to improve healthcare infrastructure and emergency medical services. Technology-based healthcare systems are also helping patients consult doctors online through telemedicine platforms. Health experts believe the expansion will reduce medical challenges faced by rural populations. Training programs are being organized for healthcare workers to improve medical service quality in village regions. Several nonprofit organizations are supporting the initiative through health camps and awareness activities. Authorities expect the project to improve public health conditions and strengthen healthcare accessibility across rural India.',
        'image': '/static/images/news5.jpg'
    }

]



about_page = [

    {
        'id': 1,

        'title': 'About Us',

        'desc': 'Welcome to our article platform where readers can explore the latest news, events, technology updates, and informative articles from different categories. Our website is designed to provide a clean and user-friendly reading experience for users who are interested in trending topics, educational content, business insights, and real-world updates. We aim to deliver useful and engaging articles that help readers stay informed and connected with current trends happening around the world.'
        
    },


    {
        'id': 2,

        'title': 'About The Author',
        

        'desc': 'Hello, I’m Nithish Rexson, a passionate MCA graduate and aspiring Python Developer with strong interest in Django web development, data analytics, and real-world software projects. I created this article platform as part of my learning journey to build a modern and user-friendly news and event website using Python and Django. I enjoy developing creative web applications, exploring new technologies, and improving my programming skills through practical projects. My goal is to become a skilled software developer and contribute to innovative technology solutions in the future.'
    },

    {
        'id': 3,

        'title': 'Our Mission',

        'desc': 'Our mission is to make information accessible, simple, and useful for everyone through high-quality articles and modern web technologies. We believe digital platforms should not only provide information but also create engaging experiences for readers. This website focuses on delivering updated and informative content while improving the overall reading experience through attractive design and easy navigation. We continuously work on improving our platform and adding more useful content for users.'
    },

    {
        'id': 4,

        'title': 'What We Provide',

        'desc': 'Our platform provides readers with access to news articles, event updates, technology insights, educational content, and trending information from multiple categories. We focus on presenting information in a simple and understandable format so that readers can easily explore different topics. The website is built with modern web technologies to ensure smooth performance, attractive design, and easy navigation for users across all devices.'
    },

    {
        'id': 5,

        'title': 'Why Choose Our Platform',

        'desc': 'We focus on delivering quality content with a clean and modern user interface that improves the overall reading experience. Our goal is to provide updated information, attractive article layouts, and organized categories that help users quickly find the content they are interested in. We continuously work on improving our platform by adding better features, improving design quality, and enhancing user interaction through real-world web development practices.'
    }

]










context2 = {'event':event_page}

context3 = {'news':news_page}

context4 = {'abouts':about_page}


def home(request):
    
    return render(request,'home.html',{'front':home_page})

def event(request):
    return render(request,'event.html',context2)

def news(request):
    return render(request,'news.html',context3)

def about(request):
    return render(request,'about.html',context4)

def read(request,pk):
    for i in home_page:
        if i['id'] == pk:
            context = {'home':i}
    return render(request,'read.html',context)

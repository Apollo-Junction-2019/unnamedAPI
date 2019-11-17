from chatterbot import *
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_first_response
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# -*- coding: utf-8 -*-

chatbot = ChatBot("Apollo",
                  preprocessors=[
                      'chatterbot.preprocessors.clean_whitespace',
                  ],
                  logic_adapters=[
                      {
                          "import_path": "chatterbot.logic.BestMatch",
                          'default_response': 'I am sorry, but I do not understand.',
                          'maximum_similarity_threshold': 0.55,
                          "statement_comparison_function": LevenshteinDistance,
                          "response_selection_method": get_first_response
                      }
                  ],
                  read_only=False)
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)
trainer = ListTrainer(chatbot)

trainer.train([
    'Hi',
    'Hello to you too ',
    'How are you?',
    'I am good, how are you?',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

x = 0
while x < 10:
    trainer.train([
    'Analog',
    'An analog method of storing data is one that uses a constantly changing physical quantity, such as the voltage of an electrical current or the amplitude of a sound wave, to represent the data. A common example of this is the constantly changing position of the hands on an analog clock. Read more: http://www.math.utah.edu/%7Ewisnia/glossary.html',
    'What is Analog',
    'An analog method of storing data is one that uses a constantly changing physical quantity, such as the voltage of an electrical current or the amplitude of a sound wave, to represent the data. A common example of this is the constantly changing position of the hands on an analog clock. Read more: http://www.math.utah.edu/%7Ewisnia/glossary.html',
    ])
    trainer.train([
    'Backup',
    'A backup is a copy of a file or resource that can be accessed if the original gets lost or destroyed. Read more: https://ist.mit.edu/security/backup ',
    'What is a Backup',
    'A backup is a copy of a file or resource that can be accessed if the original gets lost or destroyed. Read more: https://ist.mit.edu/security/backup ',

    ])
    trainer.train([
    'Bandwidth',
    'Bandwidth is a measure of how much data you can move through an Internet connection in a given amount of time. It is usually measured in bits-per-second. Read more: Read more: http://www.nova.edu/library/help/misc/glossary.html#b ',
    'What is Bandwidth',
    'Bandwidth is a measure of how much data you can move through an Internet connection in a given amount of time. It is usually measured in bits-per-second. Read more: Read more: http://www.nova.edu/library/help/misc/glossary.html#b ',
    ])
    trainer.train([
    'Browser',
    'A browser is a computer software program that allows the user to surf the Internet. A browser interprets HTML code and displays websites and graphics on the computer screen.Read more: http://www.lib.berkeley.edu/TeachingLib/Guides/Internet/Glossary.html ',
    ])
    trainer.train([
    'Computer',
    'A computer is a machine that can store information and follow instructions to help people accomplish various tasks.',
    'Read more: http://encyclopedia.kids.net.au/page/cp/CPURead more: http://www.bbc.co.uk/guides/zc4x6sg',
    ])
    trainer.train([
    'CPU',
    'The Central Processing Unit (or CPU) is the part of a computer responsible for carrying out the instructions contained in various software programs.',
    ])
    trainer.train([
    'Data',
    'The word “data” means information. It could be facts, figures, words, measurements, observations, or any combination of these things. When you surf the Internet, your browser interprets the data contained in files and resources and displays the results for you on the computer screen. Read more: https://www.mathsisfun.com/data/data.html',
    ])
    trainer.train([
    'Database',
    'A database is a collection of data that is organized in a way that makes it easy for someone to access the information inside in various ways.Read more: http://www.usg.edu/galileo/skills/unit04/primer04_01.phtml',
    ])
    trainer.train([
    'Desktop',
    'A desktop is a computer’s primary user interface. In other words, it’s the screen that can be seen when a computer is first started up. From the desktop, a user can access the files and programs held on the computer.Read more: http://techterms.com/definition/desktop',
    ])
    trainer.train([
    'Digital',
    'A digital method of storing and transporting data is one that uses “discrete signals,” usually numerical codes involving ones and zeros. An example of this is the binary code used by computers. Read more: http://seor.gmu.edu/student_project/syst101_00b/team18/digana.htm',
    ])
    trainer.train([
    'Disk Drive',
    'A disk drive, sometimes called a hard disk drive or simply a hard disk, is a storage device usually found within a computer that can read data from or write data onto a spinning metal disk. Read more: http://www.its.bldrdoc.gov/fs-1037/dir-017/_2535.htm',
    ])
    trainer.train([
    'Download',
    'The word “downloading” refers to accessing digital information. Every time someone visits a website on the Internet, they are downloading a file using their browser. Read more: http://www.cdc.gov/getsmart/campaign-materials/download-files.html',
    ])
    trainer.train([
    'Email',
    'Email, or electronic mail, is a means of sending messages from one person to another over the Internet. Read more: http://www.internetbasics.gov.au/getting_started_on_the_internet/what_is_email',
    ])
    trainer.train([
    'Gigabyte',
    'A byte is a unit used to measure the size of computer data. A gigabyte is equal to 1,073,741,824 (or about 1,000,000,000) bytes. The reason a gigabyte is not exactly one billion bytes is that computers work using a binary system, meaning that everything is measured in powers of two instead of powers of ten. Read more: http://pc.net/helpcenter/answers/kilobytes_megabytes_and_gigabytes',
    ])
    trainer.train([
    'Hardware',
    'The word “hardware” is used to describe all of the physical components that make up a computer. Read more: http://www.cs.ucr.edu/%7Egusta/cs8s05/hardware.htm',
    ])
    trainer.train([
    'Homepage',
    'A homepage is the main page of a website. A homepage serves to welcome visitors and aid them in navigating the other pages on the site. Read more: http://www.public.iastate.edu/%7Ehschmidt/writehomepage2.html',
    ])
    trainer.train([
    'HTML',
    'HTML, or HyperText Markup Language, is the language used for creating Web pages. HTML tells a browser how to display the page on the computer screen. Read more: http://www.usfca.edu/uploadedFiles/Web_Services/website/html_basic_handout.pdf',
    ])
    trainer.train([
    'HTTP',
    'HTTP stands for HyperText Transfer Protocol. It is a set of rules that a browser uses to interpret a website’s HTML code. A website tells the browser to use a certain protocol by identifying it in its Web address, which is why a lot of websites have “Read more: http://” at the beginning of their URLs. https://gustavus.edu/gts/Hyperlink',
    ])
    trainer.train([
    'Hyperlink',
    'A hyperlink, commonly referred to as a link, is a gateway between two documents on the Internet or sometimes two parts of the same document. Clicking a link tells the browser to display the Internet resource located at the address specified in the hyperlink’s HTML code. Read more: http://networking.grok.lsu.edu/Article.aspx?articleId=14849',
    ])
    trainer.train([
    'IP Address',
    'An IP Address, or Internet Protocol Address, is a string of numbers assigned to each computer using the Internet Protocol in a network.',
    ])
    trainer.train([
    'Internet',
    'The Internet is a system that connects millions of computer networks, allowing users to communicate with one another and share resources and information across great distances. Read more: http://fcit.usf.edu/internet/chap1/chap1.htm',
    ])
    trainer.train([
    'JavaScript',
    'JavaScript is an object-based scripting that can be used in conjunction with HTML to make websites more interactive. https://www-s.acm.illinois.edu/webmonkeys/javascript/intro.html',
    ])
    trainer.train([
    'Keyboard',
    'A keyboard is a tool that a person uses to interact with a computer. It consists of a number of keys that can be pressed to give the computer specific instructions. Read more: http://partners.nytimes.com/library/tech/99/08/circuits/articles/12keys-timeline.html',
    ])
    trainer.train([
    'Memory',
    '“Memory” is a word used to describe the temporary storage of information on a computer, separate from the CPU. It is sometimes primary storage or RAM (Random Access Memory).',
    ])
    trainer.train([
    'Modem',
    'The word “modem” is actually short for modulator/demodulator. A modem is an external device that allows a computer to transfer information over telephone or cable lines. Read more: http://www.physics.udel.edu/%7Ewatson/scen103/projects/96s/thosguys/modem.html',
    ])
    trainer.train([
    'Monitor',
    'A computer monitor is the part of the computer’s hardware that displays images for the user. Read more: http://scienceline.ucsb.edu/getkey.php?key=66',
    ])
    trainer.train([
    'Motherboard',
    'A motherboard is the main electronic circuit board in a computer. It connects all of the system hardware. The motherboard usually contains the CPU and the RAM. Read more: http://cs.sru.edu/%7Emullins/cpsc100book/module03_internalHardware/module03-01_internalHardware.html',
    ])
    trainer.train([
    'Network',
    'A computer network consists of two or more computers that are connected in order to allow them to share information. Read more: http://kids.britannica.com/comptons/article-9545133/computer-network',
    ])
    trainer.train([
    'Operating System',
    'An operating system is a set of programs (or software) that allows a user to operate a computer’s various parts (or hardware). Read more: http://www.personal.kent.edu/%7Ermuhamma/OpSystems/Myos/osIntro.htm',
    ])
    trainer.train([
    'PC',
    'PC stands for personal computer. The term refers to any computer that an ordinary individual can use in their home or at a desk, as opposed to a giant supercomputer. Read more: http://digitalunite.com/guides/computer-basics/what-pc ',
    ])
    trainer.train([
    'Pixel',
    'A pixel is a tiny area of illumination on a computer’s monitor. It is the smallest unit of an image on a computer. Read more: http://www.computerhope.com/jargon/p/pixel.htm',
    ])
    trainer.train([
    'Processor',
    'A processor, or a CPU, is the part of a computer that processes and carries out the instructions a user gives it. Read more: http://www.wisegeek.com/how-does-a-cpu-work.htm',
    ])
    trainer.train([
    'Shortcut',
    'A shortcut is an icon that resides on a computer’s desktop and links to a specific program or file. Read more: http://www.gvsu.edu/it/simplesolutions/how-to-create-desktop-shortcuts-in-windows-7-48.htm',
    ])
    trainer.train([
    'Software',
    'The word “software” refers to different sets of instructions, or programs, for a computer to follow. Read more: http://web2.uvcs.uvic.ca/elc/sample/ite/u01/u1_1_03.html ',
    ])
    trainer.train([
    'Spam',
    'Spam is unwanted, or junk, email. Some email providers offer spam filtering, so that these unwanted emails are automatically sent to a special spam folder. Read more: http://www.safecomputing.umich.edu/main/phishing_alerts/',
    ])
    trainer.train([
    'Taskbar',
    'A taskbar is a bar that is usually displayed at the bottom of a computer screen. Often, it contains icons for frequently-used programs. Read more: https://kb.iu.edu/d/ahzg ',
    ])
    trainer.train([
    'URL',
    'Each Web page has a unique string of characters assigned to it, called a URL, or a Uniform Resource Locator. A URL is sometimes called a Web address. When a user types a URL into a browser’s address bar, the browser will display the Web page. Read more: http://www.wou.edu/ucs/faq/urls.php ',
    ])
    trainer.train([
    'USB',
    'So, is that some name for a cool music band? Haha, joking. Ok, lets be serious now. USB stands for Universal Serial Bus. It is a method of connecting computers to external devices like cameras. Read more: http://www.swarthmore.edu/Documents/administration/its/How%20to%20Use%20a%20USB%20Flash%20Drive.pdf',
    ])
    trainer.train([
    'Virus',
    'A computer virus is a program created to steal or damage information on a computer. Read more: http://oregonstate.edu/helpdocs/safety-and-security/computer-viruses-fraud/computer-viruses ',
    'World Wide Web',
    'The World Wide Web is an information system on the Internet that allows hypertext documents to be connected with hyperlinks. Read more: http://www.ou.edu/research/electron/internet/www.htm ',
    ])
    trainer.train([
    'World Wide Web, WWW',
    'The World Wide Web is an information system on the Internet that allows hypertext documents to be connected with hyperlinks. Read more: http://www.ou.edu/research/electron/internet/www.htm ',
    ])
    trainer.train([
    'How to safely browse online?',
    'I totally understand you, bro. Let me explain... <br> The sense of reality often tends to fail when we’re surfing online. It is easy to get lost in the cyber world and forget that it is just as real as everything else in our lives. But rules of conduct and expectations on how people should behave are the same online and in the real world. There are many things you can do yourself to increase your online safety.<br>Do to others as you would have them do to you. Bullying other people online is a malicious act which affects both the bully and the bullied. Pranks can also turn bad, and it might be hard to stop a prank once it has spread across the Internet.<br>Don’t let your friends influence your decisions and principles. When you surf online together with your friends, don’t do things you wouldn’t do alone or in the public.<br>When you see something disturbing, for example hate speech or call for violence, talk to your parents/guardians, teachers, or school psychologist.<br>Read more about safe browsing here: https://greatestcourage.ee/',
    ])
    trainer.train([
    'What does Apollo mean?',
    'Apollo, its me!<br>But there was actually one story there that made me so called. Apollo is the ancient Greek God of Healing, Light, Truth, Medicine, and Music. One of his most important jobs was to bring up the sun every day. Like his sister, he was a great archer, and often carried a silver bow.<br>So am I, lighting up new knowledge that you could feel more comfortable every day.'
    ])
    trainer.train([
    'Use strong passwords',
    'Make sure to include uppercase and lowercase letters, numbers and symbols. Do not use combinations that can be easily guessed – for example, many people know your birthday. Do not use the same password for multiple accounts, because if one account is hacked you may lose control over your virtual identity. Do not share your passwords with anyone, even with your closest friends and family members. The more people know your passwords, the more likely they will leak..'
    ])
    trainer.train([
    'Internet anonymity',
    'Keep in mind that there is no such thing as absolute Internet anonymity. Even if you don’t use your real name of you’ve deleted old photos, videos, or comments, it is possible to find out what device you have previously used or use currently for surfing online. Also, capturing screenshots is very easy, and thus make sure not to post anything you don’t want to go public.'
    ])
    trainer.train([
    'Protect yourself and your devices online',
    'Internet in full of malware that can cause havoc in your devices or use them to spread viruses. It is worth knowing that sometimes you can catch a virus from a website you use daily and which you think is safe. Using antivirus software in your phone and PC is the best protection against viruses. Protecting your devices doesn’t have to cost anything - many antiviruses are free. However, be careful installing any kind of software, including antiviruses - some viruses mask themselves as antiviruses.'
    ])
    trainer.train([
    'Malcious file download',
    'Be careful when sharing files, opening letters/attachments and downloading files – you may end up with a virus, malware, or content which is not age-appropriate or downright illegal. This may happen even when your antivirus is up and running.'
    ])
    trainer.train([
    'I saw the cyberbulling!',
    'Do to others as you would have them do to you, both in the real world and in cyberspace. A simple prank might turn into a nightmare for both the bully and the bullied. Also, keep in mind that once the post is published, it may go viral very quickly, and it might be impossible to stop it. <br>Think about whether your online self reflects who you really are. Do you want to be remembered as a bully whose words and actions have actually hurt someone? <br> All conflicts or arguments cannot be considered as bullying. However, changing the subject on purpose and using condescending tricks to win arguments, create embarrassing situations or influence friendships is usually stressful for all parties. Thus, if there is a motive to hurt the other party with words or something else, then this constitutes as bullying. The greatest courage is not to follow your friends by doing things you wouldn’t do alone or in the public. Stand by your principles, and if necessary, don’t be a bystander when you see something that crosses the boundaries of politeness. <br> Don’t be a bystander when you see someone bullied at school or online. If you don’t do anything to intervene, you might unwillingly help to normalize the behavior. Keep in mind that you can do a lot of good by helping the bullied – support, comfort, and help means a lot more to the victim than you might imagine. It is quite understandable than taking a stand might seem scary – if you need advice or encouragement talk to someone you trust.'
    ])
    trainer.train([
    'bulling, help',
    'Call the free Child Helpline 116 111 (the line is open 24/7) or send an email to info@lasteabi.ee (the reply is sent as soon as possible, but not later than in five business days).'
    ])
    trainer.train([
    'How to recognize cyberbullying?',
    'Some advises from Apollo! <br> <li>Sending threatening or mean letters, text messages, etc. more than once. <li>Scamming personal information, pictures/videos and spreading them across the Internet without consent. <li>Posing as someone else online, breaching trust (e.g. breaking in someone’s email account, using false identity, spreading false information via emails and text messages, and other damaging and humiliating actions). <li>Creating an online space (e.g. website, chatroom) or content to make fun of classmates, or to condescend them, or to fuel hate and animosity. <li>If above mentioned actions involve several bullies and their actions are coordinated and deliberate.'
    ])
    trainer.train([
    'How to recognize cyberbullying?',
    'Some advises from Apollo! <br> <li>Sending threatening or mean letters, text messages, etc. more than once. <li>Scamming personal information, pictures/videos and spreading them across the Internet without consent. <li>Posing as someone else online, breaching trust (e.g. breaking in someone’s email account, using false identity, spreading false information via emails and text messages, and other damaging and humiliating actions). <li>Creating an online space (e.g. website, chatroom) or content to make fun of classmates, or to condescend them, or to fuel hate and animosity. <li>If above mentioned actions involve several bullies and their actions are coordinated and deliberate.'
    ])

    
    x = x+1

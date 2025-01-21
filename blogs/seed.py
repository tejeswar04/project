from bs4 import BeautifulSoup
from selenium import webdriver
from blogs.models import blogs  # Replace `your_app` with your Django app name

def helper():
    # List of topics and their respective Medium URLs
    topics = {
        "Artificial Intelligence": "https://medium.com/tag/artificial-intelligence",
        "Machine Learning": "https://medium.com/tag/machine-learning",
        "Deep Learning": "https://medium.com/tag/deep-learning",
        "Web Development": "https://medium.com/tag/web-development",
        "Cloud Computing": "https://medium.com/tag/cloud-computing"
    }

    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()

    for topic, url in topics.items():
        print(f"Fetching articles for topic: {topic}")
        
        # Open the topic's Medium page
        driver.get(url)
        res = driver.execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(res, 'lxml')
        
        # Find all articles
        articles = soup.find_all("article")
        
        for article in articles:
            # Extract the title
            title_tag = article.find("h2")
            title = title_tag.text.strip() if title_tag else "No title"
            
            # Extract the description
            description_tag = article.find("h3")
            description = description_tag.text.strip() if description_tag else "No description"
            
            # Extract the link to the article
            link_tag = article.find("a", href=True)
            link = link_tag["href"] if link_tag and "medium.com" in link_tag["href"] else None
            
            # Extract the image address
            image_tag = article.find("img", src=True)
            image = image_tag["src"] if image_tag else None
            
            if title and link and image:
                if not blogs.objects.filter(title=title).exists():
                    blogs.objects.create(
                        title=title,
                        img=image,  # Use an empty string if no image is found
                        des=description or "No description",  # Provide a default description if missing
                        link=link,
                        words=topic  # Add the topic as the `words` field
                    )
                    print(f"Added blog: {title}")
            else:
                print(f"link or img not there already exists: {title}")

    # Quit the driver after processing all topics
    driver.quit()

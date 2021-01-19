'''
Ask which type of post - category
Reference - URL
Reference - Ttile
'''
from datetime import datetime
def getCategory(categories):
    
    def printCategories(categories):
        for (index, category) in enumerate(categories):
            print(f"{index + 1}. {category.title()}")

    printCategories(categories)

    while True:
        category_input = input('Enter the category: ')

        try:
            if category_input.strip() == 'q':
                return ""
            category_index = int(category_input) - 1
            if category_index >= len(categories) and categories < 0:
                print("Invalid category. Please select a valid category, or enter q to exit")
            else:
                return categories[category_index]
        except:
            return None

def getPostInfo():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    date_time = now.strftime("%Y-%m-%d %H:%M:%S +0530")
    

    slug_input = input('Enter the slug: ')
    slug = slug_input.replace(" ", "-")

    post_file_name = f"{date}-{slug}.html"

    title_input = input('Enter the Post Title: ')
    subtitle_input = input('Enter the Post Sub-Title: ')

    reference_url_input = input('Enter the Reference URL: ')
    reference_title_input = input('Enter the Reference Title: ')
    
    return (date_time, post_file_name, title_input, subtitle_input, reference_url_input, reference_title_input)

def createPost(category, post_file_name, date_time, title, subtitle, reference_url, reference_title):
    from jinja2 import Environment, FileSystemLoader
    import os
 
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates_1')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('post.txt')
    
    post_dir = os.path.join(os.path.join(root, 'fit.n.geeky'), '_posts')
    filename = os.path.join(post_dir, post_file_name)
    with open(filename, 'w') as fh:
        fh.write(template.render(
            category = category.title(),
            date_time = date_time,
            title = title.title(),
            subtitle = subtitle,
            reference_url= reference_url,
            reference_title = reference_title
        ))
        return True

    return False
if __name__ == "__main__":
    categories = [
            'science',
            'technology',
            'health'        
    ]
    category = getCategory(categories)
    print(f"category = {category}")

    if category in categories:
        (date_time, post_file_name, title, subtitle, reference_url, reference_title) = getPostInfo()
        status = createPost(category, post_file_name, date_time, title, subtitle, reference_url, reference_title)
        print(status)
    else:
        print('Exiting..')

# # input 
# input1 = input() 
  
# # output 
# print(input1) 
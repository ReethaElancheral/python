# 3. Paginated News Headlines 
# Goal: Simulate pagination of headlines from a news list using a custom iterator. 
# Requirements: 
#  Show 3 headlines per page 
#  Use class-based iterator 
#  Allow moving to next/previous page using input 

class PaginatedNews:
    def __init__(self, headlines, page_size=3):
        self.headlines = headlines
        self.page_size = page_size
        self.total_pages = (len(headlines) + page_size - 1) // page_size
        self.current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_page >= self.total_pages:
            raise StopIteration
        start = self.current_page * self.page_size
        end = start + self.page_size
        page = self.headlines[start:end]
        self.current_page += 1
        return page

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 2  
            return True
        return False

    def reset(self):
        self.current_page = 0

def main():
    news = [
        "Economy grows 5% in Q2",
        "New species of bird discovered",
        "Tech stocks rally on earnings",
        "Global summit on climate change",
        "Local elections results announced",
        "Sports team wins championship",
        "New movie breaks box office records"
    ]

    paginator = PaginatedNews(news)

    print("Paginated News Headlines (3 per page). Enter 'n' for next, 'p' for previous, 'q' to quit.")
    while True:
        try:
            page = next(paginator)
            print("\n--- Page", paginator.current_page, "---")
            for headline in page:
                print(headline)
        except StopIteration:
            print("\nNo more pages.")
            break

        cmd = input("Command (n-next, p-prev, q-quit): ").lower()
        if cmd == 'q':
            print("Exiting pagination.")
            break
        elif cmd == 'p':
            if paginator.prev_page():
                continue
            else:
                print("Already at first page.")
        elif cmd != 'n':
            print("Invalid command, please enter 'n', 'p', or 'q'.")

if __name__ == "__main__":
    main()

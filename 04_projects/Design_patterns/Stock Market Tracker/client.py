from app import StockFeed,mblAppObserver,webDashboardObserver,tradingBotObserver

if __name__=="__main__":
    #create subject
    sub=StockFeed()
    
    # Create observers
    mbl=mblAppObserver()
    wd=webDashboardObserver()
    tb=tradingBotObserver()
    
    #Attach observers
    sub.attach(mbl)
    sub.attach(wd)
    sub.attach(tb)
    
    # Simulate stock price updates
    sub.set_price("Tesla",500)
    sub.set_price("Apple",1500)

    # detach observers
    sub.detach(wd)

    sub.set_price("Samsung",2000)
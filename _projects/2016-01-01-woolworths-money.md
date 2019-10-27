---
title: 'Woolworths Money'
subtitle: 'Credit Cards & Budgeting App <br>2016-2017'
date: 2018-06-30 00:00:00
description: This page is a demo that shows everything you can do inside portfolio and blog posts.
featured_image: '/images/woolworths-money-2.png'
---

![](/images/woolworths-money-2.png)

<center><a href="https://apps.apple.com/au/app/woolworths-money/id1002309281" class="button button--large">Woolworths Money iOS</a> <a href="https://play.google.com/store/apps/details?id=com.woolworths.money&_ga=1.216904342.1412740904.1445813585" class="button button--large">Woolworths Money Android</a></center>

## Manage your Credit Cards, Check your balance, View Transactions and Earn Rewards

Australia's largest national supermarket [Woolworths](https://www.woolworths.com.au/) is also a large provider of [Credit Cards](https://cards.woolworths.com.au), Gift Cards and Rewards Cards. In order to allow customers to manage their cards, Woolworths released an app called Woolworths Money. Users could add their Credit, Gift and Rewards cards to easily check their balance, view transaction history and earn more rewards.

While at [Bilue](https://bilue.com.au/), I was a core member of a small 2 person team responsible for implementing a Version 2 re-design of the existing application to be faster, easier to use, and to focus more on providing meaningful financial insights to users.

I implemented a custom UICollectionViewLayout that resembled [Apple's Wallet](https://apps.apple.com/us/app/apple-wallet/id1160481993) interface, built a radial navigation menu and an Error Message Generator script which allowed copy writers to edit error messages and text content displayed throughout the app without having to write any code.

### App Architecture

![](/images/woolworths-money-architecture.png){:height="1200" width="1200"}

Our application was primarily Objective C, with some Swift files. We used the [MVVM](https://www.objc.io/issues/13-architecture/mvvm/) (Model, View, ViewModel) architecture to model the data flow throughout the app and stored sensitive user credentials (Card Numbers, Passwords etc) in the Keychain. We split out core business logic into an embedded framework called 'WoolworthsMoneyCore' and everything platform specific remained in the main iOS target. 

This enabled us to write Unit Tests for our core business logic without spending too much time writing unit tests for our User Interface which was constantly in flux as we progressed through the re-design of the interface. It meant that the platform agnostic layer of the app could be re-used and building a watchOS application in the future would be trivial.


### Features

![](/images/woolworths-money-features1.png){:height="600" width="1200"}

#### Custom UICollectionViewLayout

At the center of this UI re-design was a Wallet style card interface which allowed users to view their cards as a stack. They could long press to pick up a card, and drag to re-position it within the stack. In order to achieve this, I wrote a custom UICollectionViewLayout subclass which constructed `UICollectionViewLayoutAttributes` for each cell and supplementary view, calculating the correct frame in order to position the cards above each other in a stack. As the user long pressed on a card in the stack (a cell in the UICollectionView), it animated a snapshot of the cell into its new position and updated the underlying IndexPaths. Spacing of the cards was configurable, and would change based on the number of cards in the stack in order to make use of the available space.

Tapping on a card would animate the card into its full screen `CardDetailViewController` where the user could view transactions, and manage a specific account. Placeholder cards were added to the UICollectionView based on specific business rules, such as the existence of a rewards card, or a credit card. These cards would prompt the user to setup a new account, or add their rewards card if they hadn't already. I wrote a comprehensive set of Unit Tests injecting different data sets of cards to validate that the placeholder cards 

#### Radial Buttons Animation

![](/images/woolworths-money-radial-menu.jpg){:height="600" width="1200"}

Re-thinking the navigation of the Wooolworths Money app, we looked at the actions users took most frequently and designed a Radial Menu on the main wallet screen, allowing users to quickly and easily get to what they need the most. I was responsible for implementing the radial menu component natively, ensuring the menu supported adding and removing action buttons dynamically based on the card's contained in the user's wallet. The menu also needed to animate smoothly while also being accessibility friendly.

I implemented the component as an `AnimatedMenu` view which acted as a container for `AnimatedMenuItem` views. I designed the component to behave similarly to a `UICollectionView`, being driven by an `AnimatedMenuDataSource` which provided the data for displaying menu items, and an `AnimatedMenuDelegate` providing callbacks for events such as menu item selection events.

![](/images/radial-menu-code.png){:height="600" width="800"}

When the user tapped to open the menu, I used a combination of `CGAffineTransform` rotation and translation animations along a curve and with delayed offsets to perform the open and close animation. When combined together, the menu items would fan out and fan back in coordination with each other. Once open an opaque white background view would fade in, acknowledging to the user that the menu was open.


#### Error Message Generator

![](/images/woolworths-money-errors.jpg){:height="600" width="1200"}

One of the biggest requests from our client from v1.0 of the app was the ability to quickly and easily update the textual content throughout the app without having to involve engineers and writing code. Being a banking app, the client had to comply with a lot of regulation, and include a large amount of timely legal copy in many different parts of the app. Updating this content frequently had become un-manageable and involved too much back and forth communication with engineers.

I worked alongside another engineer and we wrote a Swift script that would parse an XSLX document, generating a valid JSON output that could be dropped into the Xcode Project in order to update copy such as error messages, alerts, and important content. When displaying UIAlertViews, Progress Indicators, Legal text and any other static text, the text would be serialized from the `app-copy.json` file that had been generated, using unique identifiers. By swapping out the `app-copy.json`, static text could be updated immediately throughout the app without writing any code.

### What did I learn?

I worked alongside 1 other engineer on the Woolworth's Money iOS app, which was a unique opportunity for me to take a larger responsibility in the core parts of the app architecture and overall user experience. By working on a re-design of an existing product, I inherited a codebase from someone else and learned about how to deal with technical debt and foreign systems and APIs with varying levels of documentation.

I spent a lot of time thinking about the User Experience, and design of the interface. This gave me a lot of opportunities to pickup and learn Core Animation, Core Graphics, and UIKit Animations. I implemented custom View Controller transitions, a complex radial menu animation, a completely custom UICollectionViewLayout and a variety of inline progress indicators which prioritized concurrency over blocking the UI for the user.

I learned about the intricacies of working on a banking product, and a lot of the regulatory processes that need to be taken in to consideration to ensure that the product is secure and trustworthy for users.
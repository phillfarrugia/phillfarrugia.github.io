---
title: 'Woolies Shop'
subtitle: 'Shopping List & Groceries eCommerce Platform <br>2015-2016'
date: 2018-06-30 00:00:00
description: This page is a demo that shows everything you can do inside portfolio and blog posts.
featured_image: '/images/woolies-shop.png'
---

![](/images/woolies-shop.png)

<center><a href="https://www.woolworths.com.au/" class="button button--large">Woolies Shop Web</a> <a href="https://apps.apple.com/au/app/woolworths/id975089690" class="button button--large">Woolies Shop iOS</a> <a href="https://play.google.com/store/apps/details?id=com.woolworths" class="button button--large">Woolies Shop Android</a></center>

## Create Shopping Lists, Browse Products and View Recipes with Woolies Shop

Before Amazon brought on the rise of Digital Commerce, Australia's largest national Supermarket [Woolworths](https://www.woolworths.com.au/) invested in building out a digital platform enabling customers to browse and purchase their groceries online. 

During my time at [Bilue](https://bilue.com.au/), I was a core member of a team of 5 Engineers tasked with building out the iOS application. We worked with design firm [Neotony](http://neoteny.com.au/) as well as in-house Designers, Product Managers, Backend, QA and Web Engineers to build a powerful, user-friendly solution that became Australia's leading online shopping service.

As a Software Engineer on the iOS team, I was responsible for implementing user-facing features such as Shopping Lists, Online/Offline Sync, Recipes and one of [Australia's first Apple Watch apps](https://www.smh.com.au/technology/woolworths-unveils-apple-watch-app-20150402-1md9ms.html). I contributed to the team's Continuous Integration pipeline where I wrote custom build scripts to compile the project, run Unit Tests ([Quick and Nimble](https://github.com/Quick/Quick)) and code sign the IPA to be deployed to the App Store. 

### App Architecture

Our application was entirely Objective-C, used an event driven [MVVM](https://www.objc.io/issues/13-architecture/mvvm/) (Model, View, ViewModel) architecture, handled data flow using [ReactiveCocoa](https://github.com/ReactiveCocoa/ReactiveCocoa) and stored data on-device in a [Core Data database](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html). We used Git as Version Control, wrote Behavioural Driven Unit Tests ([BDD](https://github.com/Quick/Quick)) and defined all AutoLayout constraints programmatically.

### Features

![](/images/woolies-features.png){:height="600" width="1200"}

#### Shopping Lists

I worked on the implementation of the Lists feature which enabled users to create Shopping Lists. Users could add Free Text items (such as "Milk", "Sugar", "Coffee") and Product-based items which linked to real, purchaseable products. List items were queried, updated and saved to an NSManagedObjectContext which persisted to disk in an NSPersistentStore using [Core Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html).

#### Online/Offline Sync

![](/images/woolies-shop-diagram.jpg){:height="600" width="1200"}

Users were able to add, update and remove products from their lists while offline. I worked closely with the Backend Engineers to architect, and implement an Online/Offline Sync solution which had to deal with conflict resolution in a simple, and user friendly manner. We were required to rely on the server to be the source of truth for conflict resolution, and to never require the user to select from two conflicting changes. Sync was designed to be a UI blocking action, and was not required to stay continously up-to-date in the background.

In our solution, each List owned a `lastSyncedTimestamp` which was an Epoch timestamp representing the last time the list was synced with the server. A `WOWMasterListSyncManager` mapped each list to a `WOWListSyncManager` which wrapped a `WOWListModel` and synced it with the server. A full-sync required sending each List and its timestamp to the server. In the response, was the Additions, Updates, and Deletions of the items within the list since the last sync. The `lastSyncedTimestamp` was updated upon each sync. 

#### Recipes

I was also responsible for building the Recipes feature within the app, which allowed Users to view a curated list of Featured and Sponsored Recipes. Recipes were fetched from the Server and displayed in a `WOWRecipesViewController` which supported sorting alphabetically in Ascending or Descending order. Each `WOWRecipeDetailViewController` featured a large full-bleed high resolution feature image, a table of ingredients and a plain text method of cooking. In order to provide a seamless user experience despite having to load large high resolution images, I designed and implemented a solution which displayed a blurred placeholder thumbnail image, which animated into the high resolution image once fetching was complete.

Since the number of ingredients, and the method information was dynamic based upon the recipe - I was required to use dynamic manipulation of a combination of AutoLayout constraints, Frames/Bounds, and CALayers to size and fit the recipe information into the available screen space. This meant that we were able to deliver the user a completely tailored user experience that felt very luxe and high end but was unique to each individual recipe.

#### Apple Watch

![](http://www.executivestyle.com.au/content/dam/images/1/m/d/s/c/j/image.related.articleLeadwide.620x349.1md9ms.png/1427956282544.jpg)

During the initial launch of the Apple Watch, I led the development of one of the first Apple Watch apps available in Australia. This involved working closely with Apple using the initial implementations of what would later become the WatchKit SDK. At the time, data was shared between the Apple Watch and the iPhone using dynamic messaging, and then eventually shared App Containers. I modified the app's CoreData stack to share an NSPersistentStore within a shared App Container allowing both the Apple Watch and the iPhone applications to remain in sync. As users added items to their Shopping Lists from their phone, they could quickly check the items off the list from their watch in store.

I worked with an early version of MapKit for watchOS that enabled displaying a WKMapView and marking certain latitude and longitude coordinates on the map. This allowed users to see nearby stores from their wrist, and to get walking/driving directions to their nearest Woolworths store.

### Continuous Integration

![](/images/woolies-ci.png){:height="600" width="800"}

Our team adopted a continuous delivery approach to the release cycle which enabled us to consistently deliver features and bug fixes to the client on a daily basis. This meant that we needed a comprehensive set of build scripts which automated the process of executing unit tests, generating an IPA and uploading the IPA to HockeyApp. I maintained the release process, managing a fleet of CI machines across several projects and ensured that environment issues were resolved quickly so that clients received their builds each day.

I wrote seperate Bash scripts for each step of the build pipeline - configuring environment variables, updating dependencies, installing dependencies, executing unit tests, executing UI tests, compiling the project, codesigning, generating an IPA and deploying the IPA to HockeyApp/Testflight. I learnt about the contents of an IPA file, how a binary is code signed and can be re-signed, and the importance of delivering builds to clients on a consistent and regular basis.

### What did I learn?

While working on the Woolies Shop project I began to solidify my knowledge as an iOS Engineer, building up my confidence in how to work well on a team. Working alongside 5 other engineers, I learned how to take a flexible and open minded approach to writing code. I contributed to a shared style guide, encouraged everyone to define a set of best practices throughout our souce code and participated in retrospectives and sprint planning meetings, helping us to communicate effectively and work in clearly defined sprint cycles to continually deliver high quality code. 

Most importantly, being on this team taught me the importance of Code Review. I learnt to be deliberate about writing descriptions, communicating clearly about the changes being made and the context around them. I learned to be meticulous about reviewing team member's work and encouraging them to iterate and improve. It taught me the long term value this provides when maintaining a large codebase and trying to understand the historical reasons for decisions that were made.


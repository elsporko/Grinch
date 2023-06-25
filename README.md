Grinch is a tool built to assist with my son's annual boy scout Christmas Tree
pickup fundraiser. The idea is to supplement the current CRUD application that
allows customers to request a pickup for the upcoming event. The legacy
application produces route sheets that are handed out to the volunteers. Over
the past few years the route sheets have been turned into online maps to allow
for ease of navigation and planning out paths.

The process requires lots of manual intervention including distributing routes
to teams, importing route data into existinng applications, and reporting any
issues while working the route (no tree, no donation, tree left for pickup, but
not on currently scheduled for pickup, etc). The grinch application looks to
automate the manual steps as well as to add other useful features. Grinch looks
to provide a consistent replacement for existing map fechnologies whose useful
features may disappear.

Features of the application
    * user management:
        * View all users
        * Create new users 
        * Deactivate existing users
            * Perhaps an existing user cannot participate in pickup one year,
              but the account should be preserved for next year.
            * Delete users - not reccomended in order to keep track of
              historical data.
            * Mark users inactive
        * Map users to routes

    * route management:
        * Recieve routes from legacy app via API
            * In order to further the grinch project there is no reliance on
              the lagacy API to import information as there is a path to imort
              as long as picklists can be exported and used as imports into
              Grinch.
        * Assign users/user groups to routes
        * View routes as pinned map data
        * Manipulate the connection between routes and groups - This can be
          done between non-admin users as well
        * If there is a need to use long/lat values to identify addresses then
          there will be a table that stores long/lat values then the process
          should follow the legacy application method of using Google for the
          GIS values. Those values will be stored locally so that we can build
          up our own table of address to long/lat mappings and look there first
          before reaching out to Google. This will cut down the number of API
          calls and lessen the dependency on a 3rd party over time.
        * Mark pickups live
            * Options for pickup:
                * Got tree
                * Got donation
                * Got donation and tree
            * Optional leave comments (No tree, called and left a message, etc.)
            * Customer phone number will be a link that can be used to call the
              customer from the app

    * Transaction logs:
        * view group reassignment
        * Field issues reported

    * Communication
        * Ability to semd a brpadcast message to all active useres or to send a
          message to specific users
        * Messages will be received even if the uswer is no logged in
        * Messages should be archived in the data base
        * Messages must be sent and (when possible) received in real time
        * How to handle threads that are not broadcasts (perhaps a reply button
          to all non broadcasts).

Admin users will be able to access all parts of the application.

Standard users are allowed to use the communication and route management
pieces. Standard users will only have access to the map that they are assigned
to, but can reassign a pickup to any other active user except admin.


Workflow
    Setup performed by the admin user
    =====

    Create/edit routes. Standard routes are named after the 5 weekdays (routes are based on
    the town trash collection days), but the system needs to be flexible to
    handle years when the number of available tow vehicles does not match that
    total. Routes can be made inactive to meet event needs. For example if
    there are only 4 vehicles available the routes can be distributed among the
    drivers and one of the existing routes can be deactivated. If there are 6
    vehicles available a new route can be created that can be made inactive in
    the future.

    Create/edit users (name, route, email address). Users of this system are
    defined as those who will be managing tree pickup including drivers,
    navigators and an admin account. User information includes a name, route
    and email address.

    Import scheduled pickups from legacy system. This should be done through an
    API on the pickup regstration application, but for now scripts exist that
    take the picklist dump files and import the data into Grinch. Each list of
    pickups is called a picklist with each record identifying an individual
    tree pickup request. Data points for the picklist imported into grinch
    include:
        * order_id - Unique value inherited from signup app
        * pickup_date - Requested date of pickup

        * route - Identify which route to which the entry belongs. This can be
          changed by either the admin user or by any user assigned to the
          route.

        * first_name - First name of customer
        * last_name - Last name of customer
        * home_phone - Phone number of customer. When this data appears in the
          application it will allow for the user to call the customer directly.
        * email - Email address of customer. This can be used as a backup
          communication link if the customer is not available be phone.
        * street_address - Street address of customer
        * where_is_it - Expected location of the Christmas tree (INFRONT,
          OUTBACK, DRIVEWAY, etc.)
        * client_comment - Specific comment from the customer

    In addition to the data from the legacy system a picklist record will
    include:
        * admin_comment - Comments provided by the user about a pickup. This
          can be used to track any issues.
        * got_money - Flag to indicate that donation has been received
        * got_tree - Flag to indicate that the tree has been picked up
        * latitude - Latitude value of the street address (Decimal(8,6))
        * longitude - Longitude value of the street address (Decimal(9,6))

    A pickup is considered complete when both the got_money and got_tree flags
    are set to True.

    Latitude and longitude values are required by Leaflet (javascript library
    that this project intends on using for map interactions). The existing
    registration app had a means of calculating these values through a google
    API. That process will be reused in Grinch, however there will be a table
    to tie lat and long to addresses that will be a first source. If the
    address is not in the table, then it will call out to collect GIS data and
    store it locally. The structure of the lat/long lookup table is:
        * Address
        * Latitude value
        * Longitude value

    The admin sets the routes for individual users. The admin will be able to
    view all of the details for all routes. Routes are displayed as color coded
    pin points on a map to be able to distinguish between them. As plot points
    are updated by the users the pin colors will change to show progress. This
    can allow the admin to distribute more balanced route planning. Only one
    pick up day will be active at a time.  When the admin feels the routes are
    ready for distribution a flag is set to activate the day and an email
    will be sent to users with a link to their assigned route.

    Tree pickup usage workflow
    ==========================
    Each individual user will only be able to view the route that has been
    assigned to them. Once admin has activated the date and the email is
    received users will be able to view their own map. As users pull up to a
    customer's site for pickup a modal will pop up displaying the customer
    name, phone number, email address and the ability to identify the pickup as
    complete or partial (got tree, got money). There will also be a text space
    to provide further details. These details will be pushed back to the
    application allowing the admin to know of any issues. Once a pickup is
    marked either complete or partial the modal will no longer appearwhen
    passing by the address.  All updates to the route will be available in
    realtime so that the admin and other users in the same route will receive
    updated information. The route will also be available in a list context so
    that pickup information can be searched and edited.  If there is a problem
    with the pickup (sometimes we need to pester them for the donation) the
    phone number will be a link that the user can use to call the customer
    directly. If there is a problem with the phone number (voicemail full,
    etc.) then the email can be used as a backup to contact the customer. 

    Individual pickups can be reassigned to other users by either the admin
    user or the owner of the pickup. Any pickups that are to be reassigned will
    be switched to the route of the new owner.

    In addition to sharing route information there is a real time communication
    chat capability. All active users will receive all communications even if
    they are not logged in.

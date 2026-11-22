# omarchebbo.com: all changes (Demo + Original Website)

- Demo: https://claude.ai/artifact/F7ffVQaqiRtgy4XD8k9FCi
- Handoff doc: https://claude.ai/artifact/L7iwQCv3ywNhvE7hZEmqp4
- Code: this folder (`web-demos/demo-original-mixed/`, one `index.html` plus `img/`), branch `ccr-72a2b1ad-6o2sbb`. Use it as the reference for layout and behavior, then build it into the Next.js + Sanity site.

## Whole site
- Built phone-first. Nothing scrolls sideways from 320px to 1366px wide. Every button and link is at least 44×44px, text is at least 12px, and form fields use 16px text so iPhones don't zoom in.
- All motion is gentle and stops when the phone has Reduce Motion turned on.
- The header stays at the top while scrolling (sticky), and links to sections leave room for it.
- New news strip above the header: one line, for example "Short: Why are bananas banned on dialysis? · Watch →", which opens the video. It has a close button, and closing is remembered. Later it can announce the AUBMC donation.
- Header: logo (home) · The book · Start here · Free guides · Videos · My story · Shop, an outlined "Get your copy" button (the gold one in the hero leads), and a cart icon with a number badge that bumps when something is added. Between 900px and 1150px wide, the links move into the menu.
- New full-screen phone menu: Home, The book, Start here, Free guides, Videos, My story, Shop, then Blog, Gallery and Contact (smaller, with ↗). The current page is marked. At the bottom: "Get your copy", "Get the monthly letter →" and the Instagram, TikTok and YouTube icons. The links slide in one after another.
- One buy label everywhere: "Get your copy". The book page keeps "Buy now — $9.99".
- Form errors show as a red message under the field, not as a pop-up.
- The browser Back button returns visitors to the same spot on the homepage.
- Keyboard use: the closed cart and menu are skipped by the Tab key, the focus outline is dark with a gold halo, and Escape closes every pop-up.
- Arabic text uses Noto Sans Arabic (Google Fonts).
- Colors: keep the current palette (slate, gold, cream, ink). The demo's top bar (color dots and "Review") is only for the demo.
- Colors follow 60 / 30 / 10: cream about 60% (main background), slate about 30% (secondary), gold as the accent (buttons, highlights, a few bands). Measured: homepage 56 / 34 / 10 (phone and computer); book page and shop about 61 / 35 / 3.
  - Slate: the news strip, the book section, the story timeline, the first quote band and the footer, plus a panel behind the book cover and behind each shop product picture.
  - Gold: every main button (including the shop's "Add to cart" and "Pre-order"), the "always choose the sky" quote band, the "Become a donor" section, the timeline line and dates, and a gold underline on key heading words.

## Site structure (new)
- The homepage is now a home page, not a long scroll of everything. In its first look it tells a visitor three things: who Omar is, what's here for them (his book, and free help for patients and families), and why it matters (net profits go to dialysis care at AUBMC).
- Anything that was repeated got its own page, reached by a button:
  - Start here (#start): the body map, the situation buttons and the blog posts.
  - Free guides (#guides): the guides, plus "Not sure which guide? Start here".
  - Videos (#videos): all 12 shorts in a grid, plus "All videos on YouTube ↗".
  - My story (#story): About, the timeline, both quote bands, the before/after photos, and "It's all in the book" with "Read the first page".
  - Privacy & terms (#privacy): a draft for Omar to approve, linked in the footer.
- Each new page starts with "← Home" and ends with buttons to the other free resources, so there's no dead end.
- The homepage went from about 12,500px to 5,500px tall on a phone.
- Visitor paths:
  - Supporter: hero → "Read the first page" → preview → "Keep reading — $9.99" → cart → Whish.
  - Patient or family: hero → "Free help" → Start here, Free guides, Videos or Posts.
  - Curious about Omar: "The short version" → "Read my story" → "Read the first page".
  - Organizer: My story → "Invite me to speak ↗".

## Homepage, top to bottom
- Removed: "2 introductions sold", the test reader reviews, "The journey, in pictures" and the second newsletter form. Moved to their own pages: Start here, the free guides, the shorts, the blog, the timeline, the before/after photos, About and the two quote bands.
1. Hero
   - Small line "Author of *Beyond the Body, Beyond the Pain*", then the heading "I'm Omar Chebbo." and one sentence.
   - Buttons: "Read the first page" (opens the free preview of the introduction) and "Free help" (goes to the Free help section).
   - New line: "Net profits from the introduction go to dialysis care at AUBMC."
   - Numbers that count up: 3 organ transplants, 11 years on dialysis, 26+ years of the journey.
   - "Now" line with a pulsing dot: "The full memoir comes out in June 2027."
   - The graduation photo fills the box that was empty, with the quote card "And yet, I am more myself than I have ever been."
   - New "▶ Who I am · 1 min" play button on the photo. It's a YouTube video that loads only when tapped. Until the real video is ready, it uses the short "One year since my kidney transplant".
2. Book section
   - Same order on every screen size: title, cover, then text.
   - Labels: PDF · Sent by email · Read in one sitting.
   - Gold "Get your copy — $9.99" button with a heartbeat. On tap it fills, adds the book and opens the cart.
   - "Preview the first page" shows the first four paragraphs of the introduction, then "Keep reading — $9.99".
   - New "Where the money goes" box: the net-profits sentence, then "I've already made a first donation. See the hospital's signed confirmation ↗". That link opens a one-page Google Drive document in a new tab.
   - The donation progress bar and numbers stay hidden until there are real numbers. The "Verified by AUBMC" badge stays hidden until the document is ready.
   - "Read it? Email me what you thought →" opens an email. Reader quotes stay hidden until there are 3 real ones.
   - A sticky "Get your copy" bar slides up at the bottom once the buy button has scrolled out of view. It only shows on the homepage and the book page, never on the free-help pages.
   - The IV-bag drip on the cover was removed.
3. New section, "Free help: For patients and families"
   - Four buttons, each with a picture and one line: Start here, Free guides, Videos, Posts. Each opens its own page.
4. New section, "My story: The short version"
   - Three moments with pictures: 2006 My dad's liver · 2013 Dialysis at fifteen · 2024 A kidney from my brother.
   - "Read my story" (opens My story) and "▶ Watch my story · 1 min".
5. FAQ: 7 questions. New ones:
   - "How do I get the book after paying?"
   - "How do I pay?" (with Whish)
   - "How do I know the money reaches AUBMC?" (with the document link)
   - The answer about inviting Omar to speak now links hello@omarchebbo.com and the Contact page.
6. New section, "Become a donor" (gold): "My dad gave part of his liver. My brother gave a kidney.", with "How to register in Lebanon ↗" opening https://www.nodlb.org/.
7. Newsletter: one sign-up form only. After signing up, the form turns into a thank-you line.
8. Footer
   - Links: The book, Start here, Free guides, Videos, My story, Shop, Blog ↗, Gallery ↗, Contact ↗, Privacy & terms. Plus the social icons.
   - New: hello@omarchebbo.com as a tappable email link.
   - The medical notice and copyright.

## Start here page (#start)
- "Tap the body": a body map with 7 characters from the shorts, each with a count of its items. Tapping one shows the top 3 items, the first marked "Start with this", plus "See all". The characters bob three times, then rest.
- A guide item opens the Free guides page and highlights that guide. A story item opens My story at the timeline.
- "Your situation": four buttons (on dialysis, waiting for a transplant, just had a transplant, family or friend), each showing matching posts and videos.
- Blog: topic buttons with counts, compact rows (photo, title, date, read time) and "All posts →". Empty topics are hidden.
- At the end: buttons to Free guides and Videos.

## Free guides page (#guides)
- Two PDFs that download directly, with no email needed.
- The cards are in Arabic only: Arabic title, description and page count.
- New kidney animation on "Get it free": the kidney fills, beats once and lets a drop out. Then a kidney with a check shows "Your PDF is downloading." and one next step: "Next: read the first page of my memoir →".
- Two "Coming soon" cards with "Tell me when it's out" (email box).
- The cards sit in a grid (one column on phones).
- At the end: "Not sure which guide? Start here" and Videos.

## Videos page (#videos)
- All 12 shorts in a grid: 2 across on phones, 4 on tablets, 6 on a computer.
- Each shows its Arabic title with an English line under it.
- Tapping opens a full-screen vertical viewer with swipe or arrows, "Watch on YouTube" and the count "1 of 12".
- "All videos on YouTube ↗", then buttons to Start here and Free guides.

## My story page (#story)
- About first: "Hi, I'm Omar." and the text, then the "Who I am · 1 min" video picture (it replaces the hospital-bed photo, which repeated the timeline).
- Story timeline: 7 moments, each with a photo or a character, and a line that fills as you scroll. Facts: kidney failure at fifteen, dialysis from March 2013 to 2024, and a new kidney from his brother Amine on 13 June 2024. Tapping a photo opens it larger in a pop-up.
- Quote band (slate): "Dialysis doesn't restore life. It postpones death — and in that borrowed time, I learned to live."
- "The same body, the same life": three before/after drag sliders (dialysis and paragliding, fistula and diving, catheter X-ray and shooting range).
- Quote band (gold): "When you feel limited or stuck, always choose the sky."
- End: "It's all in the book." with "Read the first page" and "Invite me to speak ↗".

## Privacy & terms page (#privacy)
- A draft in plain language for Omar to approve: what is collected and why, payments with Whish, emails and unsubscribing, free guides, all sales final, what the site remembers, not medical advice, and contact.

## Book page (#book)
- "← Back" returns to where the visitor came from ("← Back to the shop" from the shop, "← Home" if they landed there directly).
- On phones the cover is smaller, and the title, price and buttons come first.
- The quantity picker is removed. Two buttons: "Buy now — $9.99" (heartbeat) and "Add to cart" (the cover flies into the cart).
- "Sent to your email right after payment."
- "Preview the first page", then a numbered "What's inside" list with 4 items taken from the introduction.
- The "Where the money goes" box and a short "Good to know" box.
- "You might also like": three cards with their own pictures. Long titles wrap instead of being cut off.

## Shop (#shop)
- Removed the search box, the category list and the price slider. Kept three buttons: All formats 4 · Digital 2 · Physical 2. This also fixes the wrong "All categories" label.
- Each product has its own picture.
- Products:
  - Introduction: $9.99, "Add to cart"
  - Ebook: $14.99, pre-order, sent by email in June 2027
  - Hardcover: $35, pre-order, free delivery, signed or unsigned
  - Bundle: $41 (was $44.99), pre-order
- The "Only 2 left" and "Only 3 left" stock badges are removed.
- Three boxes under the cards:
  - Delivery: "The introduction arrives by email right after payment. The full memoir comes out in June 2027: the ebook by email, the hardcover with free delivery."
  - Refunds: "All sales are final."
  - Where the money goes.

## Cart and checkout (new)
- The cart is a side panel that fills the screen on phones. It ends in a full checkout: Cart → Details → Payment → Order confirmed.
- Cart
  - Each item shows its delivery line ("Digital · sent by email", "Pre-order · by email in June 2027", "Pre-order · ships June 2027 · free delivery").
  - Quantity buttons only for physical books, a Remove link and the subtotal.
  - "Free guides · download" with Download buttons. Guides are never cart items.
- Details
  - Step bar, order summary and an email box.
  - A delivery address for hardcover orders: name, phone, city or area, street and building.
  - One line per item on when it arrives, then "All sales are final, no refunds."
- Payment: with Whish. It shows the total, "Receipt to", "Deliver to" and "Delivery: Free", then "Pay $X with Whish", which shows "Opening Whish…" and sends the buyer to Whish.
- Order confirmed
  - "Thank you!" and "Download the PDF" (when the introduction was bought).
  - The June 2027 lines for the ebook and the hardcover.
  - The donation document link.
  - "Get my monthly letter" and "Back to the site".

## Wording and content fixes
- One donation sentence everywhere.
- Ages corrected: dialysis at fifteen (born 6 July 1997, dialysis from March 2013).
- The introduction is a PDF only (no EPUB). Nothing says "instant download"; it's sent by email.
- Repeated wording removed ("opening pages", "eleven years", "only teenager in the ward", and the medical notice now appears only in the footer).

## Notes for building it
- Whish payment
  - Use Whish Pay's redirect checkout: create the payment on the server and confirm the order only from Whish's callback.
  - It needs a Whish Business account.
  - Check with Whish whether buyers outside Lebanon, or without a Whish account, can pay.
- YouTube videos (shorts viewer, "Who I am") should load only when tapped (youtube-nocookie.com), showing the thumbnail until then.
- Sanity
  - Tag shorts and posts with organs, situations and priority; shorts also get an English title.
  - New content types: Free guide, Donation (with the document link), Reader quote and Timeline moment.
  - Products: pre-order and delivery text.
  - Site settings: news strip, donation goal and the "Now" line.
- Images: WebP, sized to how they display, and lazy-loaded below the first screen.
- Still to build: share previews (Open Graph) and a 404 page. The privacy and terms page is drafted in the demo; Omar approves the final text.
- Demo-only, don't copy: the top bar (colors, Review), "Prototype: no payment is taken" and the "Demo: …" messages.

## Waiting on Omar
- The Google Drive link for the AUBMC document.
- The donation goal and amount raised.
- The 1-minute "Who I am" video.
- A new About photo, since the current one repeats the timeline.
- Where free delivery covers.
- Whether buyers abroad can pay with Whish.
- Confirmation of the $41 bundle price.
- 3 reader quotes.
- The email service.
- Approval of the English lines under the shorts.
- A year for the first timeline moment.

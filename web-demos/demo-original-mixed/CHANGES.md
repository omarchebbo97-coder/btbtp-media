# omarchebbo.com: all changes (Demo + Original Website)

- Demo: https://claude.ai/artifact/F7ffVQaqiRtgy4XD8k9FCi
- Handoff doc: https://claude.ai/artifact/L7iwQCv3ywNhvE7hZEmqp4
- Code: this folder (`web-demos/demo-original-mixed/`, one `index.html` plus `img/`), branch `ccr-72a2b1ad-6o2sbb`. Use it as the reference for layout and behavior, then build it into the Next.js + Sanity site.

## Whole site
- Built phone-first. Nothing scrolls sideways from 320px to 1366px wide. Every button and link is at least 44×44px, text is at least 12px, and form fields use 16px text so iPhones don't zoom in.
- All motion is gentle and stops when the phone has Reduce Motion turned on.
- The header stays at the top while scrolling (sticky), and links to sections leave room for it.
- New news strip above the header: one line, for example "Short: Why are bananas banned on dialysis? · Watch →", which opens the video. It has a close button, and closing is remembered. Later it can announce the AUBMC donation.
- Header: Home · Free guides · Blog · Shop · Gallery · Contact, a "Get your copy" button, and a cart icon with a number badge that bumps when something is added.
- New full-screen phone menu: big links, the current page marked, ↗ on links that open another site, then "Get your copy", "Get the monthly letter →" and the Instagram, TikTok and YouTube icons. The links slide in one after another.
- One buy label everywhere: "Get your copy". The book page keeps "Buy now — $9.99".
- Form errors show as a red message under the field, not as a pop-up.
- The browser Back button returns visitors to the same spot on the homepage.
- Keyboard use: the closed cart and menu are skipped by the Tab key, the focus outline is dark with a gold halo, and Escape closes every pop-up.
- Arabic text uses Noto Sans Arabic (Google Fonts).
- Colors: keep the current palette (slate, gold, cream, ink). The demo's top bar (color dots and "Review") is only for the demo.

## Homepage, top to bottom
- Removed: "2 introductions sold", the test reader reviews, two of the four quote bands, "The journey, in pictures" and the second newsletter form.
1. Hero
   - Small line "Author of *Beyond the Body, Beyond the Pain*", then the heading "I'm Omar Chebbo." and one sentence.
   - Buttons: "Read the first page" (opens the free preview of the introduction) and "Free guides".
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
   - A sticky "Get your copy" bar slides up at the bottom once the buy button has scrolled out of view.
   - The IV-bag drip on the cover was removed.
3. Quote band: "Dialysis doesn't restore life. It postpones death — and in that borrowed time, I learned to live."
4. New section, "The same body, the same life": three before/after drag sliders (dialysis and paragliding, fistula and diving, catheter X-ray and shooting range).
5. New section, "Start here"
   - "Tap the body": a body map with 7 characters from the shorts, each with a count of its items. Tapping one shows the top 3 items, the first marked "Start with this", plus "See all". The characters bob three times, then rest.
   - "Your situation": four buttons (on dialysis, waiting for a transplant, just had a transplant, family or friend), each showing matching posts and videos.
6. New section, "Free guides"
   - Two PDFs that download directly, with no email needed.
   - The cards are in Arabic only: Arabic title, description and page count.
   - New kidney animation on "Get it free": the kidney fills, beats once and lets a drop out. Then a kidney with a check shows "Your PDF is downloading." and one next step: "Next: read the first page of my memoir →".
   - Two "Coming soon" cards with "Tell me when it's out" (email box).
   - The cards swipe sideways on phones and sit 4 across on a computer.
7. Shorts
   - One swipe row of all 12 shorts, replacing the grid with pages.
   - Each shows its Arabic title with an English line under it.
   - Tapping opens a full-screen vertical viewer with swipe or arrows, "Watch on YouTube" and the count "1 of 12". "All shorts →" sits at the end of the row.
8. Blog: topic buttons with counts, compact rows (photo, title, date, read time) and "All posts →". Empty topics are hidden.
9. New section, story timeline (replaces "The journey, in pictures")
   - 7 moments, each with a photo or a character. A line fills as you scroll.
   - Facts: kidney failure at fifteen, dialysis from March 2013 to 2024, and a new kidney from his brother Amine on 13 June 2024.
   - Tapping a photo opens it larger in a pop-up.
10. Quote band: "When you feel limited or stuck, always choose the sky."
11. About
   - Text that no longer repeats the hero.
   - New "▶ Watch my story · 1 min" link.
   - Buttons "Get your copy" and "Invite me to speak".
12. FAQ: 7 questions. New ones:
    - "How do I get the book after paying?"
    - "How do I pay?" (with Whish)
    - "How do I know the money reaches AUBMC?" (with the document link)
    - The answer about inviting Omar to speak now links hello@omarchebbo.com and the Contact page.
13. New section, "Become a donor": "My dad gave part of his liver. My brother gave a kidney.", with "How to register in Lebanon ↗" opening https://www.nodlb.org/.
14. Newsletter: one sign-up form only. After signing up, the form turns into a thank-you line.
15. Footer
    - All links on one row, plus the social icons.
    - New: hello@omarchebbo.com as a tappable email link.
    - The medical notice and copyright.
    - About a third of its old height on a phone.

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
- Still to build: a privacy policy and terms page, share previews (Open Graph) and a 404 page.
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

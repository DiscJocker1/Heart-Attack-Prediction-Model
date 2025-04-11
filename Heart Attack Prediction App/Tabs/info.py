import streamlit as st

def app():
    """This function creates the Heart Health Resources page"""
    st.title("💖 Heart Health Resources, Tips + Info!")
    st.markdown(
        """<p style="font-size:20px;">
                Stay informed, and keep in control of your health! Continue to take proactive steps toward a healthier heart!
            </p>
        """, unsafe_allow_html=True)

    st.info("Let's Taco 'Bout Heart Health: 10 Tips That Are Nacho Average Advice! 😄")

    st.image("Healthy Heart.png")

    st.markdown("""
    - ***********[According to Harvard Health](https://www.health.harvard.edu/healthbeat/10-small-steps-for-better-heart-health)***********
    - **1. Take a 10-minute walk. If you don't exercise at all, a brief walk is a great way to start. If you do, it's a good way to add more exercise to your day.**
    - **2. Give yourself a lift. Lifting a hardcover book or a two-pound weight a few times a day can help tone your arm muscles. When that becomes a breeze, move on to heavier items or join a gym.**
    - **3. Eat one extra fruit or vegetable a day. Fruits and vegetables are inexpensive, taste good, and are good for everything from your brain to your bowels.**
    - **4. Make breakfast count. Start the day with some fruit and a serving of whole grains, like oatmeal, bran flakes, or whole-wheat toast.**
    - **5. Stop drinking your calories. Cutting out just one sugar-sweetened soda or calorie-laden latte can easily save you 100 or more calories a day. Over a year, that can translate into a 10-pound weight loss.**
    - **6. Have a handful of nuts. Walnuts, almonds, peanuts, and other nuts are good for your heart. Try grabbing some instead of chips or cookies when you need a snack, adding them to salads for a healthful and tasty crunch, or using them in place of meat in pasta and other dishes.**
    - **7. Sample the fruits of the sea. Eat fish or other types of seafood instead of red meat once a week. It's good for the heart, the brain, and the waistline.**
    - **8. Breathe deeply. Try breathing slowly and deeply for a few minutes a day. It can help you relax. Slow, deep breathing may also help lower blood pressure.**
    - **9. Wash your hands often. Scrubbing up with soap and water often during the day is a great way to protect your heart and health. The flu, pneumonia, and other infections can be very hard on the heart.**
    - **10. Count your blessings. Taking a moment each day to acknowledge the blessings in your life is one way to start tapping into other positive emotions. These have been linked with better health, longer life, and greater well-being, just as their opposites — chronic anger, worry, and hostility — contribute to high blood pressure and heart disease.**
    """)
    st.header("📚 Trusted Medical Sources")
    st.markdown("""
    - [American Heart Association](https://www.heart.org/)
    - [Circulation Journals](https://www.ahajournals.org/journal/circ)
    - [Heart & Stroke Foundation Canada](https://www.heartandstroke.ca/healthy-living)
    - [Harvard Heart Health](https://www.health.harvard.edu/topics/heart-health)
    - [Mayo Clinic Heart Disease Prevention](https://www.mayoclinic.org/)
    - [World Health Organization - Cardiovascular Diseases](https://www.who.int/)
    """)

    st.header("📰 Latest Research & Studies")
    st.markdown("""
    - [PubMed - Heart Disease Research](https://pubmed.ncbi.nlm.nih.gov/)
    - [JAMA Cardiology](https://jamanetwork.com/journals/jamacardiology)
    - [CVIA Journal Cardiovascular Innovations and Applications](https://cvia-journal.org)
    - [The Lancet - Cardiovascular Medicine](https://www.thelancet.com/cardiovascular)
    """)

    st.info("Stay informed and take proactive steps toward a healthier heart! ❤️")
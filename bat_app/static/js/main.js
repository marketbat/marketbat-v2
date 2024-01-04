function typeOutDailySummary() {
    // Get the text content of the p tag
    const dailySummaryText = document.querySelector('.home__explore-section-daily-summary p').textContent;

    new TypeIt("#daily_summary", {
        speed: 50,
        startDelay: 900,
        waitUntilVisible: true,
    })
        .type("<span> 🔔 It’s December, which means that as of today, you’re officially allowed to hang up Christmas lights without any judgment from your neighbors. We don’t make the rules: A survey of ~4,000 US homeowners found that Dec. 1 was the day most people identified as acceptable to put up Christmas lights.</span>", { speed: 50 })
        .go();
}

import textwrap
for index, place in enumerate(data["places"], start=1):

    place_html = f"""
<div class="place-card">

    <div class="place-number">
        RECOMMEND {index}
    </div>

    <div class="place-name">
        {place['name']}
    </div>

    <div class="country">
        {place['country']}
    </div>

    <div class="reason-title">
        💗 왜 잘 맞을까요?
    </div>

    <div class="reason">
        {place['reason']}
    </div>

    <div class="tip">
        💡 <b>콕콕 TIP</b><br>
        {place['tip']}
    </div>

</div>
"""

    st.markdown(
        textwrap.dedent(place_html),
        unsafe_allow_html=True
    )

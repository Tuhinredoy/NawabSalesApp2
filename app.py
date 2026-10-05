import streamlit as st

st.set_page_config(
    page_title="নবাব - অর্ডার অ্যাপ",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 নবাব")
st.subheader("দোকানের অর্ডার নেওয়ার অ্যাপ")

products = {
    "চিপস": 20,
    "মটর ভাজা": 30,
    "ডাল ভাজা": 25,
    "বাদাম": 40,
    "ঝাল মিক্স": 35
}

st.write("### 📦 পণ্য নির্বাচন করুন")

cart = []

for product, price in products.items():
    qty = st.number_input(
        f"{product} — ৳{price} / প্যাকেট",
        min_value=0,
        step=1,
        key=product
    )

    if qty > 0:
        cart.append({
            "name": product,
            "qty": qty,
            "price": price,
            "total": qty * price
        })

st.divider()

if cart:
    st.subheader("🧾 অর্ডার")

    grand_total = 0

    for item in cart:
        st.write(
            f"**{item['name']}** — "
            f"{item['qty']} প্যাকেট × ৳{item['price']} = "
            f"৳{item['total']}"
        )
        grand_total += item["total"]

    st.divider()
    st.subheader(f"মোট: ৳{grand_total}")

    customer = st.text_input("🏪 দোকানের নাম")
    phone = st.text_input("📞 মোবাইল নম্বর")

    if st.button("✅ অর্ডার নিশ্চিত করুন"):
        st.success("অর্ডার সফলভাবে নেওয়া হয়েছে!")
        st.write(f"দোকান: {customer}")
        st.write(f"মোবাইল: {phone}")
        st.write(f"মোট টাকা: ৳{grand_total}")

else:
    st.info("উপরে থেকে পণ্য ও পরিমাণ নির্বাচন করুন।")

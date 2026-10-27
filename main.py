import streamlit as st

# Cấu hình trang với layout wide
st.set_page_config(
    page_title="Trang Chủ - Cổng Công Cụ",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tùy chỉnh CSS khóa layout trong 1 trang duy nhất, chống tràn khi zoom
st.markdown("""
    <style>
    /* Ẩn footer mặc định của Streamlit để tiết kiệm diện tích */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Khóa cứng chiều cao màn hình, chống cuộn trang */
    html, body, [class*="st-"] {
        max-height: 100vh;
        overflow: hidden !important;
    }

    .main .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
        max-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    /* Tiêu đề chính gọn gàng */
    .main-title {
        font-size: clamp(1.5rem, 2.2vw, 2.2rem);
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 4px;
    }
    
    .subtitle {
        font-size: clamp(0.85rem, 1.2vw, 1rem);
        color: #4B5563;
        text-align: center;
        margin-bottom: 15px;
    }
    
    /* Card tự động co giãn theo khoảng trống còn lại của màn hình */
    .card-container {
        background-color: #F8FAFC;
        padding: 16px;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.2s ease;
    }
    
    .card-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
    }
    
    .card-title {
        font-size: clamp(1rem, 1.4vw, 1.25rem);
        font-weight: 600;
        color: #1E293B;
        margin-bottom: 8px;
    }
    
    .card-desc {
        font-size: clamp(0.8rem, 1.1vw, 0.95rem);
        color: #64748B;
        line-height: 1.4;
        margin-bottom: 0;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- THANH BÊN (SIDEBAR) -----------------
with st.sidebar:
    st.image("https://img.icons8.com/color/96/source-code.png", width=60)
    st.title("Về Tôi")
    st.info(
        "Cổng thông tin cá nhân tổng hợp các ứng dụng "
        "và công cụ tối ưu hóa công việc văn bản."
    )
    st.markdown("---")
    st.markdown("### 📞 Liên hệ")
    st.write("📧 Email: doiemcodon@gmail.com")
    st.write("🌐 Website: Nowebsite")

# ----------------- PHẦN TIÊU ĐỀ CHÍNH -----------------
st.markdown('<div class="main-title">🚀 Chào Mừng Đến Với Cổng Công Cụ</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Khám phá các ứng dụng và tiện ích hỗ trợ công việc của bạn được phát triển hoàn toàn linh hoạt.</div>', unsafe_allow_html=True)

st.markdown("<hr style='margin: 5px 0 15px 0;'>", unsafe_allow_html=True)

# ----------------- KHU VỰC HIỂN THỊ CÁC CÔNG CỤ -----------------
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
        <div class="card-container">
            <div>
                <div class="card-title">🛠️ Ứng dụng ghép giáo án theo thời khoá biểu</div>
                <div class="card-desc">
                    Hỗ trợ ghép giáo án theo từng tiết (với giáo án đã tách ra từng tiết riêng biệt). Đảm bảo đúng định dạng theo quy định EDOC.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='margin-top: 8px;'></div>", unsafe_allow_html=True)
    st.link_button("👉 Truy Cập Công Cụ 1", "https://congcugiaovien.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
        <div class="card-container">
            <div>
                <div class="card-title">📊 Định dạng văn bản theo yêu cầu</div>
                <div class="card-desc">
                    Hỗ trợ các chức năng định dạng văn bản cơ bản, nhanh chóng và chính xác theo chuẩn văn bản hành chính.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='margin-top: 8px;'></div>", unsafe_allow_html=True)
    st.link_button("👉 Truy Cập Công Cụ 2", "https://dinhdangvanban.streamlit.app/", use_container_width=True)

# ----------------- PHẦN CHÂN TRANG (FOOTER) -----------------
st.markdown("<hr style='margin: 15px 0 5px 0;'>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #9CA3AF; font-size: 0.8rem; margin: 0;'>© 2026 Designed & Developed with ❤️ using Streamlit</p>", 
    unsafe_allow_html=True
)

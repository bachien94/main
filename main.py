import streamlit as st

# Cấu hình trang với layout wide để tận dụng tối đa chiều rộng màn hình
st.set_page_config(
    page_title="Trang Chủ - Cổng Công Cụ",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tùy chỉnh CSS Responsive để các card tự co dãn linh hoạt
st.markdown("""
    <style>
    /* Tổng thể */
    .main-title {
        font-size: clamp(2rem, 4vw, 3rem); /* Tự động đổi kích thước chữ theo khung hình */
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: clamp(1rem, 2vw, 1.25rem);
        color: #4B5563;
        text-align: center;
        margin-bottom: 40px;
        padding: 0 15px;
    }
    
    /* Thiết kế Card linh hoạt tự co dãn */
    .card {
        background-color: #F8FAFC;
        padding: 5% 6%;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        height: 100%; /* Giúp các card cùng chiều cao trong một hàng */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.2s, box-shadow 0.2s;
        margin-bottom: 20px;
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .card h2 {
        font-size: clamp(1.2rem, 2vw, 1.6rem);
        color: #1E293B;
        margin-bottom: 15px;
    }
    .card p {
        font-size: clamp(0.9rem, 1.5vw, 1rem);
        color: #64748B;
        line-height: 1.5;
        flex-grow: 1;
    }
    
    /* Responsive cho màn hình nhỏ (Mobile) */
    @media (max-width: 768px) {
        .card {
            padding: 20px;
            margin-bottom: 15px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- THANH BÊN (SIDEBAR) -----------------
with st.sidebar:
    st.image("https://img.icons8.com/color/96/source-code.png", width=70)
    st.title("Về Tôi")
    st.info(
        "Cổng thông tin cá nhân tổng hợp các ứng dụng "
        "và công cụ tối ưu hóa công việc văn bản."
    )
    st.markdown("---")
    st.markdown("### 📞 Liên hệ")
    st.write("📧 Email: bachien94@gmail.com")
    st.write("🌐 Website: No_website")

# ----------------- PHẦN TIÊU ĐỀ CHÍNH -----------------
st.markdown('<div class="main-title">🚀 Chào Mừng Đến Với Cổng Công Cụ</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Khám phá các ứng dụng và tiện ích hỗ trợ công việc của bạn được phát triển hoàn toàn linh hoạt.</div>', unsafe_allow_html=True)

st.markdown("---")

# ----------------- KHU VỰC HIỂN THỊ CÁC CÔNG CỤ -----------------
# st.columns sẽ tự động chuyển từ 2 cột sang 1 cột khi màn hình nhỏ lại (mobile)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="card">
            <div>
                <h2>🛠️ Úng dụng ghép giáo án theo thời khoá biểu</h2>
                <p>
                    Hỗ trợ ghép giáo án theo từng tiết (với giáo án đã tách ra từng tiết riêng biệt). Đảm bảo đúng định dạng theo quy định EDOC
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    # Nút bấm tự động giãn full chiều rộng khung chứa
    st.link_button("👉 Truy Cập Công Cụ 1", "https://congcugiaovien.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
        <div class="card">
            <div>
                <h2>📊 Định dạng văn bản theo yêu cầu</h2>
                <p>
                    Hỗ trợ các chức năng định dạng văn bản cơ bản.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    # Nút bấm tự động giãn full chiều rộng khung chứa
    st.link_button("👉 Truy Cập Công Cụ 2", "https://dinhdangvanban.streamlit.app/", use_container_width=True)

# ----------------- PHẦN CHÂN TRANG (FOOTER) -----------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #9CA3AF; font-size: 0.9rem;'>© 2026 Designed & Developed with ❤️ bachien94@gmail.com</p>", 
    unsafe_allow_html=True
)

def create_chart():
    prompt = f"""
    Your job is to generate chart data based on the given instructions.

    Data input: Tuần này, số liệu bán hàng theo từng ngày được ghi nhận như sau:
    Thứ Hai (Mon): 0 đơn hàng
    Thứ Ba (Tue): 10 đơn hàng
    Thứ Tư (Wed): 5 đơn hàng
    Thứ Năm (Thu): 2 đơn hàng
    Thứ Sáu (Fri): 20 đơn hàng
    Thứ Bảy (Sat): 30 đơn hàng
    Chủ Nhật (Sun): 45 đơn hàng
    Tổng kết: lượng đơn hàng tăng mạnh vào cuối tuần, đặc biệt là Thứ Bảy và Chủ Nhật.

    Instructions:
    - xData: list of strings for the x-axis labels
    - yData: list of integers for the y-axis values

    Reply format:
    {
        "xData": "<list of x-axis labels>",
        "yData": "<list of y-axis values>"
    }

    Directly return the final JSON structure. Do not output anything else."""

    return {
        "type": "line",
        "data": {
            "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "datasets": [
                {
                    "label": "My First dataset",
                    "backgroundColor": "rgb(255, 99, 132)",
                    "borderColor": "rgb(255, 99, 132)",
                    "data": [0, 10, 5, 2, 20, 30, 45],
                }
            ],
        },
    }

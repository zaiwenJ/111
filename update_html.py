import re

with open('/workspace/差距分析预览页面.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. 极简背景 & 去线化 & 阴影重塑
html = html.replace('background-color: #fbfbfd;', 'background-color: #f5f5f7;')
html = html.replace('bg-[#fbfbfd]', 'bg-[#f5f5f7]')
html = html.replace('bg-[#fbfbfd]/50', 'bg-transparent')
html = html.replace('border-r border-gray-200/60', 'border-r-0')
html = html.replace('shadow-[4px_0_24px_rgba(0,0,0,0.02)]', 'shadow-[4px_0_24px_rgba(0,0,0,0.04)]')
html = html.replace('border-b border-gray-100/80 bg-white/50', 'bg-white/40 border-b-0')
html = html.replace('border border-gray-100', 'border-0')
html = html.replace('shadow-[0_2px_8px_rgba(0,0,0,0.04)]', 'shadow-[0_2px_10px_rgba(0,0,0,0.04),_0_10px_30px_rgba(0,0,0,0.02)]')
html = html.replace('hover:shadow-[0_8px_24px_rgba(0,0,0,0.08)]', 'hover:shadow-[0_10px_40px_rgba(0,0,0,0.06),_0_15px_60px_rgba(0,0,0,0.04)]')
html = html.replace('hover:border-indigo-200', '')
html = html.replace('border border-gray-100/80', 'border-0')
html = html.replace('shadow-[0_8px_30px_rgba(0,0,0,0.03)]', 'shadow-[0_10px_40px_rgba(0,0,0,0.04)]')

# 2. 色彩降噪与苹果标准色盘
html = html.replace('selection:bg-indigo-100 selection:text-indigo-900', 'selection:bg-[#0071e3]/20 selection:text-[#0071e3]')
html = html.replace('text-indigo-500', 'text-[#0071e3]')
html = html.replace('text-indigo-600', 'text-[#0071e3]')
html = html.replace('bg-indigo-500', 'bg-[#0071e3]')
html = html.replace('bg-indigo-600', 'bg-[#0071e3]')
html = html.replace('hover:bg-indigo-600', 'hover:bg-[#0071e3]')
html = html.replace('hover:bg-indigo-700', 'hover:bg-[#0071e3]/90')
html = html.replace('group-hover:text-indigo-600', 'group-hover:text-[#0071e3]')
html = html.replace('group-hover:bg-indigo-50', 'group-hover:bg-[#0071e3]/10')
html = html.replace('bg-gray-900 text-white', 'bg-[#1d1d1f] text-white')
html = html.replace('bg-gray-100/80 text-gray-600', 'bg-gray-100/80 text-[#86868b]')
html = html.replace('text-gray-500', 'text-[#86868b]')
html = html.replace('text-gray-400', 'text-[#86868b]')

# 标签色彩降噪
# Card 1
html = html.replace(
    '<span class="inline-block px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-100/80">国家级标志性成果</span>',
    '<span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium bg-gray-100 text-[#1d1d1f]"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>国家级标志性成果</span>'
)
html = html.replace(
    '<span class="flex items-center gap-1 bg-indigo-50/60 text-[#0071e3] px-2 py-1 rounded-full"><i class="ph-fill ph-chalkboard-teacher"></i> 教学</span>',
    '<span class="flex items-center gap-1 bg-gray-100 text-[#1d1d1f] px-2 py-1 rounded-full"><i class="ph-fill ph-chalkboard-teacher text-[#0071e3]"></i> 教学</span>'
)
# Card 2
html = html.replace(
    '<span class="inline-block px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-700 border border-blue-100/80">SCI 一区</span>',
    '<span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium bg-gray-100 text-[#1d1d1f]"><span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>SCI 一区</span>'
)
html = html.replace(
    '<span class="flex items-center gap-1 bg-purple-50/60 text-purple-600 px-2 py-1 rounded-full"><i class="ph-fill ph-flask"></i> 科研</span>',
    '<span class="flex items-center gap-1 bg-gray-100 text-[#1d1d1f] px-2 py-1 rounded-full"><i class="ph-fill ph-flask text-purple-500"></i> 科研</span>'
)
# Card 3
html = html.replace(
    '<span class="inline-block px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-100/80">国家级项目</span>',
    '<span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium bg-gray-100 text-[#1d1d1f]"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>国家级项目</span>'
)
# Card 4
html = html.replace(
    '<span class="inline-block px-2.5 py-1 rounded-full text-[11px] font-semibold bg-gray-100/80 text-gray-700 border border-gray-200/60">校级证明</span>',
    '<span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium bg-gray-100 text-[#1d1d1f]"><span class="w-1.5 h-1.5 rounded-full bg-gray-400"></span>校级证明</span>'
)
html = html.replace(
    '<span class="flex items-center gap-1 bg-orange-50/60 text-orange-600 px-2 py-1 rounded-full"><i class="ph-fill ph-star"></i> 其他综合</span>',
    '<span class="flex items-center gap-1 bg-gray-100 text-[#1d1d1f] px-2 py-1 rounded-full"><i class="ph-fill ph-star text-orange-500"></i> 其他综合</span>'
)

# Matrix Header capacities
html = html.replace('bg-blue-50/80 text-blue-700 px-3.5 py-1.5 rounded-full text-[13px] font-bold border border-blue-100/50', 'bg-[#0071e3]/10 text-[#0071e3] px-3.5 py-1.5 rounded-full text-[13px] font-bold border-0')
html = html.replace('bg-gray-50/80 text-gray-700 px-3.5 py-1.5 rounded-full text-[13px] font-bold border border-gray-200/60', 'bg-gray-100 text-[#1d1d1f] px-3.5 py-1.5 rounded-full text-[13px] font-bold border-0')
html = html.replace('border border-blue-200', 'border-0')

# 3. 苹果原生排版微调
html = html.replace('text-gray-900', 'text-[#1d1d1f]')
html = html.replace('tracking-tight', 'tracking-tighter')
html = html.replace('font-semibold text-[#1d1d1f]', 'font-bold text-[#1d1d1f]')

# 4. 引入弹簧阻尼动效
css_spring = '''
        /* 弹簧阻尼动效 */
        .spring-transition {
            transition: all 0.5s cubic-bezier(0.32, 0.72, 0, 1);
        }
        .dragging {
            opacity: 0.95;
            transform: scale(0.98) rotate(1deg);
            box-shadow: 0 30px 60px rgba(0,0,0,0.12), 0 15px 35px rgba(0,0,0,0.08);
            z-index: 50;
        }
'''
html = re.sub(r'\.dragging\s*\{[^}]+\}', css_spring.strip(), html)
html = html.replace('transition: max-height 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;', 'transition: max-height 0.5s cubic-bezier(0.32, 0.72, 0, 1), opacity 0.4s ease;')

# 给卡片添加 spring-transition
html = html.replace('transition-all duration-300', 'spring-transition')
html = html.replace('hover:-translate-y-0.5', 'hover:-translate-y-1')

# 5. 毛玻璃层级细化
html = html.replace('backdrop-blur-xl', 'backdrop-blur-2xl')
html = html.replace('bg-white/80', 'bg-white/60')
html = html.replace('bg-white/70', 'bg-white/60')
html = html.replace('border-b border-gray-100/50', 'border-b-0')

# Bottom Dock
html = html.replace('bg-white/95 backdrop-blur-3xl rounded-[24px] shadow-[0_20px_40px_-10px_rgba(0,0,0,0.15),0_0_2px_rgba(0,0,0,0.1)] border border-gray-200/80', 'bg-white/70 backdrop-blur-3xl rounded-[24px] shadow-[0_20px_40px_-10px_rgba(0,0,0,0.15),_0_0_20px_rgba(0,0,0,0.05)] border-0')
html = html.replace('border-b border-gray-100/60', 'border-b-0')

# Script updates for Drop UI logic
html = html.replace("counter.classList.replace('bg-gray-100', 'bg-blue-50');", "counter.classList.replace('bg-gray-100', 'bg-[#0071e3]/10');")
html = html.replace("counter.classList.replace('text-gray-700', 'text-blue-700');", "counter.classList.replace('text-[#1d1d1f]', 'text-[#0071e3]');")
html = html.replace("counter.classList.replace('border-gray-200', 'border-blue-200');", "")

# 修正部分没替换好的细节
html = html.replace('text-gray-800', 'text-[#1d1d1f]')
html = html.replace('bg-gray-900', 'bg-[#1d1d1f]')

with open('/workspace/差距分析预览页面.html', 'w', encoding='utf-8') as f:
    f.write(html)

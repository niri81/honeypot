<?php
// Dynamic year for the footer
$current_year = date("Y");

// Dynamic greeting based on time of day
$hour = (int) date("G");
if ($hour < 12) {
    $greeting = "Good morning";
} elseif ($hour < 18) {
    $greeting = "Good afternoon";
} else {
    $greeting = "Good evening";
}

// Sample dynamic features data
$features = [
    [
        "title" => "Lightning Fast",
        "description" =>
            "Optimized for speed and performance to ensure your users never wait.",
        "icon" => "⚡",
    ],
    [
        "title" => "Fully Responsive",
        "description" =>
            "Looks stunning on mobile phones, tablets, and desktop screens alike.",
        "icon" => "📱",
    ],
    [
        "title" => "Secure & Reliable",
        "description" =>
            "Built following best practices to keep your data safe and sound.",
        "icon" => "🔒",
    ],
];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Our Platform</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased flex flex-col min-h-screen">

    <header class="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <span class="text-2xl font-black text-indigo-600">BrandLogo</span>
            </div>
            <nav class="hidden md:flex space-x-8 text-sm font-medium text-slate-600">
                <a href="#" class="hover:text-indigo-600 transition">Home</a>
                <a href="#features" class="hover:text-indigo-600 transition">Features</a>
                <a href="#about" class="hover:text-indigo-600 transition">About</a>
                <a href="#contact" class="hover:text-indigo-600 transition">Contact</a>
            </nav>
            <div>
                <a href="#contact" class="bg-indigo-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-indigo-700 transition shadow-sm">Get Started</a>
            </div>
        </div>
    </header>

    <main class="flex-grow">
        <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 lg:py-32 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div class="space-y-6 text-center lg:text-left">
                <span class="inline-block bg-indigo-50 text-indigo-700 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider">
                    <?php echo $greeting; ?>! Welcome visitor
                </span>
                <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-slate-900 tracking-tight">
                    Build something <span class="text-indigo-600">extraordinary</span> today.
                </h1>
                <p class="text-lg text-slate-600 max-w-xl mx-auto lg:mx-0">
                    A powerful, clean, and modern PHP starter template designed to help you launch your next web project in minutes instead of hours.
                </p>
                <div class="flex flex-col sm:flex-row justify-center lg:justify-start gap-4">
                    <a href="#features" class="bg-indigo-600 text-white font-medium px-6 py-3 rounded-xl hover:bg-indigo-700 transition shadow-md text-center">Explore Features</a>
                    <a href="#contact" class="bg-white text-slate-700 border border-slate-300 font-medium px-6 py-3 rounded-xl hover:bg-slate-50 transition text-center">Contact Us</a>
                </div>
            </div>
            <div class="bg-indigo-100 border border-indigo-200 rounded-3xl p-8 flex items-center justify-center shadow-inner h-80 lg:h-96">
                <div class="text-center space-y-2">
                    <span class="text-6xl">🚀</span>
                    <p class="text-indigo-900 font-semibold text-lg">Your Hero Graphic / Image Area</p>
                </div>
            </div>
        </section>

        <section id="features" class="bg-white py-20 border-t border-slate-200">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center max-w-2xl mx-auto mb-16">
                    <h2 class="text-3xl font-bold text-slate-900">Core Features</h2>
                    <p class="text-slate-600 mt-2">Everything you need to succeed online, built right into the core.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <?php foreach ($features as $feature): ?>
                        <div class="bg-slate-50 border border-slate-200 rounded-2xl p-8 transition hover:shadow-lg">
                            <div class="text-4xl mb-4"><?php echo $feature[
                                "icon"
                            ]; ?></div>
                            <h3 class="text-xl font-bold text-slate-900 mb-2"><?php echo htmlspecialchars(
                                $feature["title"],
                            ); ?></h3>
                            <p class="text-slate-600 text-sm leading-relaxed"><?php echo htmlspecialchars(
                                $feature["description"],
                            ); ?></p>
                        </div>
                    <?php endforeach; ?>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6">
            <p class="text-sm">&copy; <?php echo $current_year; ?> BrandLogo. All rights reserved.</p>
            <div class="flex space-x-6 text-sm">
                <a href="#" class="hover:text-white transition">Privacy Policy</a>
                <a href="#" class="hover:text-white transition">Terms of Service</a>
                <a href="#" class="hover:text-white transition">Support</a>
            </div>
        </div>
    </footer>
</body>
</html>

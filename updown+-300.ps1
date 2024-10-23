# Добавляем функцию для симуляции нажатия мыши и клавиш
Add-Type @"
using System;
using System.Runtime.InteropServices;

public class MouseSimulator {
    [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
    public static extern void mouse_event(uint dwFlags, uint dx, uint dy, uint cButtons, uint dwExtraInfo);

    [DllImport("user32.dll")]
    public static extern void keybd_event(byte bVk, byte bScan, uint dwFlags, UIntPtr dwExtraInfo);

    [DllImport("user32.dll")]
    public static extern short GetAsyncKeyState(int vKey);

    [DllImport("user32.dll")]
    public static extern bool SetCursorPos(int X, int Y);

    public const int MOUSEEVENTF_LEFTDOWN = 0x02;
    public const int MOUSEEVENTF_LEFTUP = 0x04;
    public const int MOUSEEVENTF_RIGHTDOWN = 0x08;
    public const int MOUSEEVENTF_RIGHTUP = 0x10;

    public const byte VK_1 = 0x31; // Код виртуальной клавиши для "1"
    public const uint KEYEVENTF_KEYUP = 0x0002; // Флаг для отпускания клавиши

    // Метод для нажатия левой кнопки мыши
    public static void LeftDown() {
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
    }

    // Метод для нажатия клавиши "1"
    public static void PressKey1() {
        keybd_event(VK_1, 0, 0, UIntPtr.Zero); // Нажимаем клавишу
    }

    // Метод для отпускания клавиши "1"
    public static void ReleaseKey1() {
        keybd_event(VK_1, 0, KEYEVENTF_KEYUP, UIntPtr.Zero); // Отпускаем клавишу
    }

    // Метод для отпускания левой кнопки мыши
    public static void LeftUp() {
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
    }

    // Метод для нажатия правой кнопки мыши
    public static void RightDown() {
        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0);
    }

    // Метод для отпускания правой кнопки мыши
    public static void RightUp() {
        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0);
    }
}
"@

# Метод для проверки нажатия клавиши "1"
function IsKey1Pressed {
    return ([MouseSimulator]::GetAsyncKeyState([MouseSimulator]::VK_1) -band 0x8000) -ne 0
}

# Получаем текущие координаты курсора
function GetCursorPos {
    $pos = New-Object System.Drawing.Point
    [System.Windows.Forms.Cursor]::Position
}

# Устанавливаем интервал между кликами (в миллисекундах)
$interval = 3  # Интервал между кликами

# Инициализируем переменные
$clickCount = 0  # Счётчик нажатий
$moveUp = $true  # Начальное направление перемещения

# Начинаем цикл автокликов
while ($true) {
    if (IsKey1Pressed) {
        break;  # Выход из цикла, если клавиша "1" нажата
    }

    # Получаем текущие координаты курсора
    $currentPos = GetCursorPos

    # Нажимаем левую кнопку мыши
    [MouseSimulator]::LeftDown()
    # Отпускаем левую кнопку мыши
    [MouseSimulator]::LeftUp()

    # Увеличиваем счётчик нажатий
    $clickCount++

    # Проверяем, достиг ли счётчик 1000
    if ($clickCount -ge 1000) {
        if ($moveUp) {
            [MouseSimulator]::SetCursorPos($currentPos.X, $currentPos.Y - 300)  # Перемещаем курсор вверх
        } else {
            [MouseSimulator]::SetCursorPos($currentPos.X, $currentPos.Y + 300)  # Перемещаем курсор вниз
        }
        
        # Переключаем направление и сбрасываем счётчик
        $moveUp = -not $moveUp
        $clickCount = 0  # Сбрасываем счётчик
    }

    # Ожидаем заданное количество времени
    Start-Sleep -Milliseconds $interval
}

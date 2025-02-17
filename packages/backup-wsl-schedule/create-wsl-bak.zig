const std = @import("std");
const os = std.os;

pub fn main() !void {
    const command = "powershell.exe -Command \"wsl --export Ubuntu-24.04 C:\\wsl-backups\\ubuntu24-bak.tar\""; // Replace with your actual command

    // Execute the command in a separate process
    var process = try std.process.spawn(command, .{}) catch |err| {
        std.debug.print("Error spawning process: {}\n", .{err});
        return err;
    };

    // Wait for the process to finish
    const exit_code = try process.wait();

    if (exit_code == 0) {
        std.debug.print("Command executed successfully.\n", .{});
    } else {
        std.debug.print("Command failed with exit code: {}\n", .{exit_code});
    }
}

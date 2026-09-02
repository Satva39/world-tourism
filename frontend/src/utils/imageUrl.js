const API_ORIGIN = "https://world-tourism.onrender.com";

export function getImageUrl(image) {
    if (!image) return "";

    const imageUrl =
        typeof image === "string"
            ? image
            : image.image_url ||
            image.url ||
            image.image ||
            image.cover_image ||
            "";

    if (!imageUrl) return "";

    if (
        imageUrl.startsWith("http://") ||
        imageUrl.startsWith("https://")
    ) {
        return imageUrl;
    }

    return `${API_ORIGIN}${imageUrl.startsWith("/") ? "" : "/"}${imageUrl}`;
}
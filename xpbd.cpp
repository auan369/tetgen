#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>

// Define SoftBody class and physics logic
// ...

int main() {
    // Create a window for rendering using SFML
    sf::RenderWindow window(sf::VideoMode(800, 600), "Soft Body Simulation");

    // Initialize your SoftBody object
    SoftBody softBody(/* parameters */);



    //----Math on Vector Arrays-------------------------------------
    void vecSetZero(float* a, int anr) {
    anr *= 3;
    a[anr++] = 0.0f;
    a[anr++] = 0.0f;
    a[anr]   = 0.0f;
    }

    void vecScale(float* a, int anr, float scale) {
        anr *= 3;
        a[anr++] *= scale;
        a[anr++] *= scale;
        a[anr]   *= scale;
    }

    void vecCopy(float* a, int anr, const float* b, int bnr) {
        anr *= 3; bnr *= 3;
        a[anr++] = b[bnr++]; 
        a[anr++] = b[bnr++]; 
        a[anr]   = b[bnr];
    }

    void vecAdd(float* a, int anr, const float* b, int bnr, float scale = 1.0f) {
        anr *= 3; bnr *= 3;
        a[anr++] += b[bnr++] * scale; 
        a[anr++] += b[bnr++] * scale; 
        a[anr]   += b[bnr] * scale;
    }

    void vecSetDiff(float* dst, int dnr, const float* a, int anr, const float* b, int bnr, float scale = 1.0f) {
        dnr *= 3; anr *= 3; bnr *= 3;
        dst[dnr++] = (a[anr++] - b[bnr++]) * scale;
        dst[dnr++] = (a[anr++] - b[bnr++]) * scale;
        dst[dnr]   = (a[anr] - b[bnr]) * scale;
    }

    float vecLengthSquared(const float* a, int anr) {
        anr *= 3;
        float a0 = a[anr], a1 = a[anr + 1], a2 = a[anr + 2];
        return a0 * a0 + a1 * a1 + a2 * a2;
    }

    float vecDistSquared(const float* a, int anr, const float* b, int bnr) {
        anr *= 3; bnr *= 3;
        float a0 = a[anr] - b[bnr], a1 = a[anr + 1] - b[bnr + 1], a2 = a[anr + 2] - b[bnr + 2];
        return a0 * a0 + a1 * a1 + a2 * a2;
    }   

    float vecDot(const float* a, int anr, const float* b, int bnr) {
        anr *= 3; bnr *= 3;
        return a[anr] * b[bnr] + a[anr + 1] * b[bnr + 1] + a[anr + 2] * b[bnr + 2];
    }

    void vecSetCross(float* a, int anr, const float* b, int bnr, const float* c, int cnr) {
        anr *= 3; bnr *= 3; cnr *= 3;
        a[anr++] = b[bnr + 1] * c[cnr + 2] - b[bnr + 2] * c[cnr + 1];
        a[anr++] = b[bnr + 2] * c[cnr + 0] - b[bnr + 0] * c[cnr + 2];
        a[anr]   = b[bnr + 0] * c[cnr + 1] - b[bnr + 1] * c[cnr + 0];
    }
    //---------------------------------------------------------------


    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();

            // Handle other events (e.g., mouse clicks) here
        }

        // Update physics simulation
        softBody.updatePhysics(/* delta time */);

        // Clear the window
        window.clear();

        // Render the soft body and other objects
        // ...

        // Display the frame
        window.display();
    }

    return 0;
}
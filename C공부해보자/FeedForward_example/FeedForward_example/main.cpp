// Feedforward ±¸Çö
#include <iostream>

#define MAX2(a, b) (a) > (b) ? (a) : (b)
class Neuron
{
public:
	double w_;  // weight of one input
	double b_;  // bias

	// activation function
	double getAct(const double& x)
	{
		// for linear of identity activation functions
		//return x;

		//for ReLU
		return MAX2(0.0, x);
	}
	double feedForward(const double& input)
	{
		// output y = f(\sigma)
		// \sigma = w_ * input x + b
		// for multiple inputs,
		// \sigma = w0_ * x0_ + w1_ * x1_ + .... + b

		const double sigma = w_ * input + b_;

		return getAct(sigma);
	}
};

void main()
{	
	Neuron my_neuron;
	my_neuron.w_ = 2.0;
	my_neuron.b_ = 1.0;
	std::cout << "Input = 1.0" << my_neuron.feedForward(1.0) << std::endl;
	std::cout << "Input = 2.0" << my_neuron.feedForward(2.0) << std::endl;
	std::cout << "Input = 3.0" << my_neuron.feedForward(3.0) << std::endl;
}
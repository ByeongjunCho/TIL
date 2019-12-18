// Back-propagation ±¸Çö
#include <iostream>

#define MAX2(a, b) (a) > (b) ? (a) : (b)
class Neuron
{
public:
	Neuron() {
		w_ = 2.0; // weight of one input
		b_ = 1.0; // bias
	}
	Neuron(const double& w_input, const double& b_input)
		:w_(w_input), b_(b_input)
	{}

	double w_;  // weight of one input
	double b_;  // bias

	double input_, output_;  // save for back-prop
	// activation function
	double getAct(const double& x)
	{
		// for linear of identity activation functions
		//return x;

		//for ReLU
		return MAX2(0.0, x);
	}

	void propBackward(const double& target)
	{
		const double alpha = 0.1; // learning rate
		const double grad = (output_ - target) * getActGrad(output_);

		w_ -= alpha * grad * input_;
		b_ -= alpha * grad * 1.0;
	}

	double getActGrad(const double& x)
	{
		// for linear of identity activation functions
		
		return 1.0;

		//for ReLU
		if (x > 0)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
	double feedForward(const double& input)
	{
		input_ = input;
		// output y = f(\sigma)
		// \sigma = w_ * input x + b
		// for multiple inputs,
		// \sigma = w0_ * x0_ + w1_ * x1_ + .... + b

		const double sigma = w_ * input + b_;
		output_ = getAct(sigma);
		return output_;
	}

	void feedForwardAndPrint(const double& input)
	{
		printf("%f %f \n", input, feedForward(input));
	}
};

void main()
{
	Neuron my_neuron(2.0, 1.0);
	for (int i = 0; i < 100; i++)
	{
		std::cout << "Training" << i << std::endl;
		my_neuron.feedForwardAndPrint(1.0);
		my_neuron.propBackward(4.0);
		std::cout << "w = " << my_neuron.w_ << "b = " << my_neuron.b_ << std::endl;
	}
	
	
}
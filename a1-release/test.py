import _pickle as cpickle
from language_model import *
model = cpickle.load(open("model.pk", "rb"))
# model.predict_next_word("this", "is", "a")
b = model.predict_next_word("for", "the", "united")
words = ["this", "was", "a"]
#
for i in range(300):
    try:
        word = model.my_predict_next_word(words[-3], words[-2], words[-1])
        words.append(word)
    except:
        print("error!!!")
        break
# model.display_nearest_words("new")
sentence = ""
for i in words:
    sentence += i
    sentence += " "
print(sentence)
# model.tsne_plot()
# a = pickle.load(open('data.pk', 'rb'))

# obj = pickle.load(open("partially_trained.pk", 'rb'))
# print(obj['word_embedding_weights'].shape)
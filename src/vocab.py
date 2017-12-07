from collections import defaultdict


class Vocab:
    def __init__(self, word_path, pos_path, label_path, action_path):
        words = open(word_path, 'r').read().strip().split('\n')
        pos = open(pos_path, 'r').read().strip().split('\n')
        labels = open(label_path, 'r').read().strip().split('\n')
        actions = open(action_path, 'r').read().strip().split('\n')

        # first read into counts
        self.word2id_dict = {}
        self.pos2id_dict = {}
        self.label2id_dict = {}
        self.action2id_dict = {}
        self.id2word_dict = {}
        self.id2pos_dict = {}
        self.id2label_dict = {}
        self.id2action_dict = {}
        for line in words:
            items = line.strip().split(' ')
            word = items[0]
            id = items[1]
            self.word2id_dict[word] = id
            self.id2word_dict[id] = word
        for line in pos:
            items = line.strip().split(' ')
            p = items[0]
            id = items[1]
            self.pos2id_dict[p] = id
            self.id2pos_dict[id] = p
        for line in labels:
            items = line.strip().split(' ')
            label = items[0]
            id = items[1]
            self.label2id_dict[label] = id
            self.id2label_dict[id] = label
        for line in actions:
            items = line.strip().split(' ')
            action = items[0]
            id = items[1]
            self.action2id_dict[action] = id
            self.id2action_dict[id] = action


    def tagid2tag_str(self, id):
        return self.id2action_dict[id]

    def tag2id(self, tag):
        return self.action2id_dict[tag]

    def pos2id(self, tag):
        return self.pos2id_dict[tag]

    def label2id(self, tag):
        return self.label2id[tag]

    def word2id(self, word):
        return self.word2id_dict[word] if word in self.word2id_dict else self.word2id_dict['<unk>']

    def num_words(self):
        return len(self.word2id_dict)

    def num_pos_feats(self):
        return len(self.pos2id_dict)

    def num_label_feats(self):
        return len(self.label2id_dict)

    def num_tags(self):
        return len(self.action2id_dict)
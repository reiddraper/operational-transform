var optransform = {
    insertInsert: function insertInsert(a, b){
                if (a.index == b.index && a.item == b.item){
                    return null;
                }

                if (a.index < b.index){
                    return a;
                }
                else {
                    return {
                        type:  'insert',
                        index: a.index + 1,
                        item:  a.item
                        };
                }
            },

    deleteInsert: function deleteInsert(a, b){
                if (a.index < b.index){
                    return a;
                }
                else {
                    return {
                    type:  'delete',
                    index: a.index + 1
                    };
                }
            },

    insertDelete: function insertDelete(a, b){
                if (a.index < b.index){
                    return a;
                }
                else {
                    return {
                    type:  'insert',
                    index: a.index - 1,
                    item:  a.item
                    };
                }
            },

    deleteDelete: function deleteDelete(a, b){
                if (a.index == b.index){
                    return null;
                }

                if (a.index > b.index){
                    return {
                        type:  'delete',
                        index: a.index - 1
                    };
                }
                else {
                    return a;
                }
            },

    transform: function transform(a, b){
                // insert insert
                if ((a.type == 'insert') && (b.type == 'insert')){
                    return optransform.insertInsert(a, b);
                    }

                // delete insert
                if ((a.type == 'delete') && (b.type == 'insert')){
                    return optransform.deleteInsert(a, b);
                    } 

                // insert delete
                if ((a.type == 'insert') && (b.type == 'delete')){
                    return optransform.insertDelete(a, b);
                    } 

                // delete delete
                if ((a.type == 'delete') && (b.type == 'delete')){
                    return optransform.deleteDelete(a, b);
                    }
            },

    transformMany: function transformMany(a, l, i){
                i = i || 0;

                if (l.length === 0){
                    return a;
                }

                if (i == l.length - 1){
                    a = optransform.transform(a, l[i]);
                    if (a === null){
                        return null;
                    }
                    else {
                        return a;
                    }
                }
                else {
                    var current = l[i];
                    a = optransform.transform(a, current);
                    if (a === null){
                        return null;
                    }
                    return optransform.transformMany(a, l, i + 1);
                }
            },

    transformManyToMany: function transformManyToMany(a, b){
                var transformed;
                if (b.length > 0){
                    transformed = [];
                    var op;
                    for (i = 0; i < a.length; i++){
                        op = a[i];
                        op = optransform.transformMany(op, b.slice(i));
                        if (op){
                            transformed.push(op);
                        }
                    }
                }
                else{
                    transformed = a;
                }

                return transformed;
    },

    render: function render(operations, state){
                state = state || [];
                for (var i = 0; i < operations.length; i++){
                    var op = operations[i];
                    if (op.type == 'insert'){
                        state.splice(op.index, 0, op.item);
                    }
                    else {
                        state.splice(op.index, 1);
                    }
                }
                return state;
            }
};

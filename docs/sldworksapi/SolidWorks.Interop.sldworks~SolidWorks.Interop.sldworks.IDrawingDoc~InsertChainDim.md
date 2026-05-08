# InsertChainDim Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertChainDim`

Obsolete. Superseded by IModelDocExtension::InsertChainDimensions.
Obsolete. Superseded by [IModelDocExtension::InsertChainDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertChainDimensions.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertChainDim() 
```

```

Dim instance As IDrawingDoc
 
instance.InsertChainDim()
```

```

void InsertChainDim()
```

```

void InsertChainDim(); 
```

Remarks

To insert a chain dimension into a drawing:

1. Call this method.
2. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the first entity. This entity is used to create all dimensions in the chain.
3. Call IModelDocExtension::SelectByID2 to select the second entity to dimension with respect to the first.
4. Call [IModelDoc2::AddDimension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.md).
5. Call IModelDocExtension::SelectByID2 to select the next entity to dimension with respect to the first.
6. Call IModelDoc2::AddDimension2 to add the dimension to the chain.
7. Repeat steps 5 and 6 to add more dimensions to the chain.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

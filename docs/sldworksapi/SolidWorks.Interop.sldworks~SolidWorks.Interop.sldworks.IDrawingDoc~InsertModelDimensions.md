# InsertModelDimensions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelDimensions`

Inserts model dimensions into the selected drawing view according to the option specified.
Inserts model dimensions into the selected drawing view according to the option specified.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertModelDimensions( _
   ByVal Option As System.Integer _
) 
```

```

Dim instance As IDrawingDoc
Dim Option As System.Integer
 
instance.InsertModelDimensions(Option)
```

```

void InsertModelDimensions( 
   System.int Option
)
```

```

void InsertModelDimensions( 
   System.int Option
) 
```

#### Parameters

*Option*
:   - 0 - All dimensions in the view
    - 1 - All dimensions of the currently selected component (for assembly drawings)
    - 2 - All dimensions of the currently selected feature
    - 3 - All dimensions of the assembly

Remarks

The **Insert Model Items** dialog is not displayed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.md)  
[IDrawingDoc::DragModelDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DragModelDimension.md)  
[IDrawingDoc::HideShowDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDimensions.md)  
[IDrawingDoc::InsertModelAnnotations3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.md)  
[IDrawingDoc::InsertRefDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.md)

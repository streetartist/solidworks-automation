# InsertViewAsBlock Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertViewAsBlock`

Creates a sketch block from this view and aligns the specified manipulator point with the specified sketch block position on the drawing sheet.
Creates a sketch block from this view and aligns the specified manipulator point with the specified sketch block position on the drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertViewAsBlock( _
   ByVal InsertionPoint As MathPoint, _
   ByVal Position As MathPoint _
) As System.Boolean
```

```

Dim instance As IView
Dim InsertionPoint As MathPoint
Dim Position As MathPoint
Dim value As System.Boolean
 
value = instance.InsertViewAsBlock(InsertionPoint, Position)
```

```

System.bool InsertViewAsBlock( 
   MathPoint InsertionPoint,
   MathPoint Position
)
```

```

System.bool InsertViewAsBlock( 
   MathPoint^ InsertionPoint,
   MathPoint^ Position
) 
```

#### Parameters

*InsertionPoint*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) in this view where the manipulator of the new [sketch block](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) is located

*Position*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) on the drawing sheet where the new sketch block manipulator is positioned

#### Return Value

True if the view is successfully converted to a sketch block, false if not

Example

[Convert Drawing Views to Sketch Blocks (VBA)](Convert_Drawing_Views_to_Sketches_Example_VB.htm)  
[Convert Drawing Views to Sketch Blocks (VB.NET)](Convert_Drawing_Views_to_Sketches_Example_VBNET.htm)  
[Convert Drawing Views to Sketch Blocks (C#)](Convert_Drawing_Views_to_Sketches_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::ReplaceViewWithBlock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithBlock.md)  
[IView::ReplaceViewWithSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithSketch.md)

# ReplaceViewWithBlock Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithBlock`

Converts this view into a sketch block with the specified manipulator location.
Converts this view into a sketch block with the specified manipulator location.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplaceViewWithBlock( _
   ByVal InsertionPoint As MathPoint _
) As System.Boolean
```

```

Dim instance As IView
Dim InsertionPoint As MathPoint
Dim value As System.Boolean
 
value = instance.ReplaceViewWithBlock(InsertionPoint)
```

```

System.bool ReplaceViewWithBlock( 
   MathPoint InsertionPoint
)
```

```

System.bool ReplaceViewWithBlock( 
   MathPoint^ InsertionPoint
) 
```

#### Parameters

*InsertionPoint*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) in this view where the manipulator of the new [sketch block](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) is located

#### Return Value

True if the view is successfully replaced with a sketch block, false if not

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
[IView::InsertViewAsBlock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertViewAsBlock.md)  
[IView::ReplaceViewWithSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithSketch.md)

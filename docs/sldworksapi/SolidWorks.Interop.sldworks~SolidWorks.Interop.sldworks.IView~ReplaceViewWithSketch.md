# ReplaceViewWithSketch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithSketch`

Converts this view into a sketch.
Converts this view into a sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplaceViewWithSketch() As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
value = instance.ReplaceViewWithSketch()
```

```

System.bool ReplaceViewWithSketch()
```

```

System.bool ReplaceViewWithSketch(); 
```

#### Return Value

True if the view is successfully replaced with a [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md), false if not

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
[IView::InsertViewAsBlock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertViewAsBlock.md)

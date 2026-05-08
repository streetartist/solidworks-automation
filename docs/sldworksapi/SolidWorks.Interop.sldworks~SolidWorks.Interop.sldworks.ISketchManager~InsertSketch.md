# InsertSketch Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch`

Inserts a new sketch in the current part or assembly document.
Inserts a new sketch in the current part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSketch( _
   ByVal UpdateEditRebuild As System.Boolean _
) 
```

```

Dim instance As ISketchManager
Dim UpdateEditRebuild As System.Boolean
 
instance.InsertSketch(UpdateEditRebuild)
```

```

void InsertSketch( 
   System.bool UpdateEditRebuild
)
```

```

void InsertSketch( 
   System.bool UpdateEditRebuild
) 
```

#### Parameters

*UpdateEditRebuild*
:   True to rebuild the part with any changes made to the sketch and exit sketch mode, false to not

Remarks

This method does not support drawing documents.

Example

[Insert Sheet Metal Edge Flange (VBA)](Insert_Sheet_Metal_Edge_Flange_Example_VB.htm)  
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)  
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)  
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)  
[Insert and Resize Sketch Slot (C#)](Insert_and_Resize_Sketch_Slot_Example_CSharp.htm)  
[Insert and Resize Sketch Slot (VB.NET)](Insert_and_Resize_Sketch_Slot_Example_VBNET.htm)  
[Insert and Resize Sketch Slot (VBA)](Insert_and_Resize_Sketch_Slot_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)

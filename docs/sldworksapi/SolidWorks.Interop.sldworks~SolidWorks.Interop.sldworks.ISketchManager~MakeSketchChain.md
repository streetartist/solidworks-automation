# MakeSketchChain Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchChain`

Creates a sketch path using the selected entities.
Creates a sketch path using the selected entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeSketchChain() As System.Boolean
```

```

Dim instance As ISketchManager
Dim value As System.Boolean
 
value = instance.MakeSketchChain()
```

```

System.bool MakeSketchChain()
```

```

System.bool MakeSketchChain(); 
```

#### Return Value

True if the a sketch path is created, false if not

Remarks

This method is not valid:

- unless a sketch is in edit mode.
- for 3D sketches.

Example

[Create Sketch Path (VBA)](Create_Sketch_Path_Example_VB.htm)  
[Create Sketch Path (VB.NET)](Create_Sketch_Path_Example_VBNET.htm)  
[Create Sketch Path (C#)](Create_Sketch_Path_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)

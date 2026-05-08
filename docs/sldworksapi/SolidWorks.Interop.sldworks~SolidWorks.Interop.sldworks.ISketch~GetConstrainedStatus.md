# GetConstrainedStatus Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetConstrainedStatus`

Gets the current constrained status of the sketch.
Gets the current constrained status of the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConstrainedStatus() As System.Integer
```

```

Dim instance As ISketch
Dim value As System.Integer
 
value = instance.GetConstrainedStatus()
```

```

System.int GetConstrainedStatus()
```

```

System.int GetConstrainedStatus(); 
```

#### Return Value

Constrained status as defined in [swConstrainedStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstrainedStatus_e.html)

Example

[Get Sketch Constraints (VBA)](Get_Sketch_Constraints_Example_VB.htm)  
[Autodimension All Sketches (C#)](Autodimension_All_Sketches_Example_CSharp.htm)  
[Autodimension All Sketches (VB.NET)](Autodimension_All_Sketches_Example_VBNET.htm)  
[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::ConstrainAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ConstrainAll.md)

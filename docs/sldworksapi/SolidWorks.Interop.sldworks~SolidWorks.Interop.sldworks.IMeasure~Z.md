# Z Property (IMeasure)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Z`

Gets the z coordinate of the selected point in model space.
Gets the z coordinate of the selected point in model space.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Z As System.Double
```

```

Dim instance As IMeasure
Dim value As System.Double
 
value = instance.Z
```

```

System.double Z {get;}
```

```

property System.double Z {
   System.double get();
}
```

#### Property Value

z coordinate of the selected point in model space or -1 if this property is invalid for the selected entity

Example

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)  
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)  
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.md)  
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.md)  
[IMeasure::X Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~X.md)  
[IMeasure::Y Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Y.md)

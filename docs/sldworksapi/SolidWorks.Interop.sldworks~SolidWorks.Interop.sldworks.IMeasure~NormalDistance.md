# NormalDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~NormalDistance`

Gets the normal distance (normal to the selected plane) between the selected entity and plane.
Gets the normal distance (normal to the selected plane) between the selected entity and plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property NormalDistance As System.Double
```

```

Dim instance As IMeasure
Dim value As System.Double
 
value = instance.NormalDistance
```

```

System.double NormalDistance {get;}
```

```

property System.double NormalDistance {
   System.double get();
}
```

#### Property Value

Normal distance or -1 if this property is invalid for the selected entities

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
[IMeasure::Normal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Normal.md)

# Projection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Projection`

Gets the projected distance between the two selected entities.
Gets the projected distance between the two selected entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Projection As System.Double
```

```

Dim instance As IMeasure
Dim value As System.Double
 
value = instance.Projection
```

```

System.double Projection {get;}
```

```

property System.double Projection {
   System.double get();
}
```

#### Property Value

Projected distance between the two selected entities or -1 if this property is invalid for the selected entities

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
[IMeasure::ProjectionOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ProjectionOption.md)  
[IMeasure::SetProjectionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~SetProjectionEntity.md)

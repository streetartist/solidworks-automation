# IsPerpendicular Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsPerpendicular`

Gets whether the two selected entities are perpendicular.
Gets whether the two selected entities are perpendicular.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsPerpendicular As System.Boolean
```

```

Dim instance As IMeasure
Dim value As System.Boolean
 
value = instance.IsPerpendicular
```

```

System.bool IsPerpendicular {get;}
```

```

property System.bool IsPerpendicular {
   System.bool get();
}
```

#### Property Value

True if the two selected entities are perpendicular, false if not

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
[IMeasure::IsConcentricSpheres Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsConcentricSpheres.md)  
[IMeasure::IsIntersect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsIntersect.md)  
[IMeasure::IsParallel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsParallel.md)

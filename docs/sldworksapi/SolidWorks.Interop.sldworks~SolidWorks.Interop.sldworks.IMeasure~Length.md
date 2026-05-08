# Length Property (IMeasure)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Length`

Gets the length of the selected entity.
Gets the length of the selected entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Length As System.Double
```

```

Dim instance As IMeasure
Dim value As System.Double
 
value = instance.Length
```

```

System.double Length {get;}
```

```

property System.double Length {
   System.double get();
}
```

#### Property Value

Length of the selected entity or -1 if this property is invalid for the selected entity

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
[IMeasure::LengthDecimalPlaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~LengthDecimalPlaces.md)  
[IMeasure::TotalLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~TotalLength.md)

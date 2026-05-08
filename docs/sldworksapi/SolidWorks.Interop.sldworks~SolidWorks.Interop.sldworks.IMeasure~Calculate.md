# Calculate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Calculate`

Measures the selected or specified entities.
Measures the selected or specified entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Calculate( _
   ByVal Entities As System.Object _
) As System.Boolean
```

```

Dim instance As IMeasure
Dim Entities As System.Object
Dim value As System.Boolean
 
value = instance.Calculate(Entities)
```

```

System.bool Calculate( 
   System.object Entities
)
```

```

System.bool Calculate( 
   System.Object^ Entities
) 
```

#### Parameters

*Entities*
:   Array of entities to measure; if NULL, then this method measures the selected entities

#### Return Value

True if the specified or selected entities are valid types and combination , false if not

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

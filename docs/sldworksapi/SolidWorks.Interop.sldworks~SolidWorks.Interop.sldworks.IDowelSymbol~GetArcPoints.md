# GetArcPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetArcPoints`

Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based.
Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArcPoints() As System.Object
```

```

Dim instance As IDowelSymbol
Dim value As System.Object
 
value = instance.GetArcPoints()
```

```

System.object GetArcPoints()
```

```

System.Object^ GetArcPoints(); 
```

#### Return Value

Array of start, mid, and end point x and y coordinates

Remarks

If the arc segment is a complete circle, the start and end points are the same, and the midpoint is at the 180 position.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDowelSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.md)  
[IDowelSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.md)  
[IDowelSymbol::IGetArcPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~IGetArcPoints.md)

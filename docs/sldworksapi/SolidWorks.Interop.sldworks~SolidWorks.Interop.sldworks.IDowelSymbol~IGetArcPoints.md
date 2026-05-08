# IGetArcPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~IGetArcPoints`

Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based.
Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetArcPoints() As System.Double
```

```

Dim instance As IDowelSymbol
Dim value As System.Double
 
value = instance.IGetArcPoints()
```

```

System.double IGetArcPoints()
```

```

System.double IGetArcPoints(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of size 6 containing start, mid, and end point x and y coordinates

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

If the arc segment is a complete circle, the start and end points are the same, and the midpoint is at the 180 position.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDowelSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.md)  
[IDowelSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.md)  
[IDowelSymbol::GetArcPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetArcPoints.md)

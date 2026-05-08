# GetLength3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength3`

Gets the length of a curve between the specified parameters.
Gets the length of a curve between the specified parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLength3( _
   ByVal StartParam As System.Double, _
   ByVal EndParam As System.Double _
) As System.Double
```

```

Dim instance As ICurve
Dim StartParam As System.Double
Dim EndParam As System.Double
Dim value As System.Double
 
value = instance.GetLength3(StartParam, EndParam)
```

```

System.double GetLength3( 
   System.double StartParam,
   System.double EndParam
)
```

```

System.double GetLength3( 
   System.double StartParam,
   System.double EndParam
) 
```

#### Parameters

*StartParam*
:   Start parameter

*EndParam*
:   End parameter

#### Return Value

Length of the curve between the two parameters

Remarks

This method returns the length of the holding (e.g., trimmed) curve and not the base curve. The now obsolete [ICurve::Length2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength2.md) returned the length of the base curve.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)

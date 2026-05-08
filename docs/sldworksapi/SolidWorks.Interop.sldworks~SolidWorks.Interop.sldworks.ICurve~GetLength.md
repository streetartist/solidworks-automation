# GetLength Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength`

Obsolete. Superseded by ICurve::GetLength2.
Obsolete. Superseded by [ICurve::GetLength2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLength( _
   ByVal StartParam As System.Double, _
   ByVal EndParam As System.Double _
) As System.Double
```

```

Dim instance As ICurve
Dim StartParam As System.Double
Dim EndParam As System.Double
Dim value As System.Double
 
value = instance.GetLength(StartParam, EndParam)
```

```

System.double GetLength( 
   System.double StartParam,
   System.double EndParam
)
```

```

System.double GetLength( 
   System.double StartParam,
   System.double EndParam
) 
```

#### Parameters

*StartParam*

*EndParam*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)

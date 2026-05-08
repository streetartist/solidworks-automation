# ICreateTrimmedCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICreateTrimmedCurve`

Obsolete. Superseded by ICurve::CreateTrimmedCurve2.
Obsolete. Superseded by [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateTrimmedCurve( _
   ByRef Start As System.Double, _
   ByRef End As System.Double _
) As Curve
```

```

Dim instance As ICurve
Dim Start As System.Double
Dim End As System.Double
Dim value As Curve
 
value = instance.ICreateTrimmedCurve(Start, End)
```

```

Curve ICreateTrimmedCurve( 
   ref System.double Start,
   ref System.double End
)
```

```

Curve^ ICreateTrimmedCurve( 
   System.double% Start,
   System.double% End
) 
```

#### Parameters

*Start*

*End*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)

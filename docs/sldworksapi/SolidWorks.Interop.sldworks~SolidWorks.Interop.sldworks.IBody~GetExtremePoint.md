# GetExtremePoint Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~GetExtremePoint`

Obsolete. Superseded by IBody2::GetExtremePoint.
Obsolete. Superseded by [IBody2::GetExtremePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetExtremePoint.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExtremePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByRef Outx As System.Double, _
   ByRef Outy As System.Double, _
   ByRef Outz As System.Double _
) As System.Boolean
```

```

Dim instance As IBody
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Outx As System.Double
Dim Outy As System.Double
Dim Outz As System.Double
Dim value As System.Boolean
 
value = instance.GetExtremePoint(X, Y, Z, Outx, Outy, Outz)
```

```

System.bool GetExtremePoint( 
   System.double X,
   System.double Y,
   System.double Z,
   out System.double Outx,
   out System.double Outy,
   out System.double Outz
)
```

```

System.bool GetExtremePoint( 
   System.double X,
   System.double Y,
   System.double Z,
   [Out] System.double Outx,
   [Out] System.double Outy,
   [Out] System.double Outz
) 
```

#### Parameters

*X*

*Y*

*Z*

*Outx*

*Outy*

*Outz*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)

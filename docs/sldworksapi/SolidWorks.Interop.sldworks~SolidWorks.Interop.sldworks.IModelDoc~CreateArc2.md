# CreateArc2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateArc2`

Obsolete. Superseded by IModelDoc2::CreateArc2.
Obsolete. Superseded by [IModelDoc2::CreateArc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArc2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateArc2( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Xp1 As System.Double, _
   ByVal Yp1 As System.Double, _
   ByVal Zp1 As System.Double, _
   ByVal Xp2 As System.Double, _
   ByVal Yp2 As System.Double, _
   ByVal Zp2 As System.Double, _
   ByVal Direction As System.Short _
) As System.Object
```

```

Dim instance As IModelDoc
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Xp1 As System.Double
Dim Yp1 As System.Double
Dim Zp1 As System.Double
Dim Xp2 As System.Double
Dim Yp2 As System.Double
Dim Zp2 As System.Double
Dim Direction As System.Short
Dim value As System.Object
 
value = instance.CreateArc2(XC, YC, Zc, Xp1, Yp1, Zp1, Xp2, Yp2, Zp2, Direction)
```

```

System.object CreateArc2( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp1,
   System.double Yp1,
   System.double Zp1,
   System.double Xp2,
   System.double Yp2,
   System.double Zp2,
   System.short Direction
)
```

```

System.Object^ CreateArc2( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp1,
   System.double Yp1,
   System.double Zp1,
   System.double Xp2,
   System.double Yp2,
   System.double Zp2,
   System.short Direction
) 
```

#### Parameters

*XC*

*YC*

*Zc*

*Xp1*

*Yp1*

*Zp1*

*Xp2*

*Yp2*

*Zp2*

*Direction*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)

# ICreateCircle2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateCircle2`

Obsolete. Superseded by IModelDoc2::ICreateCircle2.
Obsolete. Superseded by [IModelDoc2::ICreateCircle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateCircle2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateCircle2( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Xp As System.Double, _
   ByVal Yp As System.Double, _
   ByVal Zp As System.Double _
) As SketchSegment
```

```

Dim instance As IModelDoc
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Xp As System.Double
Dim Yp As System.Double
Dim Zp As System.Double
Dim value As SketchSegment
 
value = instance.ICreateCircle2(XC, YC, Zc, Xp, Yp, Zp)
```

```

SketchSegment ICreateCircle2( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp
)
```

```

SketchSegment^ ICreateCircle2( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp
) 
```

#### Parameters

*XC*

*YC*

*Zc*

*Xp*

*Yp*

*Zp*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)

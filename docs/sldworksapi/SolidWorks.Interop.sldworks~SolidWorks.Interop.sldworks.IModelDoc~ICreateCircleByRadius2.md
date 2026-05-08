# ICreateCircleByRadius2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateCircleByRadius2`

Obsolete. Superseded by IModelDoc2::ICreateCircleByRadius2.
Obsolete. Superseded by [IModelDoc2::ICreateCircleByRadius2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateCircleByRadius2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateCircleByRadius2( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Radius As System.Double _
) As SketchSegment
```

```

Dim instance As IModelDoc
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Radius As System.Double
Dim value As SketchSegment
 
value = instance.ICreateCircleByRadius2(XC, YC, Zc, Radius)
```

```

SketchSegment ICreateCircleByRadius2( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Radius
)
```

```

SketchSegment^ ICreateCircleByRadius2( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Radius
) 
```

#### Parameters

*XC*

*YC*

*Zc*

*Radius*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)

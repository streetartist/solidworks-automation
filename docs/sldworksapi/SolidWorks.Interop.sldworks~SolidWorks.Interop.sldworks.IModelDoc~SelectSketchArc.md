# SelectSketchArc Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectSketchArc`

Obsolete. Superseded by IModelDoc2::SelectSketchArc.
Obsolete. Superseded by [IModelDoc2::SelectSketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectSketchArc.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SelectSketchArc( _
   ByVal X0 As System.Double, _
   ByVal Y0 As System.Double, _
   ByVal Inc0 As System.Integer, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Inc1 As System.Integer, _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal IncC As System.Integer, _
   ByVal RotDir As System.Integer _
) 
```

```

Dim instance As IModelDoc
Dim X0 As System.Double
Dim Y0 As System.Double
Dim Inc0 As System.Integer
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Inc1 As System.Integer
Dim XC As System.Double
Dim YC As System.Double
Dim IncC As System.Integer
Dim RotDir As System.Integer
 
instance.SelectSketchArc(X0, Y0, Inc0, X1, Y1, Inc1, XC, YC, IncC, RotDir)
```

```

void SelectSketchArc( 
   System.double X0,
   System.double Y0,
   System.int Inc0,
   System.double X1,
   System.double Y1,
   System.int Inc1,
   System.double XC,
   System.double YC,
   System.int IncC,
   System.int RotDir
)
```

```

void SelectSketchArc( 
   System.double X0,
   System.double Y0,
   System.int Inc0,
   System.double X1,
   System.double Y1,
   System.int Inc1,
   System.double XC,
   System.double YC,
   System.int IncC,
   System.int RotDir
) 
```

#### Parameters

*X0*

*Y0*

*Inc0*

*X1*

*Y1*

*Inc1*

*XC*

*YC*

*IncC*

*RotDir*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)

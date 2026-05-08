# SelectSketchLine Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectSketchLine`

Obsolete. Superseded by IModelDocExtension::SelectByID2.
Obsolete. Superseded by [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SelectSketchLine( _
   ByVal X0 As System.Double, _
   ByVal Y0 As System.Double, _
   ByVal Inc0 As System.Integer, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Inc1 As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim X0 As System.Double
Dim Y0 As System.Double
Dim Inc0 As System.Integer
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Inc1 As System.Integer
 
instance.SelectSketchLine(X0, Y0, Inc0, X1, Y1, Inc1)
```

```

void SelectSketchLine( 
   System.double X0,
   System.double Y0,
   System.int Inc0,
   System.double X1,
   System.double Y1,
   System.int Inc1
)
```

```

void SelectSketchLine( 
   System.double X0,
   System.double Y0,
   System.int Inc0,
   System.double X1,
   System.double Y1,
   System.int Inc1
) 
```

#### Parameters

*X0*

*Y0*

*Inc0*

*X1*

*Y1*

*Inc1*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)

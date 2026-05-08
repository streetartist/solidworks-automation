# SelectSketchPoint Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectSketchPoint`

Obsolete. Superseded by IModelDocExtension::SelectByID2.
Obsolete. Superseded by [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SelectSketchPoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Incidence As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Incidence As System.Integer
 
instance.SelectSketchPoint(X, Y, Incidence)
```

```

void SelectSketchPoint( 
   System.double X,
   System.double Y,
   System.int Incidence
)
```

```

void SelectSketchPoint( 
   System.double X,
   System.double Y,
   System.int Incidence
) 
```

#### Parameters

*X*

*Y*

*Incidence*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)

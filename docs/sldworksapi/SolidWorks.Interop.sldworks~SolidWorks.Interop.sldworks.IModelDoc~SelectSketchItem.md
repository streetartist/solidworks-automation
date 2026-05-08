# SelectSketchItem Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectSketchItem`

Obsolete. Superseded by IModelDoc2::SelectSketchItem.
Obsolete. Superseded by [IModelDoc2::SelectSketchItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectSketchItem.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectSketchItem( _
   ByVal SelOpt As System.Integer, _
   ByVal Name As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim SelOpt As System.Integer
Dim Name As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.SelectSketchItem(SelOpt, Name, X, Y, Z)
```

```

System.bool SelectSketchItem( 
   System.int SelOpt,
   System.string Name,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool SelectSketchItem( 
   System.int SelOpt,
   System.String^ Name,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*SelOpt*

*Name*

*X*

*Y*

*Z*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)

# InsertBlock Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBlock`

Obsolete. Superseded by ISketchManager::InsertSketchBlockInstance.
Obsolete. Superseded by [ISketchManager::InsertSketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBlock( _
   ByVal FileName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Scale As System.Double _
) As BlockInstance
```

```

Dim instance As IDrawingDoc
Dim FileName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Angle As System.Double
Dim Scale As System.Double
Dim value As BlockInstance
 
value = instance.InsertBlock(FileName, X, Y, Angle, Scale)
```

```

BlockInstance InsertBlock( 
   System.string FileName,
   System.double X,
   System.double Y,
   System.double Angle,
   System.double Scale
)
```

```

BlockInstance^ InsertBlock( 
   System.String^ FileName,
   System.double X,
   System.double Y,
   System.double Angle,
   System.double Scale
) 
```

#### Parameters

*FileName*

*X*

*Y*

*Angle*

*Scale*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

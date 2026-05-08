# InsertCustomSymbol2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCustomSymbol2`

Obsolete. Superseded by ISketchManager::InsertSketchBlockInstance.
Obsolete. Superseded by [ISketchManager::InsertSketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCustomSymbol2( _
   ByVal FileName As System.String _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim FileName As System.String
Dim value As System.Object
 
value = instance.InsertCustomSymbol2(FileName)
```

```

System.object InsertCustomSymbol2( 
   System.string FileName
)
```

```

System.Object^ InsertCustomSymbol2( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

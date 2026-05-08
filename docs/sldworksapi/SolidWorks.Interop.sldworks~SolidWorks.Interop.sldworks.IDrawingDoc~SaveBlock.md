# SaveBlock Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveBlock`

Obsolete. Superseded by ISketchBlockDefinition::Save.
Obsolete. Superseded by [ISketchBlockDefinition::Save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~Save.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveBlock( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SaveBlock(FileName)
```

```

System.bool SaveBlock( 
   System.string FileName
)
```

```

System.bool SaveBlock( 
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

# IGetBlockDefinitions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetBlockDefinitions`

Obsolete. Superseded by SketchManager::GetSketchBlockDefinitions.
Obsolete. Superseded by [SketchManager::GetSketchBlockDefinitions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBlockDefinitions( _
   ByVal Count As System.Integer _
) As BlockDefinition
```

```

Dim instance As IDrawingDoc
Dim Count As System.Integer
Dim value As BlockDefinition
 
value = instance.IGetBlockDefinitions(Count)
```

```

BlockDefinition IGetBlockDefinitions( 
   System.int Count
)
```

```

BlockDefinition^ IGetBlockDefinitions( 
   System.int Count
) 
```

#### Parameters

*Count*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

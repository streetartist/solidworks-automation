# GetBlockDefinition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetBlockDefinition`

Obsolete. Superseded by SketchManager::GetSketchBlockDefinitions.
Obsolete. Superseded by [SketchManager::GetSketchBlockDefinitions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBlockDefinition( _
   ByVal Name As System.String _
) As BlockDefinition
```

```

Dim instance As IDrawingDoc
Dim Name As System.String
Dim value As BlockDefinition
 
value = instance.GetBlockDefinition(Name)
```

```

BlockDefinition GetBlockDefinition( 
   System.string Name
)
```

```

BlockDefinition^ GetBlockDefinition( 
   System.String^ Name
) 
```

#### Parameters

*Name*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

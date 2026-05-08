# MakeBlockDefinition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~MakeBlockDefinition`

Obsolete. Superseded by ISkethcManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.
Obsolete. Superseded by [ISkethcManager::MakeSketchBlockFromFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md), [ISketchManager::MakeSketchBlockSelected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md), and [ISketchManager::MakeSketchBlockFromSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeBlockDefinition( _
   ByVal Name As System.String, _
   ByVal XRefFileName As System.String, _
   ByVal Instance As System.Boolean _
) As BlockDefinition
```

```

Dim instance As IDrawingDoc
Dim Name As System.String
Dim XRefFileName As System.String
Dim Instance As System.Boolean
Dim value As BlockDefinition
 
value = instance.MakeBlockDefinition(Name, XRefFileName, Instance)
```

```

BlockDefinition MakeBlockDefinition( 
   System.string Name,
   System.string XRefFileName,
   System.bool Instance
)
```

```

BlockDefinition^ MakeBlockDefinition( 
   System.String^ Name,
   System.String^ XRefFileName,
   System.bool Instance
) 
```

#### Parameters

*Name*

*XRefFileName*

*Instance*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

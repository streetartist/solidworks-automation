# CreateBlockDefinition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateBlockDefinition`

Obsolete. Superseded by ISketchManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.
Obsolete. Superseded by [ISketchManager::MakeSketchBlockFromFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md), [ISketchManager::MakeSketchBlockSelected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md), and [ISketchManager::MakeSketchBlockFromSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBlockDefinition( _
   ByVal Name As System.String, _
   ByVal XRefFileName As System.String, _
   ByVal Instance As System.Boolean, _
   ByVal Segments As System.Object, _
   ByVal Points As System.Object, _
   ByVal Notes As System.Object, _
   ByVal Dimensions As System.Object, _
   ByVal Blocks As System.Object _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim Name As System.String
Dim XRefFileName As System.String
Dim Instance As System.Boolean
Dim Segments As System.Object
Dim Points As System.Object
Dim Notes As System.Object
Dim Dimensions As System.Object
Dim Blocks As System.Object
Dim value As System.Object
 
value = instance.CreateBlockDefinition(Name, XRefFileName, Instance, Segments, Points, Notes, Dimensions, Blocks)
```

```

System.object CreateBlockDefinition( 
   System.string Name,
   System.string XRefFileName,
   System.bool Instance,
   System.object Segments,
   System.object Points,
   System.object Notes,
   System.object Dimensions,
   System.object Blocks
)
```

```

System.Object^ CreateBlockDefinition( 
   System.String^ Name,
   System.String^ XRefFileName,
   System.bool Instance,
   System.Object^ Segments,
   System.Object^ Points,
   System.Object^ Notes,
   System.Object^ Dimensions,
   System.Object^ Blocks
) 
```

#### Parameters

*Name*

*XRefFileName*

*Instance*

*Segments*

*Points*

*Notes*

*Dimensions*

*Blocks*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

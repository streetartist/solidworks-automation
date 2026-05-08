# CreateCustomSymbol Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCustomSymbol`

Obsolete. Superseded by ISkethcManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.
Obsolete. Superseded by [ISkethcManager::MakeSketchBlockFromFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md), [ISketchManager::MakeSketchBlockSelected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md), and [ISketchManager::MakeSketchBlockFromSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCustomSymbol( _
   ByVal Segments As System.Object, _
   ByVal Points As System.Object, _
   ByVal Notes As System.Object _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim Segments As System.Object
Dim Points As System.Object
Dim Notes As System.Object
Dim value As System.Object
 
value = instance.CreateCustomSymbol(Segments, Points, Notes)
```

```

System.object CreateCustomSymbol( 
   System.object Segments,
   System.object Points,
   System.object Notes
)
```

```

System.Object^ CreateCustomSymbol( 
   System.Object^ Segments,
   System.Object^ Points,
   System.Object^ Notes
) 
```

#### Parameters

*Segments*

*Points*

*Notes*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

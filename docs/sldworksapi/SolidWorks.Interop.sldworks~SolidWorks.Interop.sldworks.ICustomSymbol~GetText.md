# GetText Method (ICustomSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~GetText`

Obsolete. Superseded by ISketchBlockDefinition::GetNoteCount and ISketchBlockDefinition::GetNotes.
Obsolete. Superseded by [ISketchBlockDefinition::GetNoteCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNoteCount.md) and [ISketchBlockDefinition::GetNotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNotes.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetText( _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As ICustomSymbol
Dim Index As System.Integer
Dim value As System.String
 
value = instance.GetText(Index)
```

```

System.string GetText( 
   System.int Index
)
```

```

System.String^ GetText( 
   System.int Index
) 
```

#### Parameters

*Index*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.md)  
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.md)

# SetTextFormatAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextFormatAtIndex`

Obsolete. Superseded by IAnnotation::SetTextFormat and IAnnotation::ISetTextFormat.
Obsolete. Superseded by [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md) and [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTextFormatAtIndex( _
   ByVal Index As System.Integer, _
   ByVal TextFormat As System.Object _
) 
```

```

Dim instance As INote
Dim Index As System.Integer
Dim TextFormat As System.Object
 
instance.SetTextFormatAtIndex(Index, TextFormat)
```

```

void SetTextFormatAtIndex( 
   System.int Index,
   System.object TextFormat
)
```

```

void SetTextFormatAtIndex( 
   System.int Index,
   System.Object^ TextFormat
) 
```

#### Parameters

*Index*

*TextFormat*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)

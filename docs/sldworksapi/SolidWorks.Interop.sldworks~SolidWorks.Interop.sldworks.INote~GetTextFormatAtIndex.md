# GetTextFormatAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFormatAtIndex`

Obsolete. Superseded by IAnnotation::GetTextFormat and IAnnotation::IGetTextFormat.
Obsolete. Superseded by [IAnnotation::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md) and [IAnnotation::IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextFormatAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As INote
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetTextFormatAtIndex(Index)
```

```

System.object GetTextFormatAtIndex( 
   System.int Index
)
```

```

System.Object^ GetTextFormatAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)

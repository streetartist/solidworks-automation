# ISetTextFormat Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ISetTextFormat`

Obsolete. Superseded by IAnnotation::SetTextFormat and IAnnotation::ISetTextFormat.
Obsolete. Superseded by [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md) and [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetTextFormat( _
   ByVal TextFormatType As System.Integer, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

```

Dim instance As INote
Dim TextFormatType As System.Integer
Dim TextFormat As TextFormat
Dim value As System.Boolean
 
value = instance.ISetTextFormat(TextFormatType, TextFormat)
```

```

System.bool ISetTextFormat( 
   System.int TextFormatType,
   TextFormat TextFormat
)
```

```

System.bool ISetTextFormat( 
   System.int TextFormatType,
   TextFormat^ TextFormat
) 
```

#### Parameters

*TextFormatType*

*TextFormat*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)

# SetTextFormat Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetTextFormat`

Obsolete. Superseded by IAnnotation::SetTextFormat.
Obsolete. Superseded by [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTextFormat( _
   ByVal TextFormatType As System.Integer, _
   ByVal TextFormat As System.Object _
) As System.Boolean
```

```

Dim instance As IGtol
Dim TextFormatType As System.Integer
Dim TextFormat As System.Object
Dim value As System.Boolean
 
value = instance.SetTextFormat(TextFormatType, TextFormat)
```

```

System.bool SetTextFormat( 
   System.int TextFormatType,
   System.object TextFormat
)
```

```

System.bool SetTextFormat( 
   System.int TextFormatType,
   System.Object^ TextFormat
) 
```

#### Parameters

*TextFormatType*

*TextFormat*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)

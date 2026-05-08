# ISetTextFormat Method (IDrSection)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetTextFormat`

Sets the text format for the text for this section line.
Sets the text format for the text for this section line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetTextFormat( _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

```

Dim instance As IDrSection
Dim UseDoc As System.Boolean
Dim TextFormat As TextFormat
Dim value As System.Boolean
 
value = instance.ISetTextFormat(UseDoc, TextFormat)
```

```

System.bool ISetTextFormat( 
   System.bool UseDoc,
   TextFormat TextFormat
)
```

```

System.bool ISetTextFormat( 
   System.bool UseDoc,
   TextFormat^ TextFormat
) 
```

#### Parameters

*UseDoc*
:   True if set to use the appropriate document default setting, false if it is not (see **Remarks**)

*TextFormat*
:   Pointer to the [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) object for this section line text

#### Return Value

True if text format is successfully set, false if not

Remarks

If UseDoc is True, then use the appropriate document default setting. SOLIDWORKS will also ignore TextFormat, which you should set to NULL.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetTextFormat.md)  
[IDrSection::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextFormat.md)  
[IDrSection::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextFormat.md)

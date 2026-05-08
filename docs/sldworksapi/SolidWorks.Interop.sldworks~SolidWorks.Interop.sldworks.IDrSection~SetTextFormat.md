# SetTextFormat Method (IDrSection)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetTextFormat`

Sets the text format for the text for this section line.
Sets the text format for the text for this section line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTextFormat( _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As System.Object _
) As System.Boolean
```

```

Dim instance As IDrSection
Dim UseDoc As System.Boolean
Dim TextFormat As System.Object
Dim value As System.Boolean
 
value = instance.SetTextFormat(UseDoc, TextFormat)
```

```

System.bool SetTextFormat( 
   System.bool UseDoc,
   System.object TextFormat
)
```

```

System.bool SetTextFormat( 
   System.bool UseDoc,
   System.Object^ TextFormat
) 
```

#### Parameters

*UseDoc*
:   True if set to use the appropriate document default setting, false if it is not (see **Remarks**)

*TextFormat*
:   Text format for this section line text

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
[IDrSection::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetTextFormat.md)  
[IDrSection::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextFormat.md)  
[IDrSection::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextFormat.md)

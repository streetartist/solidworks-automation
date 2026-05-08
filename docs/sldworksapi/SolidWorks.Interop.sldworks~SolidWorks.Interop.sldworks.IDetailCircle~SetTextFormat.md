# SetTextFormat Method (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetTextFormat`

Sets the text format for this detail circle.
Sets the text format for this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTextFormat( _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

```

Dim instance As IDetailCircle
Dim UseDoc As System.Boolean
Dim TextFormat As TextFormat
Dim value As System.Boolean
 
value = instance.SetTextFormat(UseDoc, TextFormat)
```

```

System.bool SetTextFormat( 
   System.bool UseDoc,
   TextFormat TextFormat
)
```

```

System.bool SetTextFormat( 
   System.bool UseDoc,
   TextFormat^ TextFormat
) 
```

#### Parameters

*UseDoc*
:   True to use the local document text format, false to use the text format specified by  
    TextFormat

*TextFormat*
:   [Text format](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) to use if UseDoc is false

#### Return Value

True if the format was set successfully, false if it was not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetTextFormat.md)  
[IDetailCircle::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetUseDocTextFormat.md)

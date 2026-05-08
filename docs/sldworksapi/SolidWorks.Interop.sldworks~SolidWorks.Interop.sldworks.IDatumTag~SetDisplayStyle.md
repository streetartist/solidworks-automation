# SetDisplayStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetDisplayStyle`

Sets the display style of this datum tag.
Sets the display style of this datum tag.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDisplayStyle( _
   ByVal UseDoc As System.Boolean, _
   ByVal Style As System.Integer _
) As System.Boolean
```

```

Dim instance As IDatumTag
Dim UseDoc As System.Boolean
Dim Style As System.Integer
Dim value As System.Boolean
 
value = instance.SetDisplayStyle(UseDoc, Style)
```

```

System.bool SetDisplayStyle( 
   System.bool UseDoc,
   System.int Style
)
```

```

System.bool SetDisplayStyle( 
   System.bool UseDoc,
   System.int Style
) 
```

#### Parameters

*UseDoc*
:   True to use the document setting for the datum tag's display style, false to not

*Style*
:   Display style as defined in [swDatumDisplayType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumDisplayType_e.html)

#### Return Value

True if the specified display style is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::GetDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetDisplayStyle.md)  
[IDatumTag::GetUseDocDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetUseDocDisplayStyle.md)

# GetDisplayStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetDisplayStyle`

Gets the display style of this datum tag.
Gets the display style of this datum tag.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayStyle() As System.Integer
```

```

Dim instance As IDatumTag
Dim value As System.Integer
 
value = instance.GetDisplayStyle()
```

```

System.int GetDisplayStyle()
```

```

System.int GetDisplayStyle(); 
```

#### Return Value

Display style as defined in [swDatumDisplayType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumDisplayType_e.html) (see **Remarks**)

Remarks

This method does not return swDatumDisplayType\_Default if the datum tag is set to use the document default setting. Instead, either swDatumDisplayType\_Roundgb or swDatumDisplayType\_Square is returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::GetUseDocDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetUseDocDisplayStyle.md)  
[IDatumTag::SetDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetDisplayStyle.md)

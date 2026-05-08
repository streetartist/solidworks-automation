# GetUseDocDisplayStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetUseDocDisplayStyle`

Gets whether this datum tag uses the document setting for its display style.
Gets whether this datum tag uses the document setting for its display style.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseDocDisplayStyle() As System.Boolean
```

```

Dim instance As IDatumTag
Dim value As System.Boolean
 
value = instance.GetUseDocDisplayStyle()
```

```

System.bool GetUseDocDisplayStyle()
```

```

System.bool GetUseDocDisplayStyle(); 
```

#### Return Value

True to use the document setting for the datum feature symbol's display style, false to use local display style

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::GetDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetDisplayStyle.md)  
[IDatumTag::SetDisplayStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~SetDisplayStyle.md)

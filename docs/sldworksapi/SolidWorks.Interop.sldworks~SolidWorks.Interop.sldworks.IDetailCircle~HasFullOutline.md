# HasFullOutline Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~HasFullOutline`

Gets whether this detail circle has a full outline in the detail view.
Gets whether this detail circle has a full outline in the detail view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HasFullOutline() As System.Boolean
```

```

Dim instance As IDetailCircle
Dim value As System.Boolean
 
value = instance.HasFullOutline()
```

```

System.bool HasFullOutline()
```

```

System.bool HasFullOutline(); 
```

#### Return Value

True if the detail circle has a full outline in the detail view, false if not

Remarks

This method is only available when [IDetailCircle::NoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline.md) is false.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::SetFullOutline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetFullOutline.md)

# EnableSelection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableSelection`

Enables or disables selection.
Enables or disables selection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableSelection As System.Boolean
```

```

Dim instance As ISelectionMgr
Dim value As System.Boolean
 
instance.EnableSelection = value
 
value = instance.EnableSelection
```

```

System.bool EnableSelection {get; set;}
```

```

property System.bool EnableSelection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if selection is enabled, false if disabled

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::EnableContourSelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableContourSelection.md)

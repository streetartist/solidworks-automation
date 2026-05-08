# CustomPropertyManager Property (ICutListItem)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem~CustomPropertyManager`

Gets the custom property manager for this configuration-specific cut list.
Gets the custom property manager for this configuration-specific cut list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CustomPropertyManager As CustomPropertyManager
```

```

Dim instance As ICutListItem
Dim value As CustomPropertyManager
 
value = instance.CustomPropertyManager
```

```

CustomPropertyManager CustomPropertyManager {get;}
```

```

property CustomPropertyManager^ CustomPropertyManager {
   CustomPropertyManager^ get();
}
```

#### Property Value

[ICustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICutListItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem.md)  
[ICutListItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem_members.md)

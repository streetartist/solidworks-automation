# LargeIconList Property (IFlyoutGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~LargeIconList`

Obsolete. Superseded by IFlyoutGroup::IconList.
Obsolete. Superseded by [IFlyoutGroup::IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~IconList.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LargeIconList As System.String
```

```

Dim instance As IFlyoutGroup
Dim value As System.String
 
instance.LargeIconList = value
 
value = instance.LargeIconList
```

```

System.string LargeIconList {get; set;}
```

```

property System.String^ LargeIconList {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path to the bitmap or PNG containing all of the large button and separator images for this flyout

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.md)  
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.md)  
[IFlyoutGroup::AddCommandItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~AddCommandItem.md)  
[IFlyoutGroup::ReplaceCommandItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~ReplaceCommandItem.md)

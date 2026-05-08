# SmallMainIcon Property (IFlyoutGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~SmallMainIcon`

Obsolete. Superseded by IFlyoutGroup::MainIconList.
Obsolete. Superseded by [IFlyoutGroup::MainIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup~MainIconList.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SmallMainIcon As System.String
```

```

Dim instance As IFlyoutGroup
Dim value As System.String
 
instance.SmallMainIcon = value
 
value = instance.SmallMainIcon
```

```

System.string SmallMainIcon {get; set;}
```

```

property System.String^ SmallMainIcon {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path to the small bitmap or PNG used in this flyout

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlyoutGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup.md)  
[IFlyoutGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.md)

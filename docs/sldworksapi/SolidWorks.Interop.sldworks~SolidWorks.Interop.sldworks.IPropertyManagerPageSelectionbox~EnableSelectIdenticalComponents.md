# EnableSelectIdenticalComponents Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~EnableSelectIdenticalComponents`

Gets or sets whether to enable Select Identical Components in the context menu of this PropertyManager page selection box.
Gets or sets whether to enable **Select Identical Components** in the context menu of this PropertyManager page selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableSelectIdenticalComponents As System.Boolean
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Boolean
 
instance.EnableSelectIdenticalComponents = value
 
value = instance.EnableSelectIdenticalComponents
```

```

System.bool EnableSelectIdenticalComponents {get; set;}
```

```

property System.bool EnableSelectIdenticalComponents {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable **Select Identical Components** in this selection box's context menu, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)

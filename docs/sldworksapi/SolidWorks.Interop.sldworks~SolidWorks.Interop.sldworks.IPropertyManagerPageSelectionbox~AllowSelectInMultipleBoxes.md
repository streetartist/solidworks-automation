# AllowSelectInMultipleBoxes Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~AllowSelectInMultipleBoxes`

Gets or sets whether an entity can be selected in this selection box if the entity is selected elsewhere.
Gets or sets whether an entity can be selected in this selection box if the entity is selected elsewhere.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AllowSelectInMultipleBoxes As System.Boolean
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Boolean
 
instance.AllowSelectInMultipleBoxes = value
 
value = instance.AllowSelectInMultipleBoxes
```

```

System.bool AllowSelectInMultipleBoxes {get; set;}
```

```

property System.bool AllowSelectInMultipleBoxes {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

|  |  |
| --- | --- |
| **If...** | **Then...** |
| true | - When an entity is selected while this selection box is active and that entity is selected in a different selection box, then the entity is added to this selection box. - If the entity is already selected in this selection box, then the entity is removed from the selection box. |
| false | When an entity is selected while this selection box is active and that entity is already selected, then the entity is removed from the selection box. This is the default behavior of a selection box. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)

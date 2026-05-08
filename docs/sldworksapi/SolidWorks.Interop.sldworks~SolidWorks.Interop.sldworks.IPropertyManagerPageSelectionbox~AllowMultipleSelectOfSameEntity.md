# AllowMultipleSelectOfSameEntity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~AllowMultipleSelectOfSameEntity`

Gets or sets whether the same entity can be selected multiple times in this selection box.
Gets or sets whether the same entity can be selected multiple times in this selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AllowMultipleSelectOfSameEntity As System.Boolean
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Boolean
 
instance.AllowMultipleSelectOfSameEntity = value
 
value = instance.AllowMultipleSelectOfSameEntity
```

```

System.bool AllowMultipleSelectOfSameEntity {get; set;}
```

```

property System.bool AllowMultipleSelectOfSameEntity {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the same entity can be selected multiple times in this selection box, false if not

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)

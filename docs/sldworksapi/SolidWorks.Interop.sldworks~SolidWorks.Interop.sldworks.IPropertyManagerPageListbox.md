# IPropertyManagerPageListbox Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox`

Allows you to access a PropertyManager page list box control.
Allows you to access a [PropertyManager page](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) list box control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPropertyManagerPageListbox 
```

```

Dim instance As IPropertyManagerPageListbox
```

```

public interface IPropertyManagerPageListbox 
```

```

public interface class IPropertyManagerPageListbox 
```

Remarks

Implement the event handler [IPropertyManagerPage2Handler8::OnListboxRMBUp](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnListboxRMBUp.md) to position and display a menu when the right mouse button is released.

By default, only one list item can be selected at a time. When another list item is selected, that item becomes the active item, and the previously selected item is cleared. To enable multi-selection, use swPropMgrPageListBoxStyle\_MultipleItemSelect with [IProperytManagerPageListbox:Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~Style.md).

These methods support multi-selection:

- [IPropertyManagerPageListbox::GetSelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItems.md) or [IPropertyManagerPageListbox::IGetSelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~IGetSelectedItems.md)
- [IPropertyManagerPageListbox::GetSelectedItemsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItemsCount.md)
- [IPropertyManagerPageListbox::SetSelectedItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~SetSelectedItem.md)

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

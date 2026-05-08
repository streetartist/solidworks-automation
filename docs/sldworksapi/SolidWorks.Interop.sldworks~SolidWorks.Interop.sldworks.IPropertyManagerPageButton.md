# IPropertyManagerPageButton Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton`

Allows you to access a PropertyManager page button control.
Allows you to access a [PropertyManager page](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) button control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPropertyManagerPageButton 
```

```

Dim instance As IPropertyManagerPageButton
```

```

public interface IPropertyManagerPageButton 
```

```

public interface class IPropertyManagerPageButton 
```

Remarks

Users can resize PropertyManager pages horizontally in SOLIDWORKS 2006 and later. This change in functionality affects the appearance of the buttons on PropertyManager pages created in SOLIDWORKS 2005 and earlier.

In SOLIDWORKS 2005 and earlier, buttons remained aligned vertically at an indented position when a user resized a PropertyManager page. In most instances, these buttons are now centered when a user resizes a PropertyManager page. However, if a button on a PropertyManager page was aligned at the very left edge of the page and it was the only button on that line, then it is assumed that it was intentionally placed at that position and it will stay at that position if a user resizes the page. Any text on the button will also be left justified inside the button. If a button has a bitmap as its label, then the button remains next to the label instead of being centered.

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

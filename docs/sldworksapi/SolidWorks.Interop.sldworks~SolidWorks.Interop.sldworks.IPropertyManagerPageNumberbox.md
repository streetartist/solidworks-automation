# IPropertyManagerPageNumberbox Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox`

Allows you to access a PropertyManager page number box control.
Allows you to access a [PropertyManager page](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) number box control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPropertyManagerPageNumberbox 
```

```

Dim instance As IPropertyManagerPageNumberbox
```

```

public interface IPropertyManagerPageNumberbox 
```

```

public interface class IPropertyManagerPageNumberbox 
```

Remarks

|  |  |
| --- | --- |
| If you implement a... | Then... |
| Spin box | an edit box with attached up and down arrow buttons for incrementing and decrementing the value is created. |
| Combo box/spin box | a text box with:   - a down-arrow button to display the attached drop-down list. You must set up and control the attached drop-down list - up and down buttons for incrementing and decrementing the value   is created.  Use [IPropertyManagerPageNumberbox::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~Style.md) to select the type of combo-box/spin-box number box you want to implement. |

For both types of number boxes, SOLIDWORKS automatically validates the values and units. The up and down arrow buttons automatically increment and decrement the value. Both types of number boxes:

- Accept numerical expressions.
- Store all values as meters or radians and display them in the units specified in the current unit settings.

NOTE: When a document's unit system is set to a non-metric setting, the dimension precision value (the number of digits displayed after a decimal point) is based on the number of digits specified. It is not based on the document's dimension precision settings.

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

Example

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) examples.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

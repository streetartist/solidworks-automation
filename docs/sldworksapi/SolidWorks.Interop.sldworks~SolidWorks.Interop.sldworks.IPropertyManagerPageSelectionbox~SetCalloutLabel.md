# SetCalloutLabel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetCalloutLabel`

Sets the default callout label for selections made in this selection box on the PropertyManager page.
Sets the default callout label for selections made in this selection box on the PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCalloutLabel( _
   ByVal Label As System.String _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim Label As System.String
Dim value As System.Boolean
 
value = instance.SetCalloutLabel(Label)
```

```

System.bool SetCalloutLabel( 
   System.string Label
)
```

```

System.bool SetCalloutLabel( 
   System.String^ Label
) 
```

#### Parameters

*Label*
:   Default callout label

#### Return Value

True if the callout label was set, false if not

Remarks

This property can be used at any time, whether or not the callout is displayed. The label must not be an empty string. By default, the selection box is created without callouts for selections. This method overrides that behavior.

For more control, you can implement the [IPropertyManagerPage2Handler5::OnSelectionboxCalloutCreated](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnSelectionboxCalloutCreated.md) property, which allows you to collect information such as the selection type from the last selection. Next, use the [IPropertyManagerPageSelectionbox::Callout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Callout.md) property to get the [ICallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md) object. Then, use that object's various properties to control the callout text and display characteristics based on that selection information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)

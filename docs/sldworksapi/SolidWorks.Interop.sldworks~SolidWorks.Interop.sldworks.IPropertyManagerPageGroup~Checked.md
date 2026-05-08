# Checked Property (IPropertyManagerPageGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~Checked`

Gets or sets the setting of a check box in the title of a group box on a PropertyManager page.
Gets or sets the setting of a check box in the title of a group box on a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Checked As System.Boolean
```

```

Dim instance As IPropertyManagerPageGroup
Dim value As System.Boolean
 
instance.Checked = value
 
value = instance.Checked
```

```

System.bool Checked {get; set;}
```

```

property System.bool Checked {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the check box is selected, false if not

Remarks

A group box on PropertyManager page can be created with a check box in its title. Selecting the check box causes the group box to expand so that all of the controls on that group box can be seen by the end-user. Clearing the check box causes the group box to close, or compress, so that all of the controls on that group box are hidden.

When a group box is expanded, the states of the controls within the group are not changed.  For example, if all of the controls are disabled, they remain disabled when the group box is expanded. The owner of the PropertyManager page is responsible for setting the control states.

When the end-user selects or clears the check box of a group box, the [IPropertyManagerPage2Handler5::OnGroupCheck](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnGroupCheck.md) method is called, so that your program can react to this event and do things such as enabling the appropriate controls.  However, if your program is using this property to set the check box, then this method is not called and your program should set the controls after setting this property.

This property does not control whether or not there is a check box on your group box. That is determined when the group box is added. See [IPropertyManagerPage2::AddGroupBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.md) or [IPropertyManagerPage2::IAddGroupBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.md), specifically the Options argument.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md)  
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.md)

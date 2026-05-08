# EditText Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~EditText`

Gets or sets the text in the combo box.
Gets or sets the text in the combo box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EditText As System.String
```

```

Dim instance As IPropertyManagerPageCombobox
Dim value As System.String
 
instance.EditText = value
 
value = instance.EditText
```

```

System.string EditText {get; set;}
```

```

property System.String^ EditText {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Text for or in combo box

Remarks

[IPropertyManagerPageCombobox::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~Style.md) must be set to swPropMgrPageComboBoxStyle\_EditableText to edit text in a combo box.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.md)  
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.md)

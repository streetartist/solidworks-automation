# State Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox~State`

Gets or sets the state of this check box.
Gets or sets the state of this check box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property State As System.Integer
```

```

Dim instance As IPropertyManagerPageCheckbox
Dim value As System.Integer
 
instance.State = value
 
value = instance.State
```

```

System.int State {get; set;}
```

```

property System.int State {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

State of this check box as defined in [swPropertyManagerCheckboxState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertyManagerCheckboxState_e.html)

Remarks

If you use this property to set the state of a check box, then you must use this property to modify the state of the check box.

Example

[Set Focus on PropertyManager Page Control (C#)](Set_Focus_on_PropertyManager_Page_Control_Example_CSharp.htm)  
[Set Focus on PropertyManager Page Control (VB.NET)](Set_Focus_on_PropertyManager_Page_Control_Example_VBNET.htm)  
[Set Focus on PropertyManager Page Control (VBA)](Set_Focus_on_PropertyManager_Page_Control_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageCheckbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox.md)  
[IPropertyManagerPageCheckbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox_members.md)

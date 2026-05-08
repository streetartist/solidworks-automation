# swPropMgrPageComboBoxStyle_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageComboBoxStyle_e`

PropertyManager page combobox styles.
PropertyManager page combobox styles.

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("4D667123-E0F2-4BBF-B7A9-947E16C68DE4")>
Public Enum swPropMgrPageComboBoxStyle_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropMgrPageComboBoxStyle_e
```

```

[System.Runtime.InteropServices.Guid("4D667123-E0F2-4BBF-B7A9-947E16C68DE4")]
public enum swPropMgrPageComboBoxStyle_e : System.Enum 
```

```

public enum swPropMgrPageComboBoxStyle_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("4D667123-E0F2-4BBF-B7A9-947E16C68DE4")
public enum swPropMgrPageComboBoxStyle_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("4D667123-E0F2-4BBF-B7A9-947E16C68DE4")]
__value public enum swPropMgrPageComboBoxStyle_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("4D667123-E0F2-4BBF-B7A9-947E16C68DE4")]
public enum class swPropMgrPageComboBoxStyle_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropMgrPageComboBoxStyle\_AvoidSelectionText** | 8 or 0x8; The item the user selects in the attached drop-down list does not appear in the combo box. Instead, the user's selection causes the add-in to get a callback via [IPropertyManagerPage2Handler4::OnComboboxSelectionChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler4~OnComboboxSelectionChanged.md). The Id argument is the combo box |
| **swPropMgrPageComboBoxStyle\_EditableText** | 2 or 0x2; Allows editing of the text in the combo box |
| **swPropMgrPageComboBoxStyle\_EditBoxReadOnly** | 4 or 0x4; User can only select a value from the attached drop-down list for the combo box  NOTE: You can set swPropMgrPageComboBoxStyle\_EditBoxReadOnly either before or after the PropertyManager page is displayed. If set after the PropertyManager page is displayed and the box contains editable text, then that text cannot be edited by the user. However, you can use [IPropertyManagerPageCombobox::EditText](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageCombobox~EditText.html) to edit the text in the combo box. |
| **swPropMgrPageComboBoxStyle\_Sorted** | 1 or 0x1; Sort the items in the attached drop-down list of the combo box in alphabetical order |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropMgrPageComboBoxStyle\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)

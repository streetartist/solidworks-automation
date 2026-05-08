# SetLabel2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLabel2`

Sets the label for this section view.
Sets the label for this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLabel2( _
   ByVal Label As System.String _
) As System.Integer
```

```

Dim instance As IDrSection
Dim Label As System.String
Dim value As System.Integer
 
value = instance.SetLabel2(Label)
```

```

System.int SetLabel2( 
   System.string Label
)
```

```

System.int SetLabel2( 
   System.String^ Label
) 
```

#### Parameters

*Label*
:   Label for this section view

#### Return Value

Value as defined in [swSetSectionLabelStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetSectionLabelStatus_e.html)

Remarks

|  |  |
| --- | --- |
| **If the return status...** | **Then the operation...** |
| < 0 | Failed |
| = 0 | Succeeded |
| > 0 | Succeeded. However:   - If you attempt to set the section label to the same value as an existing section label and the drawing standard does allow duplicate section labels, then status = 1. That is, the label is changed, but the status indicates that the label is a duplicate, which is not allowed by the drawing standard. - If the dimensioning standard allows duplicate section labels, then status = 0. |

Example

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)  
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)  
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::GetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLabel.md)

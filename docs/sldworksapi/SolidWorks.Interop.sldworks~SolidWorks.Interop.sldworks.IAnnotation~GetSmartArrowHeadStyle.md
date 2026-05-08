# GetSmartArrowHeadStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSmartArrowHeadStyle`

Gets the setting for smart arrowhead style for this annotation.
Gets the setting for smart arrowhead style for this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSmartArrowHeadStyle() As System.Boolean
```

```

Dim instance As IAnnotation
Dim value As System.Boolean
 
value = instance.GetSmartArrowHeadStyle()
```

```

System.bool GetSmartArrowHeadStyle()
```

```

System.bool GetSmartArrowHeadStyle(); 
```

#### Return Value

True if the smart arrowhead style setting is enabled, false if the smart arrowhead style setting is disabled

Remarks

The smart arrowhead style flag is a characteristic of the annotation, not individual leaders. You can get or set it whether or not leaders are currently displayed.

|  |  |
| --- | --- |
| **Use...** | **To...** |
| [IAnnotation::GetLeaderStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderStyle.md) | Get leader characteristics |
| [IAnnotation::SetLeader3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.md) | Set leader characteristics |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)

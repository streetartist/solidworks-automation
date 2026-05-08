# IsAppliedToAllConfigurations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsAppliedToAllConfigurations`

Gets whether a dimension is currently applied to all configurations of the model or to just the current configuration.
Gets whether a dimension is currently applied to all configurations of the model or to just the current configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsAppliedToAllConfigurations() As System.Boolean
```

```

Dim instance As IDimension
Dim value As System.Boolean
 
value = instance.IsAppliedToAllConfigurations()
```

```

System.bool IsAppliedToAllConfigurations()
```

```

System.bool IsAppliedToAllConfigurations(); 
```

#### Return Value

True if the dimension is applied to all configurations, false if the dimension is applied only to the current configuration

Remarks

If there is only one configuration of a part, this method returns True.

This method applies only to dimensions that are driven by or drive geometry. For example, this method does not apply to reference dimensions (see [IDimension::IsReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsReference.md) and [IDimension::DrivenState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DrivenState.md)). This method returns True for reference dimensions.

Example

[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)

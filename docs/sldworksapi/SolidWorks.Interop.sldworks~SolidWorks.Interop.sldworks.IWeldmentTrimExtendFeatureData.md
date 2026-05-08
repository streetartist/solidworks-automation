# IWeldmentTrimExtendFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData`

Allows access to the data that defines a weldment trim extend feature.
Allows access to the data that defines a weldment trim extend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IWeldmentTrimExtendFeatureData 
```

```

Dim instance As IWeldmentTrimExtendFeatureData
```

```

public interface IWeldmentTrimExtendFeatureData 
```

```

public interface class IWeldmentTrimExtendFeatureData 
```

Remarks

Only bodies created by weldment features can be trimmed and extended. Only End Trim corner types can have multiple target and boundary bodies to trim. All other corner types can have only one target and boundary body to trim. For all other corner types, first valid body specified is used if more than one body is specified.

Example

[Get Weldment Trim Extend Corner Type (VBA)](Get_Weldment_Trim_Extend_Corner_Type_Example_VB.htm)  
[Get Weldment Trim Extend Corner Type (VB.NET)](Get_Weldment_Trim_Extend_Corner_Type_Example_VBNET.htm)  
[Get Weldment Trim Extend Corner Type (C#)](Get_Weldment_Trim_Extend_Corner_Type_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::InsertWeldmentTrimFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature2.md)  
[IFeatureManager::InsertWeldmentTrimFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature.md)

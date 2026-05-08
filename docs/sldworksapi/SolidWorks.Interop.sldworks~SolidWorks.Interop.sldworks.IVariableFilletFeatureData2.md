# IVariableFilletFeatureData2 Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2`

Allows access to a variable radius fillet feature.
Allows access to a variable radius fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IVariableFilletFeatureData2 
```

```

Dim instance As IVariableFilletFeatureData2
```

```

public interface IVariableFilletFeatureData2 
```

```

public interface class IVariableFilletFeatureData2 
```

Remarks

To create a variable fillet feature, follow the instructions in the Remarks section of [IFeatureManager::FeatureFillet3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet3.md).

To edit a variable fillet feature:

1. Call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md).
2. Call [IVariableFilletFeatureData2::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~AccessSelections.md).
3. Modify properties on this interface as needed and call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).
4. If nothing is modified, call [IVariableFilletFeatureData2::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ReleaseSelectionAccess.md).

For more information, read the **Variable Size Fillets** topic in the SOLIDWORKS user-interface help.

Example

[Create Variable Radius Asymmetric Elliptical Fillet (VBA)](Create_Asymmetric_Elliptic_Fillets_Example_VB.htm)  
[Create Variable Radius Asymmetric Elliptical Fillet (VB.NET)](Create_Asymmetric_Elliptic_Fillets_Example_VBNET.htm)  
[Create Variable Radius Asymmetric Elliptical Fillet (C#)](Create_Asymmetric_Elliptic_Fillets_Example_CSharp.htm)  
[Create Curvature Continuous Variable Fillet Feature (C#)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_CSharp.htm)  
[Create Curvature Continuous Variable Fillet Feature (VB.NET)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VBNET.htm)  
[Create Curvature Continuous Variable Fillet Feature (VBA)](Create_Curvature_Continuous_Variable_Fillet_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)

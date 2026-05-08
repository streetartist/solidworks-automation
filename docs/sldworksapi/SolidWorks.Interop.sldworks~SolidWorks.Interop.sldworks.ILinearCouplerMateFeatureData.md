# ILinearCouplerMateFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData`

Allows access to linear/linear coupler mate feature data.
Allows access to linear/linear coupler mate feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ILinearCouplerMateFeatureData 
```

```

Dim instance As ILinearCouplerMateFeatureData
```

```

public interface ILinearCouplerMateFeatureData 
```

```

public interface class ILinearCouplerMateFeatureData 
```

Remarks

A linear/linear coupler mate establishes a relationship between the translation of one component and the translation of another component.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) is the parent of this advanced mate interface.

To create a linear/linear coupler mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md) Remarks.
2. Specify [ILinearCouplerMateFeatureData::MateEntity1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~MateEntity1.md) and [ILinearCouplerMateFeatureData::MateEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~MateEntity2.md).
3. Specify other properties of the LinearCouplerMateFeatureData object as required.

To edit a linear/linear coupler mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a LinearCouplerMateFeatureData object.
3. Modify the LinearCouplerMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).

To delete a linear/linear coupler mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.md).

Example

[Create and Edit Linear-Linear Coupler Mate (VBA)](Create_Linear_Coupler_Mate_Example_VB.htm)  
[Create and Edit Linear-Linear Coupler Mate (C#)](Create_Linear_Coupler_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

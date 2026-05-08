# IWidthMateFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData`

Allows access to width mate feature data.
Allows access to width mate feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IWidthMateFeatureData 
```

```

Dim instance As IWidthMateFeatureData
```

```

public interface IWidthMateFeatureData 
```

```

public interface class IWidthMateFeatureData 
```

Remarks

A width mate constrains a tab between two planar faces.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) is the parent of this advanced mate interface.

To create a width mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md) Remarks.
2. Specify [IWidthMateFeatureData::TabSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~TabSelection.md) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the tab using Mark = 16.
3. Specify [IWidthMateFeatureData::WidthSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~WidthSelection.md) or use IModelDocExtension::SelectByID2 to pre-select the width using Mark = 1.
4. Specify [IWidthMateFeatureData::ConstraintType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~ConstraintType.md).
5. Specify other properties of the WidthMateFeatureData object as required.

To edit a width mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a WidthMateFeatureData object.
3. Modify the WidthMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).

To delete a width mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.md).

Example

[Create and Edit Width Mate (VBA)](Create_Width_Mate_Example_VB.htm)  
[Create and Edit Width Mate (C#)](Create_Width_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

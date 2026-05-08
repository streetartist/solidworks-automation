# ISymmetricMateFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData`

Allows access to symmetry mate feature data.
Allows access to symmetry mate feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISymmetricMateFeatureData 
```

```

Dim instance As ISymmetricMateFeatureData
```

```

public interface ISymmetricMateFeatureData 
```

```

public interface class ISymmetricMateFeatureData 
```

Remarks

Symmetry mates force two similar entities to be symmetric about a plane or planar face.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) is the parent of this advanced mate interface.

To create a symmetry mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md) Remarks.
2. Specify [ISymmetricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~EntitiesToMate.md) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities using Mark = 1.
3. Specify [ISymmetricMateFeatureData::SymmetryPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~SymmetryPlane.md) or use IModelDocExtension::SelectByID2 to pre-select the symmetry plane using Mark = 4.
4. Specify other properties of the SymmetricMateFeatureData object as required.

To edit a symmetry mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a SymmetricMateFeatureData object.
3. Modify the SymmetricMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).

To delete a symmetry mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.md).

Example

[Create and Edit Symmetric Mate (VBA)](Create_Symmetric_Mate_Example_VB.htm)  
[Create and Edit Symmetric Mate (C#)](Create_Symmetric_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISymmetricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)

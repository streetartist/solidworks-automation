# IMirrorComponentFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData`

Allows access to a mirror component feature.
Allows access to a mirror component feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IMirrorComponentFeatureData 
```

```

Dim instance As IMirrorComponentFeatureData
```

```

public interface IMirrorComponentFeatureData 
```

```

public interface class IMirrorComponentFeatureData 
```

Remarks

Before calling [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md) to access this interface, you can pre-select the entities needed to create the mirror component feature:

| To specify... | Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) using selection Mark... |
| --- | --- |
| Mirror plane | 1 |
| Components to mirror | 2 |
| Alignment references | 4 |

To create a basic Mirror Component feature, use at a minimum:

- [IMirrorComponentFeatureData::MirrorPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorPlane.md)
- [IMirrorComponentFeatureData::ComponentsToInstanceAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToComponentOrigin.md)
- (Optional) [IMirrorComponentFeatureData::MirrorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorType.md) (if not explicitly set, defaults to [swMirrorComponentMirrorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentMirrorType_e.html).swMirrorType\_CenterOfBoundingBox)
- (Optional) [IMirrorComponentFeatureData::ComponentOrientationsAlignToComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToComponentOrigin.md) (if not explicitly set, defaults to [swMirrorComponentOrientation2\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentOrientation2_e.html).swOrientation\_MirroredX\_MirroredY)

To create a mirror instance as a copy of the component, positioned symmetrically about a plane in one of four orientations (for fully symmetric components, all four orientations are true mirrors), use:

- MirrorPlane
- MirrorType
- ComponentOrientationsAlignToComponentOrigin
- [ComponentOrientationsAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentOrientationsAlignToSelection.md)
- ComponentsToInstanceAlignToComponentOrigin
- [ComponentsToInstanceAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToSelection.md)
- [AlignmentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~AlignmentReferences.md)
- [FlipDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~FlipDirections.md)
- [SyncFlexibleSubAssemblies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~SyncFlexibleSubAssemblies.md)

To create a new opposite-hand version of the component (a true mirror of a nonsymmetric component), positioned symmetrically about a plane, use:

- MirrorPlane
- MirrorType
- [CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.md)
- [OppositeHandComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~OppositeHandComponents.md)
- [MirrorComponentsFolderLocation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorComponentsFolderLocation.md)
- [PlaceFilesInOneFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PlaceFilesInOneFolder.md)
- [MirroredComponentFilenames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirroredComponentFilenames.md)
- [NameModifier](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifier.md)
- [NameModifierType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~NameModifierType.md)
- [ReplaceFileLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ReplaceFileLocations.md)
- [MirrorTransferOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~MirrorTransferOptions.md)
- [DimXpertScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~DimXpertScheme.md)
- [BreakLinksToOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~BreakLinksToOriginalPart.md)
- [PreserveZAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PreserveZAxis.md)
- [PropagateFromOriginalPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PropagateFromOriginalPart.md)

After specifying this interface as needed, call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) to create the feature.

This interface is analogous in functionality to the Mirror Components PropertyManager. See the following topics in the SOLIDWORKS user-interface help for more information:

- ****Comparing Types of Mirror Components****
- **Mirroring Components**

Example

[Mirror Components II (VBA)](Mirror_Components_II_Example_VB.htm)  
[Mirror Components II (VB.NET)](Mirror_Components_II_Example_VBNET.htm)  
[Mirror Components II (C#)](Mirror_Components_II_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IComponent2::IsMirrored Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsMirrored.md)  
[IPartDoc::IsMirrored Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsMirrored.md)

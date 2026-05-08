# MirrorComponents3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MirrorComponents3`

Obsolete. Superseded by IFeatureManager::CreateDefinition, IFeatureManager::CreateFeature, and IMirrorComponentFeatureData.
Obsolete. Superseded by [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md), [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md), and [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MirrorComponents3( _
   ByVal MirrorPlane As System.Object, _
   ByVal ComponentsToInstance As System.Object, _
   ByVal ComponentOrientations As System.Object, _
   ByVal OrientAboutCenterOfMass As System.Boolean, _
   ByVal ComponentsToMirror As System.Object, _
   ByVal CreateDerivedConfigurations As System.Boolean, _
   ByVal MirroredComponentFilenames As System.Object, _
   ByVal NameModifierType As System.Integer, _
   ByVal NameModifier As System.String, _
   ByVal MirroredComponentFileLocation As System.String, _
   ByVal ImportOptions As System.Integer, _
   ByVal BreakLinks As System.Boolean, _
   ByVal PreserveZAxis As System.Boolean, _
   ByVal SyncFlexibleSubAssemblies As System.Boolean _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim MirrorPlane As System.Object
Dim ComponentsToInstance As System.Object
Dim ComponentOrientations As System.Object
Dim OrientAboutCenterOfMass As System.Boolean
Dim ComponentsToMirror As System.Object
Dim CreateDerivedConfigurations As System.Boolean
Dim MirroredComponentFilenames As System.Object
Dim NameModifierType As System.Integer
Dim NameModifier As System.String
Dim MirroredComponentFileLocation As System.String
Dim ImportOptions As System.Integer
Dim BreakLinks As System.Boolean
Dim PreserveZAxis As System.Boolean
Dim SyncFlexibleSubAssemblies As System.Boolean
Dim value As System.Object
 
value = instance.MirrorComponents3(MirrorPlane, ComponentsToInstance, ComponentOrientations, OrientAboutCenterOfMass, ComponentsToMirror, CreateDerivedConfigurations, MirroredComponentFilenames, NameModifierType, NameModifier, MirroredComponentFileLocation, ImportOptions, BreakLinks, PreserveZAxis, SyncFlexibleSubAssemblies)
```

```

System.object MirrorComponents3( 
   System.object MirrorPlane,
   System.object ComponentsToInstance,
   System.object ComponentOrientations,
   System.bool OrientAboutCenterOfMass,
   System.object ComponentsToMirror,
   System.bool CreateDerivedConfigurations,
   System.object MirroredComponentFilenames,
   System.int NameModifierType,
   System.string NameModifier,
   System.string MirroredComponentFileLocation,
   System.int ImportOptions,
   System.bool BreakLinks,
   System.bool PreserveZAxis,
   System.bool SyncFlexibleSubAssemblies
)
```

```

System.Object^ MirrorComponents3( 
   System.Object^ MirrorPlane,
   System.Object^ ComponentsToInstance,
   System.Object^ ComponentOrientations,
   System.bool OrientAboutCenterOfMass,
   System.Object^ ComponentsToMirror,
   System.bool CreateDerivedConfigurations,
   System.Object^ MirroredComponentFilenames,
   System.int NameModifierType,
   System.String^ NameModifier,
   System.String^ MirroredComponentFileLocation,
   System.int ImportOptions,
   System.bool BreakLinks,
   System.bool PreserveZAxis,
   System.bool SyncFlexibleSubAssemblies
) 
```

#### Parameters

*MirrorPlane*
:   [Reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) or planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) about which to mirror the components

*ComponentsToInstance*
:   Array of seed [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) with which to create copy mirror components

*ComponentOrientations*
:   Array of [swMirrorComponentOrientation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorComponentOrientation_e.html) values; valid only if ComponentsToInstance is not Nothing or null

*OrientAboutCenterOfMass*
:   True to orient the mirror components about the center of mass, false to orient them about the bounding box center

*ComponentsToMirror*
:   Array of seed components with which to create opposite-hand mirror components

*CreateDerivedConfigurations*
:   True to create a derived configuration of the mirror components in the original assembly, false to create new part files; valid only if ComponentsToMirror and MirroredComponentFilenames are not Nothing or null and NameModifierType is [swMirrorComponentNameModifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorComponentNameModifier_e.html).swMirrorComponentName\_Custom

*MirroredComponentFilenames*
:   Array of mirror part file names whose names can be further modified by the settings of NameModifierType and NameModifier; if CreateDerivedConfigurations is true, then this array contains the names for the new configurations and NameModifierType must be swMirrorComponentNameModifier\_e.swMirrorComponentName\_Custom; valid only if ComponentsToMirror is not Nothing or null

*NameModifierType*
:   Mirror part file name modifier type as defined in swMirrorComponentNameModifier\_e; valid only if ComponentsToMirror and MirroredComponentFilenames are not Nothing or null

*NameModifier*
:   Prefix or suffix to apply to file names of mirror parts; valid only if NameModifierType is swMirrorComponentNameModifier\_e.swMirrorComponentName\_Prefix or swMirrorComponentNameModifier\_e.swMirrorComponentName\_Suffix and ComponentsToMirror and if MirroredComponentFilenames are not Nothing or null

*MirroredComponentFileLocation*
:   Folder where to save the mirror parts; valid only if CreateDerivedConfigurations is false

*ImportOptions*
:   Mirror transfer options as defined in [swMirrorPartOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorPartOptions_e.html)

*BreakLinks*
:   True to break the links between the mirror parts and the original parts, false to keep the links

*PreserveZAxis*
:   True to mirror the Z-axis orientation in the mirror part, false to flip the Z-axis orientation in the mirror part

*SyncFlexibleSubAssemblies*
:   True to synchronize the movement of flexible subassembly components with the parent component, false to not

#### Return Value

Array of mirror [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Example

[Mirror Components (C#)](Mirror_Components_Example_CSharp.htm)  
[Mirror Components (VB.NET)](Mirror_Components_Example_VBNET.htm)  
[Mirror Components (VBA)](Mirror_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IComponent2::IsMirrored Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsMirrored.md)  
[IPartDoc::IsMirrored Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsMirrored.md)

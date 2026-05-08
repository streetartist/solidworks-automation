# ReferencedConfiguration Property (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration`

Gets or sets the active configuration used by this component.
Gets or sets the active configuration used by this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencedConfiguration As System.String
```

```

Dim instance As IComponent2
Dim value As System.String
 
instance.ReferencedConfiguration = value
 
value = instance.ReferencedConfiguration
```

```

System.string ReferencedConfiguration {get; set;}
```

```

property System.String^ ReferencedConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the configuration

Remarks

You can use this property to change the active configuration of:

- a pattern seed component.
- pattern instance components, but only when the pattern's ForceUseSeedConfiguration property is set to false.

When the configuration is changed, components might become suppressed or unsuppressed. This means that the array previously returned from [IComponent2::GetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.md) or [IComponent2::IGetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildren.md) becomes invalid. If an application is traversing an assembly and calls IComponent2::ReferencedConfiguration, then it should stop the traversal and start again by getting the assembly's [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) and active configuration. The array previously returned from IComponent2::GetChildren or IComponent2::IGetChildren should be released before calling IComponent2::ReferencedConfiguration. To hold onto the changed component, you can perform an extra AddRef() on that component before freeing the array.

After changing the referenced configuration, you must call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) to display the changes.

Example

[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)  
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)  
[Change Referenced Configuration (VBA)](Change_Referenced_Configuration_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.md)  
[IChainPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ForceUseSeedConfiguration.md)  
[IDerivedPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~ForceUseSeedConfiguration.md)  
[ILocalCircularPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ForceUseSeedConfiguration.md)  
[ILocalCurvePatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~ForceUseSeedConfiguration.md)  
[ILocalLinearPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ForceUseSeedConfiguration.md)  
[ILocalSketchPatternFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~ForceUseSeedConfiguration.md)  
[IMirrorComponentFeatureData::ForceUseSeedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ForceUseSeedConfiguration.md)

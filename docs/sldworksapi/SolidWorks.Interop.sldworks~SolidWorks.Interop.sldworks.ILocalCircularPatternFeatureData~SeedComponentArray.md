# SeedComponentArray Property (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SeedComponentArray`

Gets or sets an array of seed component features for this circular component pattern feature.
Gets or sets an array of seed component features for this circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SeedComponentArray As System.Object
```

```

Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Object
 
instance.SeedComponentArray = value
 
value = instance.SeedComponentArray
```

```

System.object SeedComponentArray {get; set;}
```

```

property System.Object^ SeedComponentArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of seed component [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

You can:

- get the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object for each seed component represented by a feature using [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md).
- pass a mixed array of IComponent2 and [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) objects representing components.

See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Get and Set Seed Components (VBA)](Get_and_Set_Seed_Components_Example_VB.htm)  
[Get and Set Seed Components (VB.NET)](Get_and_Set_Seed_Components_Example_VBNET.htm)  
[Get and Set Seed Components (C#)](Get_and_Set_Seed_Components_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)  
[ILocalCircularPatternFeatureData::GetSeedComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetSeedComponentCount.md)  
[ILocalCircularPatternFeatureData::IGetSeedComponentArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSeedComponentArray.md)  
[ILocalCircularPatternFeatureData::ISetSeedComponentArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ISetSeedComponentArray.md)

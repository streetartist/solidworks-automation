# ISetSeedComponentArray Method (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ISetSeedComponentArray`

Sets an array of seed component features for this circular component pattern feature.
Sets an array of seed component features for this circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSeedComponentArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
) 
```

```

Dim instance As ILocalCircularPatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Object
 
instance.ISetSeedComponentArray(FeatCount, ArrayDataIn)
```

```

void ISetSeedComponentArray( 
   System.int FeatCount,
   ref System.object ArrayDataIn
)
```

```

void ISetSeedComponentArray( 
   System.int FeatCount,
   System.Object^% ArrayDataIn
) 
```

#### Parameters

*FeatCount*
:   Number of seed components

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of seed component [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) (see **Remarks**)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

You can pass a mixed array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) and [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) objects representing components.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)  
[ILocalCircularPatternFeatureData::GetSeedComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetSeedComponentCount.md)  
[ILocalCircularPatternFeatureData::IGetSeedComponentArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSeedComponentArray.md)  
[ILocalCircularPatternFeatureData::SeedComponentArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SeedComponentArray.md)

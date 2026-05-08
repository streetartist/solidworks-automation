# PostIntersect Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostIntersect`

Creates an intersect feature.
Creates an intersect feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PostIntersect( _
   ByVal IntersectionsToExclude As System.Object, _
   ByVal Merge As System.Boolean, _
   ByVal Consume As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim IntersectionsToExclude As System.Object
Dim Merge As System.Boolean
Dim Consume As System.Boolean
Dim value As Feature
 
value = instance.PostIntersect(IntersectionsToExclude, Merge, Consume)
```

```

Feature PostIntersect( 
   System.object IntersectionsToExclude,
   System.bool Merge,
   System.bool Consume
)
```

```

Feature^ PostIntersect( 
   System.Object^ IntersectionsToExclude,
   System.bool Merge,
   System.bool Consume
) 
```

#### Parameters

*IntersectionsToExclude*
:   Array of booleans indicating which bodies returned by [IFeatureManager::PreIntersect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreIntersect.md) to exclude from this intersect feature

*Merge*
:   True to merge all intersect regions into one body, false to not

*Consume*
:   True to remove input surfaces from the FeatureManager design tree, false to not

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, you must call [IFeatureManager::PreIntersect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreIntersect.md) to obtain the intersect bodies.

Example

[Get Intersect Feature Data (VBA)](Get_Intersect_Feature_Data_Example_VB.htm)  
[Get Intersect Feature Data (VB.NET)](Get_Intersect_Feature_Data_Example_VBNET.htm)  
[Get Intersect Feature Data (C#)](Get_Intersect_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)

# InsertGridFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGridFeature`

Inserts a Grid System feature.
Inserts a Grid System feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertGridFeature( _
   ByVal HeightDoubles As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim HeightDoubles As System.Object
Dim value As Feature
 
value = instance.InsertGridFeature(HeightDoubles)
```

```

Feature InsertGridFeature( 
   System.object HeightDoubles
)
```

```

Feature^ InsertGridFeature( 
   System.Object^ HeightDoubles
) 
```

#### Parameters

*HeightDoubles*
:   Array of doubles specifying distances between Grid System levels

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

The number of elements in HeightDoubles determines the number of levels in this Grid System feature.

Example

[Insert Grid System Feature (C#)](Insert_Grid_System_Feature_Example_CSharp.htm)  
[Insert Grid System Feature (VB.NET)](Insert_Grid_System_Feature_Example_VBNET.htm)  
[Insert Grid System Feature (VBA)](Insert_Grid_System_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)

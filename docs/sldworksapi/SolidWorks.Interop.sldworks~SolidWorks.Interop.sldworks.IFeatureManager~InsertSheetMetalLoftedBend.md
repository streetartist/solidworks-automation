# InsertSheetMetalLoftedBend Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalLoftedBend`

Obsolete. Superseded by IFeatureManager::InsertSheetMetalLoftedBend2.
Obsolete. Superseded by [IFeatureManager::InsertSheetMetalLoftedBend2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalLoftedBend2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalLoftedBend( _
   ByVal ThickDirType As System.Integer, _
   ByVal Thickness As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim ThickDirType As System.Integer
Dim Thickness As System.Double
Dim value As Feature
 
value = instance.InsertSheetMetalLoftedBend(ThickDirType, Thickness)
```

```

Feature InsertSheetMetalLoftedBend( 
   System.int ThickDirType,
   System.double Thickness
)
```

```

Feature^ InsertSheetMetalLoftedBend( 
   System.int ThickDirType,
   System.double Thickness
) 
```

#### Parameters

*ThickDirType*
:   Toggles the thickening direction:

    - 0 = outside
    - 1 = inside (default value)

*Thickness*
:   Thickness of the bend

#### Return Value

Pointer to the lofted-bend [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) in the sheet metal part

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)

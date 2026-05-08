# InsertEndCapFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature`

Obsolete. Superseded by IFeatureManager::InsertEndCapFeature3.
Obsolete. Superseded by [IFeatureManager::InsertEndCapFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertEndCapFeature( _
   ByVal Depth As System.Double, _
   ByVal BIsGivenOffset As System.Boolean, _
   ByVal BIsChamfer As System.Boolean, _
   ByVal OffsetValue As System.Double, _
   ByVal WallThicknessRatio As System.Double, _
   ByVal ChamferValue As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Depth As System.Double
Dim BIsGivenOffset As System.Boolean
Dim BIsChamfer As System.Boolean
Dim OffsetValue As System.Double
Dim WallThicknessRatio As System.Double
Dim ChamferValue As System.Double
Dim value As Feature
 
value = instance.InsertEndCapFeature(Depth, BIsGivenOffset, BIsChamfer, OffsetValue, WallThicknessRatio, ChamferValue)
```

```

Feature InsertEndCapFeature( 
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue
)
```

```

Feature^ InsertEndCapFeature( 
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue
) 
```

#### Parameters

*Depth*
:   Thickness of the end cap

*BIsGivenOffset*
:   True to provide an offset value, false to provide a thickness ratio

*BIsChamfer*
:   True if end cap feature is chamfered, false if end cap is filleted

*OffsetValue*
:   Edge offset value; valid only if BIsGivenOffset is true

*WallThicknessRatio*
:   Wall thickness ratio; valid only if BIsGivenOffset is false

*ChamferValue*
:   Chamfer distance if BIsChamfer is true, fillet radius if BIsChamfer is false

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)

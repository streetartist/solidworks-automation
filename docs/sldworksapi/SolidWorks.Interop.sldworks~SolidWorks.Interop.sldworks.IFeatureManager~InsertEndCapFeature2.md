# InsertEndCapFeature2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature2`

Inserts an end cap feature using the specified end faces of a structural member.
Inserts an end cap feature using the specified end faces of a structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertEndCapFeature2( _
   ByVal Depth As System.Double, _
   ByVal BIsGivenOffset As System.Boolean, _
   ByVal BIsChamfer As System.Boolean, _
   ByVal OffsetValue As System.Double, _
   ByVal WallThicknessRatio As System.Double, _
   ByVal ChamferValue As System.Double, _
   ByVal Faces As System.Object _
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
Dim Faces As System.Object
Dim value As Feature
 
value = instance.InsertEndCapFeature2(Depth, BIsGivenOffset, BIsChamfer, OffsetValue, WallThicknessRatio, ChamferValue, Faces)
```

```

Feature InsertEndCapFeature2( 
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue,
   System.object Faces
)
```

```

Feature^ InsertEndCapFeature2( 
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue,
   System.Object^ Faces
) 
```

#### Parameters

*Depth*
:   Depth of the end cap

*BIsGivenOffset*
:   True if end cap is offset, false if not

*BIsChamfer*
:   True if end cap feature is chamfered, false If not

*OffsetValue*
:   Value by which to offset the end cap

*WallThicknessRatio*
:   Wall thickness ratio

*ChamferValue*
:   Angle of the chamfer

*Faces*
:   Array of [Face2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) objects

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Call [IFeatureManager::InsertEndCapFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature3.md) if you want to pre-select the faces to end-cap in the graphics area.

Example

[Insert Weldment Features (VBA)](Insert_Weldment_Features_Example_VB.htm)  
[Insert Weldment Features (VB.NET)](Insert_Weldment_Features_Example_VBNET.htm)  
[Insert Weldment Features (C#)](Insert_Weldment_Features_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md)

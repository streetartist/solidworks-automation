# InsertEndCapFeature3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature3`

Inserts an end cap feature for one or more pre-selected open ends of a structural member.
Inserts an end cap feature for one or more pre-selected open ends of a structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertEndCapFeature3( _
   ByVal Depth As System.Double, _
   ByVal BIsGivenOffset As System.Boolean, _
   ByVal BIsChamfer As System.Boolean, _
   ByVal OffsetValue As System.Double, _
   ByVal WallThicknessRatio As System.Double, _
   ByVal ChamferValue As System.Double, _
   ByVal BIsCornerTreatment As System.Boolean, _
   ByVal DepthOffset As System.Double, _
   ByVal BIsReverse As System.Boolean, _
   ByVal BIsEndCapInward As System.Integer _
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
Dim BIsCornerTreatment As System.Boolean
Dim DepthOffset As System.Double
Dim BIsReverse As System.Boolean
Dim BIsEndCapInward As System.Integer
Dim value As Feature
 
value = instance.InsertEndCapFeature3(Depth, BIsGivenOffset, BIsChamfer, OffsetValue, WallThicknessRatio, ChamferValue, BIsCornerTreatment, DepthOffset, BIsReverse, BIsEndCapInward)
```

```

Feature InsertEndCapFeature3( 
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue,
   System.bool BIsCornerTreatment,
   System.double DepthOffset,
   System.bool BIsReverse,
   System.int BIsEndCapInward
)
```

```

Feature^ InsertEndCapFeature3( 
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue,
   System.bool BIsCornerTreatment,
   System.double DepthOffset,
   System.bool BIsReverse,
   System.int BIsEndCapInward
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

*BIsCornerTreatment*
:   True to chamfer or fillet the end cap corners, false to not; valid only if BIsGivenOffset is false

*DepthOffset*
:   Inset distance; valid only if BIsEndCapInward = 2

*BIsReverse*
:   True to reverse the offset or thickness ratio, false to not

*BIsEndCapInward*
:   Thickness direction as defined in [swEndCapThicknessDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndCapThicknessDirection_e.html)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, select one or more end [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of a structural member in the graphics area.

Instead of using this method, you can pass the faces in an argument array of [IFeatureManager::InsertEndCapFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature2.md).

Example

[Insert Weldment End Cap (VBA)](Insert_Weldment_End_Cap_Example_VB.htm)  
[Insert Weldment End Cap (VB.NET)](Insert_Weldment_End_Cap_Example_VBNET.htm)  
[Insert Weldment End Cap (C#)](Insert_Weldment_End_Cap_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md)

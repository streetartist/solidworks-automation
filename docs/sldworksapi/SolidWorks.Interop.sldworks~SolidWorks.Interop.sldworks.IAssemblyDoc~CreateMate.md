# CreateMate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate`

Creates a mate with the specified feature data object.
Creates a mate with the specified feature data object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateMate( _
   ByVal MateData As System.Object _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim MateData As System.Object
Dim value As System.Object
 
value = instance.CreateMate(MateData)
```

```

System.object CreateMate( 
   System.object MateData
)
```

```

System.Object^ CreateMate( 
   System.Object^ MateData
) 
```

#### Parameters

*MateData*
:   Mate-specific object (see **Remarks**)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) is the base interface for the following mate-specific interfaces (an asterisk indicates that pre-selection of mate entities during mate creation is supported):

- [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.md)
- [ICamFollowerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData.md) \*
- [ICoincidentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.md) \*
- [IConcentricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.md) \*
- [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md)
- [IGearMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.md) \*
- [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.md) \*
- [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.md)
- [ILockMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData.md) \*
- [IParallelMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData.md) \*
- [IPerpendicularMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData.md) \*
- [IProfileCenterMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.md)
- [IRackPinionMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.md) \*
- [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.md) \*
- [ISlotMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.md) \*
- [ISymmetricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.md)
- [ITangentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.md) \*
- [IUniversalJointMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.md) \*
- [IWidthMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.md)

To create a standard, advanced, or mechanical mate:

1. Use [IAssemblyDoc::CreateMateData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMateData.md) to access a MateFeatureData object.
2. Set the general properties of the MateFeatureData object.
3. Cast the MateFeatureData object to one of the mate-specific objects.
4. Follow specific instructions in the Remarks of the mate-specific interface, set specific properties of the mate-specific object, and/or pre-select entities to mate for asterisked interfaces above.
5. Call this method, passing in the mate-specific object.

To create:

- Misaligned concentric mates, use [IAssemblyDoc::AddConcentricMateWithTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddConcentricMateWithTolerance.md).
- Cylindrical distance mates, use [IAssemblyDoc::AddDistanceMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate.md).

Example

See the Example sections of the interfaces listed in Remarks.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AutoMateRepair Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoMateRepair.md)

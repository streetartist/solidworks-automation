# SetDistance Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetDistance`

Sets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer.
Sets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDistance( _
   ByVal PFilletItem As System.Object, _
   ByVal Dist2 As System.Double _
) 
```

```

Dim instance As ISimpleFilletFeatureData2
Dim PFilletItem As System.Object
Dim Dist2 As System.Double
 
instance.SetDistance(PFilletItem, Dist2)
```

```

void SetDistance( 
   System.object PFilletItem,
   System.double Dist2
)
```

```

void SetDistance( 
   System.Object^ PFilletItem,
   System.double Dist2
) 
```

#### Parameters

*PFilletItem*
:   Item at which to set the Distance 2 radius

*Dist2*
:   Distance 2 radius of the asymmetric fillet/chamfer at PFilletItem

Remarks

Call [ISimpleFilletFeatureData2::SetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.md) to set the Distance 1 radius.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::GetDistance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetDistance.md)  
[ISimpleFilletFeatureData2::AsymmetricFillet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.md)

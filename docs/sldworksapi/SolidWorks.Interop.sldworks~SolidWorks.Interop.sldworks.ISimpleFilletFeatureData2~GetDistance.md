# GetDistance Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetDistance`

Gets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer.
Gets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDistance( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

```

Dim instance As ISimpleFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double
 
value = instance.GetDistance(PFilletItem)
```

```

System.double GetDistance( 
   System.object PFilletItem
)
```

```

System.double GetDistance( 
   System.Object^ PFilletItem
) 
```

#### Parameters

*PFilletItem*
:   Item at which to get the Distance 2radius

#### Return Value

Distance 2 radius at PFilletItem for this asymmetric fillet/chamfer

Remarks

Call [ISimpleFilletFeatureData2::GetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetRadius.md) to get the Distance 1 radius at PFilletItem for this asymmetric fillet/chamfer.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::SetDistance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetDistance.md)  
[ISimpleFilletFeatureData2::AsymmetricFillet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.md)

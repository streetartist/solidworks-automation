# CouplerRatioDenominator Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~CouplerRatioDenominator`

Gets or sets the displacement of the second mated component along its direction of motion in this linear/linear coupler mate.
Gets or sets the displacement of the second mated component along its direction of motion in this linear/linear coupler mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CouplerRatioDenominator As System.Double
```

```

Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Double
 
instance.CouplerRatioDenominator = value
 
value = instance.CouplerRatioDenominator
```

```

System.double CouplerRatioDenominator {get; set;}
```

```

property System.double CouplerRatioDenominator {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Coupler ratio denominator

Remarks

ILinearCouplerMateFeatureData::CouplerRatioNumerator / ILinearCouplerMateFeatureData::CouplerRatioDenominator describes the ratio of displacement between the first and second mated components.

Example

See the [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.md)  
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.md)

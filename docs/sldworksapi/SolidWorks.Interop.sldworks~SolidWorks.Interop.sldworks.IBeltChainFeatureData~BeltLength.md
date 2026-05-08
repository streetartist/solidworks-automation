# BeltLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltLength`

Gets and sets the belt length.
Gets and sets the belt length.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BeltLength As System.Double
```

```

Dim instance As IBeltChainFeatureData
Dim value As System.Double
 
instance.BeltLength = value
 
value = instance.BeltLength
```

```

System.double BeltLength {get; set;}
```

```

property System.double BeltLength {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Belt length

Remarks

This property can only be set if [IBeltChainFeatureData::DrivingLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~DrivingLength.md) is set to true.

Example

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)
